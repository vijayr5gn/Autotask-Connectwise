from tabulate import tabulate
import json
from rich.console import Console
from rich.syntax import Syntax

console = Console()

def print_table(data, fields):
    if not data:
        console.print("[yellow]No records found.[/yellow]")
        return
    
    rows = []
    for item in data:
        row = []
        for f in fields:
            # Handle nested fields (e.g., 'company/id')
            if '/' in f:
                parts = f.split('/')
                val = item
                for part in parts:
                    if isinstance(val, dict):
                        val = val.get(part)
                    else:
                        val = None
                row.append(val)
            else:
                row.append(item.get(f))
        rows.append(row)
    
    headers = [f.replace("_", " ").replace("/", " ").title() for f in fields]
    print(tabulate(rows, headers=headers, tablefmt="pretty"))

def print_json(data):
    json_str = json.dumps(data, indent=2)
    syntax = Syntax(json_str, "json", theme="monokai", line_numbers=True)
    console.print(syntax)

def print_summary(item, fields):
    console.print("\n[bold]Record Summary:[/bold]")
    for f in fields:
        # Handle nested fields
        if '/' in f:
            parts = f.split('/')
            val = item
            for part in parts:
                if isinstance(val, dict):
                    val = val.get(part)
                else:
                    val = None
            console.print(f"  [bold]{f.title()}:[/bold] {val}")
        else:
            console.print(f"  [bold]{f.title()}:[/bold] {item.get(f)}")
    console.print("")
