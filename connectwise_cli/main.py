import sys
import questionary
from rich.console import Console
from .config import config
from .entities.registry import (
    ENTITY_CATEGORIES,
    Companies as CWCompanies,
    CompanyContacts as CWContacts,
    ServiceBoards,
    Priorities,
    ServiceSources,
    Impacts,
    Severities,
    ServiceLocations,
    SLAs,
)
from .client import client as cw_client
from .cli.formatting import print_table, print_json, print_summary

console = Console()

def main_menu():
    try:
        config.validate()
    except ValueError as e:
        console.print(f"[red]Configuration Error: {e}[/red]")
        console.print("Please check your .env file. Ensure all CONNECTWISE_* variables are set.")
        sys.exit(1)

    while True:
        # Build top-level choices: categories + custom scripts + exit
        category_names = list(ENTITY_CATEGORIES.keys())
        choices = category_names + [
            "Custom Script - [AT -> CW] Get Billing Contacts from CW",
            "Custom Script - [AT -> AT] Update Contacts to Billing contacts in AT",
            "Custom Script - [CW -> AT] Sync Billing Contacts to Autotask",
            "Custom Script - [CW -> AT] Sync Primary Contacts to Autotask",
            "Custom Script - [CW] Export Board Ticket Properties",
            "Exit"
        ]

        category = questionary.select(
            "Select Category (ConnectWise):",
            choices=choices
        ).ask()

        if category == "Exit":
            break

        if category == "Custom Script - [AT -> CW] Get Billing Contacts from CW":
            handle_custom_script1()
            continue

        if category == "Custom Script - [AT -> AT] Update Contacts to Billing contacts in AT":
            handle_custom_script2()
            continue

        if category == "Custom Script - [CW -> AT] Sync Billing Contacts to Autotask":
            handle_custom_script3()
            continue

        if category == "Custom Script - [CW -> AT] Sync Primary Contacts to Autotask":
            handle_custom_script4()
            continue

        if category == "Custom Script - [CW] Export Board Ticket Properties":
            handle_custom_script5()
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
    limit = questionary.text("How many records to view? (default 10):", default="10").ask()
    try:
        limit = int(limit)
    except:
        limit = 10

    filters = None
    if questionary.confirm("Filter by 'conditions'?").ask():
        filters = questionary.text('Enter condition string (e.g., name="CompanyName"):').ask()

    try:
        items = cls.list(limit=limit, filters=filters)
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
        data[field] = val
    
    while questionary.confirm("Add more fields?").ask():
        field = questionary.text("Field name:").ask()
        val = questionary.text("Value:").ask()
        data[field] = val
    
    try:
        result = cls.create(data)
        new_id = result.get("id")
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
            console.print("[green]Record deleted successfully.[/green]")
        except Exception as e:
            console.print(f"[red]Error deleting record: {e}[/red]")
    else:
        console.print("[yellow]Deletion cancelled.[/yellow]")

def handle_custom_script1():
    import csv
    from datetime import datetime
    from autotask_cli.entities.registry import Companies as ATCompanies
    
    limit_str = questionary.text("How many Autotask companies to process? (Leave empty for ALL):").ask()
    limit = None
    if limit_str:
        try:
            limit = int(limit_str)
        except:
            limit = None
            
    if limit is None:
        console.print("[yellow]Fetching ALL companies from Autotask. This may take a while...[/yellow]")
    else:
        console.print(f"[bold]Fetching first {limit} companies from Autotask...[/bold]")
        
    try:
        at_companies = ATCompanies.list(limit=limit)
        total_at = len(at_companies)
        console.print(f"[green]Found {total_at} Autotask companies.[/green]")
        
        results = []
        for i, at_comp in enumerate(at_companies, 1):
            at_id = at_comp.get("id")
            at_name = at_comp.get("companyName")
            if not at_name:
                continue
                
            console.print(f"[{i}/{total_at}] Matching '{at_name}' (AT ID: {at_id})...")
            # Use double-quotes for the name in ConnectWise filters to handle single quotes correctly.
            # We escape double quotes by doubling them.
            safe_name = at_name.replace('"', '""')
            
            # ConnectWise list now handles paging internally
            cw_comps = CWCompanies.list(filters=f'name="{safe_name}"')
            
            if not cw_comps:
                console.print(f"[yellow]  - No match found in ConnectWise.[/yellow]")
                continue
                
            for cw_comp in cw_comps:
                cw_id = cw_comp.get("id")
                cw_name = cw_comp.get("name")
                
                # Check for billing contact in company object
                billing_contact_info = cw_comp.get("billingContact")
                invoice_email = cw_comp.get("invoiceToEmailAddress")
                
                bc_id = "N/A"
                bc_name = "N/A"
                bc_email = invoice_email or "N/A"
                
                if billing_contact_info:
                    bc_id = billing_contact_info.get("id")
                    bc_name = billing_contact_info.get("name")
                    
                    # Fetch contact to get their actual email if invoice_email is missing
                    if not invoice_email or invoice_email == "N/A":
                        try:
                            contact = CWContacts.get(bc_id)
                            if contact:
                                comms = contact.get("communicationItems", [])
                                for item in comms:
                                    if item.get("communicationType") == "Email" and item.get("defaultFlag"):
                                        bc_email = item.get("value")
                                        break
                        except:
                            pass
                
                console.print(f"[green]  - Match: {cw_name} (CW ID: {cw_id})[/green]")
                
                results.append({
                    "AT Company ID": at_id,
                    "AT Company Name": at_name,
                    "CW Company ID": cw_id,
                    "CW Company Name": cw_name,
                    "CW Billing Contact ID": bc_id,
                    "CW Billing Contact Name": bc_name,
                    "CW Billing Contact Email": bc_email
                })
        
        if results:
            console.print(f"\n[bold]Found {len(results)} matches.[/bold]")
            
            # Export to CSV
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            filename = f"connectwise-{timestamp}.csv"
            
            try:
                with open(filename, 'w', newline='') as f:
                    if results:
                        writer = csv.DictWriter(f, fieldnames=results[0].keys())
                        writer.writeheader()
                        writer.writerows(results)
                console.print(f"\n[green]Successfully exported data to {filename}[/green]")
            except Exception as export_err:
                console.print(f"[red]Error exporting to CSV: {export_err}[/red]")
        else:
            console.print("\n[yellow]No matches found to export.[/yellow]")
            
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")



def handle_custom_script2():
    import csv
    import os
    from autotask_cli.entities.registry import Companies as ATCompanies, Contacts as ATContacts
    
    filename = "importsheet.csv"
    if not os.path.exists(filename):
        console.print(f"[red]File {filename} not found.[/red]")
        return
        
    console.print(f"[bold]Reading {filename}...[/bold]")
    
    rows = []
    try:
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            # Normalize column names by stripping whitespace
            reader.fieldnames = [name.strip() for name in reader.fieldnames]
            for row in reader:
                # Strip whitespace from values
                clean_row = {k.strip(): v.strip() for k, v in row.items()}
                rows.append(clean_row)
    except Exception as e:
        console.print(f"[red]Error reading CSV: {e}[/red]")
        return
        
    # Filter rows where CW Billing Contact ID is 'N/A'
    filtered_rows = [r for r in rows if r.get("CW Billing Contact ID") == "N/A"]
    total = len(filtered_rows)
    
    if total == 0:
        console.print("[yellow]No rows found with 'CW Billing Contact ID' as 'N/A'.[/yellow]")
        return
        
    console.print(f"[green]Found {total} rows to process (where CW Billing Contact ID is 'N/A').[/green]")
    
    if not questionary.confirm(f"Proceed to create {total} contacts in Autotask and set them as billing contacts?").ask():
        console.print("[yellow]Cancelled.[/yellow]")
        return
        
    success_count = 0
    for i, row in enumerate(filtered_rows, 1):
        at_comp_id = row.get("AT Company ID")
        at_comp_name = row.get("AT Company Name")
        
        if not at_comp_id or not at_comp_name:
            console.print(f"[{i}/{total}] [yellow]Missing AT Company ID or Name in row. Skipping.[/yellow]")
            continue
            
        console.print(f"[{i}/{total}] Processing {at_comp_name} (AT ID: {at_comp_id})...")
        
        try:
            # 1. Create the contact
            contact_data = {
                "companyID": int(at_comp_id),
                "firstName": at_comp_name,
                "lastName": "Saikiran",
                "emailAddress": "saikirans@5gn.com.au",
                "mobilePhone": "0499999999",
                "isActive": 1,
                "billingContact":1
            }
            
            contact_result = ATContacts.create(contact_data)
            new_contact_id = contact_result.get("itemId")
            
            if not new_contact_id:
                console.print(f"  [red]- Failed to create contact (no ID returned).[/red]")
                continue
                
            console.print(f"  [green]- Created contact (ID: {new_contact_id}).[/green]")
            
            # 2. Update the company to set the billing contact
            # Autotask Company object uses 'billToContactID' for the billing contact
            # company_update_data = {
            #     "billToContactID": new_contact_id
            # }
            
            # ATCompanies.update(at_comp_id, company_update_data)
            # console.print(f"  [green]- Updated company {at_comp_id} billing contact to {new_contact_id}.[/green]")
            
            success_count += 1
            
        except Exception as e:
            console.print(f"  [red]- Error: {e}[/red]")
            
    console.print(f"\n[bold][green]Completed! Successfully processed {success_count} / {total} records.[/green][/bold]")


def handle_custom_script3():
    """CW -> AT: Find CW billing contacts, match or create in Autotask, set as primary billing contact."""
    import csv
    from datetime import datetime
    from autotask_cli.entities.registry import Companies as ATCompanies, Contacts as ATContacts

    limit_str = questionary.text("How many Autotask companies to process? (Leave empty for ALL):").ask()
    limit = None
    if limit_str:
        try:
            limit = int(limit_str)
        except:
            limit = None

    if limit is None:
        console.print("[yellow]Fetching ALL companies from Autotask. This may take a while...[/yellow]")
    else:
        console.print(f"[bold]Fetching first {limit} companies from Autotask...[/bold]")

    try:
        at_companies = ATCompanies.list(limit=limit)
        total_at = len(at_companies)
        console.print(f"[green]Found {total_at} Autotask companies.[/green]")

        results = []
        skipped = 0
        for i, at_comp in enumerate(at_companies, 1):
            at_id = at_comp.get("id")
            at_name = at_comp.get("companyName")
            if not at_name:
                continue

            console.print(f"\n[{i}/{total_at}] Processing '{at_name}' (AT ID: {at_id})...")

            # ----- Step 1: Find matching company in ConnectWise -----
            safe_name = at_name.replace('"', '""')
            cw_comps = CWCompanies.list(filters=f'name="{safe_name}"')

            if not cw_comps:
                console.print(f"  [yellow]- No matching company in ConnectWise. Skipping.[/yellow]")
                skipped += 1
                continue

            cw_comp = cw_comps[0]  # Take the first match
            cw_id = cw_comp.get("id")
            cw_name = cw_comp.get("name")
            console.print(f"  [cyan]- CW match: {cw_name} (CW ID: {cw_id})[/cyan]")

            # ----- Step 2: Get CW billing contact details -----
            billing_contact_info = cw_comp.get("billingContact")
            invoice_email = cw_comp.get("invoiceToEmailAddress")

            if not billing_contact_info:
                console.print(f"  [yellow]- No billing contact set in ConnectWise. Skipping.[/yellow]")
                skipped += 1
                continue

            bc_cw_id = billing_contact_info.get("id")
            bc_cw_name = billing_contact_info.get("name", "")

            # Parse name into first/last
            name_parts = bc_cw_name.split(" ", 1) if bc_cw_name else []
            cw_first = name_parts[0] if len(name_parts) >= 1 else "Billing"
            cw_last = name_parts[1] if len(name_parts) >= 2 else "Contact"

            # Get email from the CW contact record
            cw_email = invoice_email or ""
            if not cw_email and bc_cw_id:
                try:
                    cw_contact_detail = CWContacts.get(bc_cw_id)
                    if cw_contact_detail:
                        comms = cw_contact_detail.get("communicationItems", [])
                        for item in comms:
                            if item.get("communicationType") == "Email" and item.get("defaultFlag"):
                                cw_email = item.get("value", "")
                                break
                except:
                    pass

            console.print(f"  [cyan]- CW billing contact: {cw_first} {cw_last} ({cw_email or 'no email'})[/cyan]")

            # ----- Step 3: Search for matching contact in Autotask -----
            at_contact_id = None
            at_contact = None
            action_taken = "Skipped"

            try:
                # Search by companyID first
                at_contacts = ATContacts.list(filters=[
                    {"op": "eq", "field": "companyID", "value": at_id}
                ])

                if at_contacts:
                    # Try to match by email first (most reliable)
                    if cw_email:
                        for c in at_contacts:
                            if c.get("emailAddress", "").lower().strip() == cw_email.lower().strip():
                                at_contact = c
                                break

                    # Fallback: match by name
                    if not at_contact:
                        for c in at_contacts:
                            c_first = (c.get("firstName") or "").lower().strip()
                            c_last = (c.get("lastName") or "").lower().strip()
                            if c_first == cw_first.lower().strip() and c_last == cw_last.lower().strip():
                                at_contact = c
                                break

            except Exception as e:
                console.print(f"  [red]- Error searching AT contacts: {e}[/red]")
                continue

            # ----- Step 4: Update existing or create new AT contact -----
            try:
                if at_contact:
                    # Found an existing contact — update it to be billing contact
                    at_contact_id = int(at_contact.get("id"))
                    console.print(f"  [green]- Found existing AT contact: {at_contact.get('firstName')} {at_contact.get('lastName')} (ID: {at_contact_id})[/green]")

                    # Include companyID so the API can resolve the contact
                    # primaryContact = Main Billing Contact on the Company page
                    update_data = {
                        "companyID": int(at_id),
                        "firstName": at_contact.get("firstName", cw_first),
                        "lastName": at_contact.get("lastName", cw_last),
                        "isActive": int(at_contact.get("isActive", 1)),
                        "billingContact": True,
                        "primaryContact": True,
                    }
                    if cw_email and not at_contact.get("emailAddress"):
                        update_data["emailAddress"] = cw_email

                    ATContacts.update(at_contact_id, update_data)
                    console.print(f"  [green]- Updated contact {at_contact_id}.[/green]")
                    action_taken = "Updated"
                else:
                    # No matching contact — create a new one
                    console.print(f"  [yellow]- No matching contact in Autotask. Creating new one...[/yellow]")
                    new_contact_data = {
                        "companyID": int(at_id),
                        "firstName": cw_first,
                        "lastName": cw_last,
                        "isActive": 1,
                        "billingContact": True,
                        "primaryContact": True,
                    }
                    if cw_email:
                        new_contact_data["emailAddress"] = cw_email

                    create_result = ATContacts.create(new_contact_data)
                    at_contact_id = create_result.get("itemId")

                    if not at_contact_id:
                        console.print(f"  [red]- Failed to create contact (no ID returned).[/red]")
                        continue

                    console.print(f"  [green]- Created new contact (ID: {at_contact_id}).[/green]")
                    action_taken = "Created"

            except Exception as e:
                console.print(f"  [red]- Error updating/creating AT contact: {e}[/red]")
                continue



            results.append({
                "AT Company ID": at_id,
                "AT Company Name": at_name,
                "CW Company ID": cw_id,
                "CW Company Name": cw_name,
                "Action": action_taken,
                "AT Contact ID": at_contact_id,
                "Contact Name": f"{cw_first} {cw_last}",
                "Contact Email": cw_email or "N/A"
            })

        # ----- Summary & CSV export -----
        console.print(f"\n{'='*60}")
        console.print(f"[bold]SUMMARY[/bold]")
        console.print(f"  Total AT companies processed: {total_at}")
        console.print(f"  Matched & synced:             {len(results)}")
        console.print(f"  Skipped (no CW match/contact):{skipped}")
        console.print(f"{'='*60}")

        if results:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            filename = f"cw-at-billing-sync-{timestamp}.csv"

            try:
                with open(filename, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=results[0].keys())
                    writer.writeheader()
                    writer.writerows(results)
                console.print(f"\n[green]Results exported to {filename}[/green]")
            except Exception as export_err:
                console.print(f"[red]Error exporting CSV: {export_err}[/red]")
        else:
            console.print("\n[yellow]No records to export.[/yellow]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")


def handle_custom_script4():
    """CW -> AT: Find CW default (primary) contacts, match or create in Autotask, set as primaryContact."""
    import csv
    from datetime import datetime
    from autotask_cli.entities.registry import Companies as ATCompanies, Contacts as ATContacts

    limit_str = questionary.text("How many Autotask companies to process? (Leave empty for ALL):").ask()
    limit = None
    if limit_str:
        try:
            limit = int(limit_str)
        except:
            limit = None

    if limit is None:
        console.print("[yellow]Fetching ALL companies from Autotask. This may take a while...[/yellow]")
    else:
        console.print(f"[bold]Fetching first {limit} companies from Autotask...[/bold]")

    try:
        at_companies = ATCompanies.list(limit=limit)
        total_at = len(at_companies)
        console.print(f"[green]Found {total_at} Autotask companies.[/green]")

        results = []
        skipped = 0
        for i, at_comp in enumerate(at_companies, 1):
            at_id = at_comp.get("id")
            at_name = at_comp.get("companyName")
            if not at_name:
                continue

            console.print(f"\n[{i}/{total_at}] Processing '{at_name}' (AT ID: {at_id})...")

            # ----- Step 1: Find matching company in ConnectWise -----
            safe_name = at_name.replace('"', '""')
            cw_comps = CWCompanies.list(filters=f'name="{safe_name}"')

            if not cw_comps:
                console.print(f"  [yellow]- No matching company in ConnectWise. Skipping.[/yellow]")
                skipped += 1
                continue

            cw_comp = cw_comps[0]
            cw_id = cw_comp.get("id")
            cw_name = cw_comp.get("name")
            console.print(f"  [cyan]- CW match: {cw_name} (CW ID: {cw_id})[/cyan]")

            # ----- Step 2: Get CW default (primary) contact details -----
            default_contact_info = cw_comp.get("defaultContact")

            if not default_contact_info:
                console.print(f"  [yellow]- No default contact set in ConnectWise. Skipping.[/yellow]")
                skipped += 1
                continue

            dc_cw_id = default_contact_info.get("id")
            dc_cw_name = default_contact_info.get("name", "")

            # Parse name into first/last
            name_parts = dc_cw_name.split(" ", 1) if dc_cw_name else []
            cw_first = name_parts[0] if len(name_parts) >= 1 else "Primary"
            cw_last = name_parts[1] if len(name_parts) >= 2 else "Contact"

            # Get email from the CW contact record
            cw_email = ""
            if dc_cw_id:
                try:
                    cw_contact_detail = CWContacts.get(dc_cw_id)
                    if cw_contact_detail:
                        comms = cw_contact_detail.get("communicationItems", [])
                        for item in comms:
                            if item.get("communicationType") == "Email" and item.get("defaultFlag"):
                                cw_email = item.get("value", "")
                                break
                except:
                    pass

            console.print(f"  [cyan]- CW primary contact: {cw_first} {cw_last} ({cw_email or 'no email'})[/cyan]")

            # ----- Step 3: Search for matching contact in Autotask -----
            at_contact_id = None
            at_contact = None
            action_taken = "Skipped"

            try:
                at_contacts = ATContacts.list(filters=[
                    {"op": "eq", "field": "companyID", "value": at_id}
                ])

                if at_contacts:
                    # Try to match by email first (most reliable)
                    if cw_email:
                        for c in at_contacts:
                            if c.get("emailAddress", "").lower().strip() == cw_email.lower().strip():
                                at_contact = c
                                break

                    # Fallback: match by name
                    if not at_contact:
                        for c in at_contacts:
                            c_first = (c.get("firstName") or "").lower().strip()
                            c_last = (c.get("lastName") or "").lower().strip()
                            if c_first == cw_first.lower().strip() and c_last == cw_last.lower().strip():
                                at_contact = c
                                break

            except Exception as e:
                console.print(f"  [red]- Error searching AT contacts: {e}[/red]")
                continue

            # ----- Step 4: Update existing or create new AT contact -----
            try:
                if at_contact:
                    at_contact_id = int(at_contact.get("id"))
                    console.print(f"  [green]- Found existing AT contact: {at_contact.get('firstName')} {at_contact.get('lastName')} (ID: {at_contact_id})[/green]")

                    update_data = {
                        "companyID": int(at_id),
                        "firstName": at_contact.get("firstName", cw_first),
                        "lastName": at_contact.get("lastName", cw_last),
                        "isActive": int(at_contact.get("isActive", 1)),
                        "primaryContact": True,
                    }
                    if cw_email and not at_contact.get("emailAddress"):
                        update_data["emailAddress"] = cw_email

                    ATContacts.update(at_contact_id, update_data)
                    console.print(f"  [green]- Set contact {at_contact_id} as Primary Contact.[/green]")
                    action_taken = "Updated"
                else:
                    console.print(f"  [yellow]- No matching contact in Autotask. Creating new one...[/yellow]")
                    new_contact_data = {
                        "companyID": int(at_id),
                        "firstName": cw_first,
                        "lastName": cw_last,
                        "isActive": 1,
                        "primaryContact": True,
                    }
                    if cw_email:
                        new_contact_data["emailAddress"] = cw_email

                    create_result = ATContacts.create(new_contact_data)
                    at_contact_id = create_result.get("itemId")

                    if not at_contact_id:
                        console.print(f"  [red]- Failed to create contact (no ID returned).[/red]")
                        continue

                    console.print(f"  [green]- Created new Primary Contact (ID: {at_contact_id}).[/green]")
                    action_taken = "Created"

            except Exception as e:
                console.print(f"  [red]- Error updating/creating AT contact: {e}[/red]")
                continue

            results.append({
                "AT Company ID": at_id,
                "AT Company Name": at_name,
                "CW Company ID": cw_id,
                "CW Company Name": cw_name,
                "Action": action_taken,
                "AT Contact ID": at_contact_id,
                "Contact Name": f"{cw_first} {cw_last}",
                "Contact Email": cw_email or "N/A"
            })

        # ----- Summary & CSV export -----
        console.print(f"\n{'='*60}")
        console.print(f"[bold]SUMMARY[/bold]")
        console.print(f"  Total AT companies processed: {total_at}")
        console.print(f"  Matched & synced:             {len(results)}")
        console.print(f"  Skipped (no CW match/contact):{skipped}")
        console.print(f"{'='*60}")

        if results:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            filename = f"cw-at-primary-sync-{timestamp}.csv"

            try:
                with open(filename, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=results[0].keys())
                    writer.writeheader()
                    writer.writerows(results)
                console.print(f"\n[green]Results exported to {filename}[/green]")
            except Exception as export_err:
                console.print(f"[red]Error exporting CSV: {export_err}[/red]")
        else:
            console.print("\n[yellow]No records to export.[/yellow]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")


def handle_custom_script5():
    """Export ConnectWise service board ticket properties (form fields & dropdown options)."""
    import csv
    import json
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    # Board-level sub-resources to fetch per board
    BOARD_PROPERTIES = [
        ("Types",       "service/boards/{board_id}/types",       "name",  "inactiveFlag"),
        ("Sub-Types",   "service/boards/{board_id}/subtypes",    "name",  "inactiveFlag"),
        ("Items",       "service/boards/{board_id}/items",       "name",  "inactiveFlag"),
        ("Statuses",    "service/boards/{board_id}/statuses",    "name",  "closedStatus"),
        ("Teams",       "service/boards/{board_id}/teams",       "name",  None),
        ("Type/SubType/Item Associations", "service/boards/{board_id}/typeSubTypeItemAssociations", "type/name", None),
    ]

    # Global properties shared across all boards
    GLOBAL_PROPERTIES = [
        ("Priorities",         Priorities),
        ("Sources",            ServiceSources),
        ("Impacts",            Impacts),
        ("Severities",         Severities),
        ("Service Locations",  ServiceLocations),
        ("SLAs",               SLAs),
    ]

    def fetch_paged(endpoint):
        """Fetch all records from an endpoint with pagination."""
        all_items = []
        page = 1
        while True:
            params = {"pageSize": 1000, "page": page}
            try:
                data = cw_client.request("GET", endpoint, params=params)
            except Exception:
                break
            if not data or not isinstance(data, list):
                break
            all_items.extend(data)
            if len(data) < 1000:
                break
            page += 1
        return all_items

    # ===== Step 1: Fetch all service boards =====
    console.print("[bold cyan]Fetching all Service Boards...[/bold cyan]")
    try:
        boards = ServiceBoards.list()
    except Exception as e:
        console.print(f"[red]Error fetching boards: {e}[/red]")
        return

    if not boards:
        console.print("[yellow]No service boards found.[/yellow]")
        return

    active_boards = [b for b in boards if not b.get("inactiveFlag", False)]
    console.print(f"[green]Found {len(boards)} boards ({len(active_boards)} active).[/green]")

    # ===== Step 2: Fetch properties per board =====
    structured_data = {"boards": [], "global_properties": {}}
    csv_rows = []

    for idx, board in enumerate(active_boards, 1):
        board_id = board.get("id")
        board_name = board.get("name", "Unknown")
        console.print(f"\n[bold][{idx}/{len(active_boards)}] Board: {board_name} (ID: {board_id})[/bold]")

        board_data = {"id": board_id, "name": board_name, "properties": {}}

        for prop_label, endpoint_tpl, name_field, flag_field in BOARD_PROPERTIES:
            endpoint = endpoint_tpl.format(board_id=board_id)
            try:
                items = fetch_paged(endpoint)
                console.print(f"  {prop_label}: {len(items)} options")

                board_data["properties"][prop_label] = items

                for item in items:
                    # Resolve nested name fields like "type/name"
                    option_name = item
                    for part in name_field.split("/"):
                        if isinstance(option_name, dict):
                            option_name = option_name.get(part, "N/A")
                        else:
                            option_name = "N/A"
                            break

                    active = "Yes"
                    if flag_field:
                        flag_val = item.get(flag_field, False)
                        if flag_field == "inactiveFlag":
                            active = "No" if flag_val else "Yes"
                        elif flag_field == "closedStatus":
                            active = "Closed" if flag_val else "Open"

                    csv_rows.append({
                        "Board": board_name,
                        "Board ID": board_id,
                        "Property": prop_label,
                        "Option Name": option_name,
                        "Option ID": item.get("id", "N/A"),
                        "Active/Status": active,
                    })

            except Exception as e:
                console.print(f"  [yellow]{prop_label}: Error - {e}[/yellow]")

        structured_data["boards"].append(board_data)

    # ===== Step 3: Fetch global properties =====
    console.print(f"\n[bold cyan]Fetching Global Properties...[/bold cyan]")
    for prop_label, entity_cls in GLOBAL_PROPERTIES:
        try:
            items = entity_cls.list()
            console.print(f"  {prop_label}: {len(items)} options")
            structured_data["global_properties"][prop_label] = items

            for item in items:
                csv_rows.append({
                    "Board": "(Global)",
                    "Board ID": "-",
                    "Property": prop_label,
                    "Option Name": item.get("name", "N/A"),
                    "Option ID": item.get("id", "N/A"),
                    "Active/Status": "No" if item.get("inactiveFlag", False) else "Yes",
                })
        except Exception as e:
            console.print(f"  [yellow]{prop_label}: Error - {e}[/yellow]")

    # ===== Step 4: Export JSON =====
    json_file = f"cw-board-properties-{timestamp}.json"
    try:
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(structured_data, f, indent=2, default=str)
        console.print(f"\n[green]JSON exported: {json_file}[/green]")
    except Exception as e:
        console.print(f"[red]Error writing JSON: {e}[/red]")

    # ===== Step 5: Export CSV =====
    csv_file = f"cw-board-properties-{timestamp}.csv"
    try:
        fieldnames = ["Board", "Board ID", "Property", "Option Name", "Option ID", "Active/Status"]
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(csv_rows)
        console.print(f"[green]CSV exported:  {csv_file}[/green]")
    except Exception as e:
        console.print(f"[red]Error writing CSV: {e}[/red]")

    # ===== Summary =====
    console.print(f"\n{'='*60}")
    console.print(f"[bold green]Done! Exported properties for {len(active_boards)} boards + global properties.[/bold green]")
    console.print(f"[bold]Total rows in CSV: {len(csv_rows)}[/bold]")
    console.print(f"{'='*60}")


if __name__ == "__main__":
    main_menu()
