import sys
import questionary
from rich.console import Console
from .config import config
from .entities.registry import ENTITY_CATEGORIES, Companies, Contacts, Opportunities, SalesOrders, Tickets
from .cli.formatting import print_table, print_json, print_summary

console = Console()

OPERATORS = {
    "=": "eq",
    "contains": "contains",
    ">": "gt",
    "<": "lt",
    "!=": "noteq"
}

def main_menu():
    try:
        config.validate()
    except ValueError as e:
        console.print(f"[red]Configuration Error: {e}[/red]")
        console.print("Please check your .env file. See .env.example for details.")
        sys.exit(1)

    while True:
        # Build top-level choices: categories + custom scripts + exit
        category_names = list(ENTITY_CATEGORIES.keys())
        choices = category_names + ["Custom Script", "Exit"]

        category = questionary.select(
            "Select Category (Autotask):",
            choices=choices
        ).ask()

        if category == "Exit":
            break

        if category == "Custom Script":
            handle_custom_script()
            continue

        # Second level: pick an entity within the selected category
        entity_map = ENTITY_CATEGORIES[category]
        entity_menu(category, entity_map)


def entity_menu(category_name, entity_map):
    """Let the user pick an entity within a category, then show the action menu."""
    while True:
        entity_names = list(entity_map.keys())
        choices = entity_names + ["Back"]

        entity_label = questionary.select(
            f"Select Entity [{category_name}]:",
            choices=choices
        ).ask()

        if entity_label == "Back":
            break

        entity_cls = entity_map[entity_label]
        action_menu(entity_label, entity_cls)


def action_menu(name, cls):
    while True:
        # Build available actions based on entity capabilities
        actions = ["View (List)", "View by ID"]
        if cls.can_create:
            actions.append("Create")
        if cls.can_update:
            actions.append("Update")
        if cls.can_delete:
            actions.append("Delete")
        actions.append("Back")

        action = questionary.select(
            f"Action for {name}:",
            choices=actions
        ).ask()

        if action == "Back":
            break
        elif action == "View (List)":
            handle_list(cls)
        elif action == "View by ID":
            handle_get(cls)
        elif action == "Create":
            handle_create(cls)
        elif action == "Update":
            handle_update(cls)
        elif action == "Delete":
            handle_delete(cls)

def handle_list(cls):
    limit = questionary.text("How many records to view? (max 500, default 10):", default="10").ask()
    try:
        limit = int(limit)
    except:
        limit = 10

    filters = []
    if questionary.confirm("Filter by field?").ask():
        field = questionary.text("Field name:").ask()
        op_label = questionary.select("Operator:", choices=list(OPERATORS.keys())).ask()
        value = questionary.text("Value:").ask()
        filters.append({"op": OPERATORS[op_label], "field": field, "value": value})

    try:
        items = cls.list(limit=limit, filters=filters if filters else None)
        print_table(items, cls.display_fields)
        
        if items and questionary.confirm("View details for one record?").ask():
            record_id = questionary.text("Enter ID:").ask()
            item = cls.get(record_id)
            print_json(item)
    except Exception as e:
        console.print(f"[red]Error fetching list: {e}[/red]")

def handle_get(cls):
    record_id = questionary.text("Enter ID:").ask()
    try:
        item = cls.get(record_id)
        if item:
            print_json(item)
            print_summary(item, cls.display_fields)
        else:
            console.print("[yellow]Record not found.[/yellow]")
    except Exception as e:
        console.print(f"[red]Error fetching record: {e}[/red]")

def handle_create(cls):
    if not cls.can_create:
        console.print(f"[yellow]{cls.__name__} does not support create operations.[/yellow]")
        return

    data = {}
    console.print(f"\n[bold]Creating {cls.__name__}[/bold]")
    for field in cls.required_fields:
        val = questionary.text(f"{field} (required):").ask()
        # Try to coerce to int for known ID-like fields
        if field.endswith("ID") or field in ("isActive", "companyType", "ownerResourceID", "status", "priority"):
            try:
                data[field] = int(val)
            except ValueError:
                data[field] = val
        else:
            data[field] = val
    
    while questionary.confirm("Add more fields?").ask():
        field = questionary.text("Field name:").ask()
        val = questionary.text("Value:").ask()
        data[field] = val
    
    try:
        result = cls.create(data)
        new_id = result.get("itemId")
        console.print(f"[green]Successfully created! ID: {new_id}[/green]")
    except Exception as e:
        console.print(f"[red]Error creating record: {e}[/red]")

def handle_update(cls):
    if not cls.can_update:
        console.print(f"[yellow]{cls.__name__} does not support update operations.[/yellow]")
        return

    record_id = questionary.text("Enter ID to update:").ask()
    data = {}
    console.print(f"\n[bold]Updating {cls.__name__} {record_id}[/bold]")
    
    while True:
        field = questionary.text("Field name to update (or leave empty to finish):").ask()
        if not field:
            break
        val = questionary.text(f"New value for {field}:").ask()
        data[field] = val
    
    if not data:
        console.print("[yellow]No fields to update.[/yellow]")
        return

    if questionary.confirm("Execute update?").ask():
        try:
            cls.update(record_id, data)
            console.print("[green]Update successful.[/green]")
        except Exception as e:
            console.print(f"[red]Error updating record: {e}[/red]")

def handle_delete(cls):
    if not cls.can_delete:
        console.print(f"[yellow]{cls.__name__} does not support delete operations.[/yellow]")
        return

    record_id = questionary.text("Enter ID to delete:").ask()
    confirm = questionary.text(f"Type DELETE to confirm deleting {record_id}:").ask()
    
    if confirm == "DELETE":
        try:
            cls.delete(record_id)
            console.print("[green]Record deleted successfully (or set to inactive).[/green]")
        except Exception as e:
            console.print(f"[red]Error deleting record: {e}[/red]")
    else:
        console.print("[yellow]Deletion cancelled.[/yellow]")

def handle_custom_script():

    return


if __name__ == "__main__":
    main_menu()
