from resources import *
from simple_term_menu import TerminalMenu
from pathlib import Path
import os
from rich import print


def menu_temp():
    """
    Main Menu, Select from all four options
    """

    menu_temp.options = [
        "Config Temperature",
        "Use Default Temperatures",
    ]

    terminal_menu = TerminalMenu(
        menu_temp.options,
        title="",
        menu_cursor=" >> ",
        menu_cursor_style=("fg_red", "bold"),
        menu_highlight_style=("fg_yellow", "underline", "italics", "bold"),
    )
    menu_temp.menu_entry_index = terminal_menu.show()

    if menu_temp.options[menu_temp.menu_entry_index] == "Use Default Temperatures":
        from modules.cpu_temp_monitor import temperature

        good_min_temp = 0
        good_max_temp = 45
        avg_min_temp = 46
        avg_max_temp = 60

        temperature(good_min_temp, good_max_temp, avg_min_temp, avg_max_temp)

    if menu_temp.options[menu_temp.menu_entry_index] == "Config Temperature":
        from modules.cpu_temp_monitor import temperature

        try:
            deg = chr(176)
            the_path = os.getcwd()
            the_path2 = f"{the_path}/modules/values.txt"

            file = open(f"{the_path2}", "r")
            print(
                "\n [bold][medium_spring_green]Previous Temperature conf.[/medium_spring_green][/bold]"
            )
            print(file.read())
            file.close()

            file = open(f"{the_path2}", "w")

            print(
                "\n[bold][green3] Enter 'Good' Min Temp:[/green3][/bold]",
                end="",
            )

            good_min_temp = int(input(" >> "))

            print(
                "[bold][green3] Enter 'Good' Max Temp:[/green3][/bold]",
                end="",
            )
            good_max_temp = int(input(" >> "))
            print(
                "[bold][yellow2] Enter 'Average' Min Temp:[/yellow2][/bold]",
                end="",
            )
            avg_min_temp = int(input(" >> "))
            print(
                "[bold][yellow2] Enter 'Average' Max Temp:[/yellow2][/bold]",
                end="",
            )
            avg_max_temp = int(input(" >> "))
            gmt = f"[bold][pale_turquoise1]Good Min Temp: [turquoise2]{good_min_temp}[/turquoise2]{deg}C[/pale_turquoise1][/bold]"
            gMt = f"[bold][pale_turquoise1]Good Max Temp: [turquoise2]{good_max_temp}[/turquoise2]{deg}C[/pale_turquoise1][/bold]"
            amt = f"[bold][pale_turquoise1]Average Min Temp: [turquoise2]{avg_min_temp}[/turquoise2]{deg}C[/pale_turquoise1][/bold]"
            aMt = f"[bold][pale_turquoise1]Average Max Temp: [turquoise2]{avg_max_temp}[/turquoise2]{deg}C[/pale_turquoise1][/bold]"
            temps = f"\n\t{gmt}\n\t{gMt}\n\t{amt}\n\t{aMt}"
            file.write(temps)
            file.close()

            temperature(good_min_temp, good_max_temp, avg_min_temp, avg_max_temp)
        except ValueError:
            print("\n [bold][red1]ERROR: Enter Numbers Only[/red1][/bold]")
            time.sleep(2)
            run_again()


menu_temp()
