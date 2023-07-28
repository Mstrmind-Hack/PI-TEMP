from resources import *
from rich import print
from rich.table import Table
from rich import box


active = True


def temperature(
    good_min_temp: int,
    good_max_temp: int,
    avg_min_temp: int,
    avg_max_temp: int,
):
    while active:
        subprocess.run(["clear"])
        box_title = "PI"

        deg = chr(176)  # Degree Simbol

        run = subprocess.Popen(
            ["cat", "/sys/class/thermal/thermal_zone0/temp"], stdout=subprocess.PIPE
        )
        output = run.stdout.read()
        number = str(output, "utf-8")
        number2 = int(number) / 1000

        if good_min_temp <= number2 <= good_max_temp:
            table = Table(
                title=f"\n[bold][orange_red1] {box_title} [/orange_red1][magenta2]CPU Temp.[/magenta2][/bold]",
                show_header=False,
                header_style="bold orange3",
                show_lines=False,
                min_width=20,
                expand=True,
                box=box.DOUBLE_EDGE,
                border_style="chartreuse1",
                title_justify="left",
            )
            table.add_row(
                f"[medium_spring_green]{number2}[/medium_spring_green] [magenta2]{deg}C[/magenta2]",
                style="bold",
            )
        elif avg_min_temp <= number2 <= avg_max_temp:
            table = Table(
                title=f"\n[bold][orange_red1] {box_title} [/orange_red1][magenta2]CPU Temp.[/magenta2][/bold]",
                show_header=False,
                header_style="bold orange3",
                show_lines=False,
                min_width=20,
                expand=True,
                box=box.DOUBLE_EDGE,
                border_style="bright_yellow",
                title_justify="left",
            )
            table.add_row(
                f"[medium_spring_green]{number2}[/medium_spring_green] [magenta2]{deg}C[/magenta2]",
                style="bold medium_spring_green",
            )
        else:
            table = Table(
                title=f"\n[bold][orange_red1] {box_title} [/orange_red1][magenta2]CPU Temp.[/magenta2][/bold]",
                show_header=False,
                header_style="bold orange3",
                show_lines=False,
                min_width=20,
                expand=True,
                box=box.DOUBLE_EDGE,
                border_style="red1",
                title_justify="left",
            )
            table.add_row(
                f"[orange_red1]{number2}[/orange_red1] [magenta2]{deg}C[/magenta2]",
                style="bold blink",
            )
        if table:
            print(table)
        time.sleep(0.5)
