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

        deg = chr(176)  # Degree Symbol

        run = subprocess.Popen(
            ["cat", "/sys/class/thermal/thermal_zone0/temp"], stdout=subprocess.PIPE
        )
        output = run.stdout.read()
        number = str(output, "utf-8")
        number2 = int(number) / 1000

        def table_border(border_color, number_color):
            table = Table(
                title=f"[bold][orange_red1] {box_title} [/orange_red1][magenta2]CPU Temp.[/magenta2][/bold]",
                show_header=False,
                header_style="bold orange3",
                show_lines=False,
                min_width=20,
                expand=True,
                box=box.DOUBLE_EDGE,
                border_style=f"{border_color}",
                title_justify="left",
            )

            if number_color != "orange_red1":
                table.add_row(
                    f"[{number_color}]{number2}[/{number_color}] [magenta2]{deg}C[/magenta2]",
                    style="bold",
                )
            else:
                table.add_row(
                    f"[{number_color}]{number2}[/{number_color}] [magenta2]{deg}C[/magenta2]",
                    style="bold blink",
                )
            if table:
                print(table)

        if good_min_temp <= number2 <= good_max_temp:
            table_border("chartreuse1", "medium_spring_green")

        elif avg_min_temp <= number2 <= avg_max_temp:
            table_border("bright_yellow", "medium_spring_green")

        else:
            table_border("red1", "orange_red1")

        time.sleep(0.5)
