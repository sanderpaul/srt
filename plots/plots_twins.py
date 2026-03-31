import settings
from diagram import *
from settings import *


@with_global_settings
@with_output_folder
def run():
    SETTINGS["DOWN"] = 1
    SETTINGS["LEFT"] = 12
    SETTINGS["RIGHT"] = 12
    SETTINGS["UP"] = 20
    SETTINGS["CORNER"] = 20
    SETTINGS["LEGEND_LOC"] = "upper left"
    SETTINGS["X_AXIS_LABEL"] = r"Space [z / c$\tau$]"
    SETTINGS["Y_AXIS_LABEL"] = r"Time [ct / c$\tau$]"

    plot = Diagram()
    first_world_line = WorldLine(
        Point(0, 0),
        beta=0.8,
        settings={
            "space": True,
            "time": True,
            "time_ticks": True,
            "space_ticks": True,
        },
    )

    second_world_line = WorldLine(
        Point(4, 5),
        beta=-0.8,
        settings={
            "space": True,
            "time": True,
            "time_ticks": True,
            "space_ticks": True,
        },
        color="C4",
    )

    plot.add_world_line(first_world_line)
    plot.add_world_line(second_world_line)

    exchange_with = Event(
        4,
        5,
        settings={"t_first": True, "z_first": True, "t_second": True, "z_second": True},
        world_line=first_world_line,
    )

    plot.add_event(exchange_with)
    plot.draw("twins_first")

    first = Difference(
        Point(0, 0), Point(4, 5), settings={"direct": True}, color="C0", linestyle="-"
    )
    second = Difference(
        Point(0, 10), Point(4, 5), settings={"direct": True}, color="C0", linestyle="-"
    )

    exchange_without = Event(4, 5, settings={}, world_line=first_world_line)
    final_without = Event(0, 10, settings={})

    plot = Diagram()
    plot.add_world_line(first_world_line)
    plot.add_world_line(second_world_line)
    plot.add_event(exchange_without)
    plot.add_event(final_without)
    plot.add_difference(first)
    plot.add_difference(second)
    plot.draw("twins_second")

    for i in range(9):
        plot.add_difference(
            Difference(
                Point(0, i + 1),
                Point((40 - 4 * (i + 1)) / 9, (40 + 5 * (i + 1)) / 9),
                settings={"direct": True},
                color="C2",
            )
        )
    plot.draw("twins_third")

    plot = Diagram()
    plot.add_world_line(first_world_line)
    plot.add_world_line(second_world_line)
    plot.add_event(exchange_without)
    plot.add_event(final_without)
    plot.add_difference(first)
    plot.add_difference(second)
    for i in range(3):
        local_z = (i + 1) * 4 / 3
        local_t = (i + 1) * 5 / 3

        plot.add_difference(
            Difference(
                Point(local_z, local_t),
                Point(0, local_t + local_z),
                settings={"direct": True},
                color="C2",
            )
        )

        plot.add_difference(
            Difference(
                Point(local_z, 10 - local_t),
                Point(0, 10 - local_t + local_z),
                settings={"direct": True},
                color="C2",
            )
        )
    plot.draw("twins_fourth")