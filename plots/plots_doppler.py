import settings
from diagram import *
from settings import *


@with_global_settings
@with_output_folder
def run():
    SETTINGS["DOWN"] = 1
    SETTINGS["LEFT"] = 1
    SETTINGS["RIGHT"] = 25
    SETTINGS["UP"] = 25
    SETTINGS["CORNER"] = 25
    SETTINGS["LEGEND_LOC"] = "lower right"

    world_line = WorldLine(
        Point(0, 0),
        beta=0.886,
        settings={
            "space": True,
            "time": True,
            "time_ticks": True,
            "space_ticks": True,
        },
    )

    plot = Diagram()
    plot.draw("doppler_first")

    plot.add_world_line(world_line)
    plot.draw("doppler_second")

    data_first = convert(Point(0, 1), world_line.to_line())
    data_second = convert(Point(0, 5), world_line.to_line())

    plot.add_event(
        Event(data_first.z, data_first.t, settings={}, world_line=world_line)
    )
    plot.add_event(
        Event(data_second.z, data_second.t, settings={}, world_line=world_line)
    )
    plot.draw("doppler_third")

    first = data_first.to_event(
        settings={
            "t_first": True,
            "z_first": True,
        },
        world_line=world_line,
    )

    second = data_second.to_event(
        settings={
            "t_first": True,
            "z_first": True,
        },
        world_line=world_line,
    )

    plot = Diagram()
    plot.add_world_line(world_line)
    plot.add_event(first)
    plot.add_event(second)
    plot.draw("doppler_fourth")

    first_arrival = Event(
        0,
        first.t + first.z,
        settings={},
        color=SETTINGS["DIFF_COLOR"],
        linestyle=SETTINGS["DIFF_LINE"],
    )
    second_arrival = Event(
        0,
        second.t + second.z,
        settings={},
        color=SETTINGS["DIFF_COLOR"],
        linestyle=SETTINGS["DIFF_LINE"],
    )

    plot.add_difference(
        Difference(
            first.to_point(), first_arrival.to_point(), settings={"direct": True}
        )
    )
    plot.add_difference(
        Difference(
            second.to_point(), second_arrival.to_point(), settings={"direct": True}
        )
    )
    plot.add_event(first_arrival)
    plot.add_event(second_arrival)
    plot.draw("doppler_fifth")