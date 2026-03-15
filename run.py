#!/usr/bin/env python3
import sys
import questionary

def run():
    choice = questionary.select(
        "Which system do you want to connect to?",
        choices=["Autotask", "ConnectWise", "Exit"]
    ).ask()

    if choice == "Autotask":
        from autotask_cli.main import main_menu
        main_menu()
    elif choice == "ConnectWise":
        from connectwise_cli.main import main_menu
        main_menu()
    else:
        sys.exit(0)

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Unexpected Error: {e}")
        sys.exit(1)
