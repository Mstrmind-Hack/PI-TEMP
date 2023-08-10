from resources import *

subprocess.run(["clear"])
pi_temp_banner()


try:
    """
    Imports the main menu with all its functions
    """

    from modules.menu import menu

except KeyboardInterrupt:
    print("\n")
    print("[bold][deep_pink1] Exiting...[/deep_pink1][/bold]")
    time.sleep(2)
    subprocess.run(["clear"])
