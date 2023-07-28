from resources import *
from simple_term_menu import TerminalMenu

from rich import print


try:

    def menu():
        """
        Main Menu, Select from all four options
        """
        print(
            f"\n[bold][orange_red1] --------- MAIN MENU --------- [/orange_red1][/bold]"
        )

        menu.options = [
            "Pi-CPU Temp Monitor",
        ]

        terminal_menu = TerminalMenu(
            menu.options,
            title="",
            menu_cursor=" >> ",
            menu_cursor_style=("fg_red", "bold"),
            menu_highlight_style=("fg_yellow", "underline", "italics", "bold"),
        )
        menu.menu_entry_index = terminal_menu.show()

        if menu.options[menu.menu_entry_index] == "Pi-CPU Temp Monitor":
            from modules.temp_values_menu import menu_temp

    menu()


except TypeError:
    print("\n")
    print("[bold][deep_pink1] Exiting...[/deep_pink1][/bold]")
    time.sleep(2)
    subprocess.run(["clear"])
