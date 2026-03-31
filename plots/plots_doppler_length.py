import settings
from diagram import *
from settings import *


@with_global_settings
@with_output_folder
def run():
    SETTINGS["DOWN"] = 1
    SETTINGS["LEFT"] = 1
    SETTINGS["RIGHT"] = 6
    SETTINGS["UP"] = 13
    SETTINGS["CORNER"] = 5
    SETTINGS["LEGEND_LOC"] = "lower right"

    beta = 0.6
    t_emit = 2.0

    world_line_1 = WorldLine(
        Point(0, 0),
        beta=beta,
        settings={
            "space": True,
            "time": True,
            "time_ticks": True,
            "space_ticks": True,
        },
    )

    origin_2 = convert(Point(1, 0), Line(Point(0, 0), beta))
    world_line_2 = WorldLine(
        origin_2,
        beta=beta,
        settings={
            "space": True,
            "time": True,
            "time_ticks": True,
            "space_ticks": True,
        },
        color="C4",
    )

    # Lab separation between worldlines (Lorentz-contracted proper length 1)
    lab_sep = origin_2.z - beta * origin_2.t  # = 1/gamma

    # Outgoing signal: t = z + t_emit
    # Crosses wl_1 (z = beta*t):
    t_1 = t_emit / (1 - beta)
    z_1 = beta * t_1

    # Reflects off wl_2 (z = lab_sep + beta*t):
    t_2 = (lab_sep + t_emit) / (1 - beta)
    z_2 = lab_sep + beta * t_2

    t_receive_1 = t_1 + z_1
    t_receive_2 = t_2 + z_2

    emit = Event(0, t_emit, settings={})
    reflect_1 = Event(z_1, t_1, settings={}, world_line=world_line_1)
    reflect_2 = Event(z_2, t_2, settings={}, world_line=world_line_2)
    receive_1 = Event(0, t_receive_1, settings={})
    receive_2 = Event(0, t_receive_2, settings={})

    plot = Diagram()
    plot.add_world_line(world_line_1)
    plot.add_world_line(world_line_2)
    plot.draw("doppler_length_first")

    plot.add_event(emit)
    plot.draw("doppler_length_second")

    plot.add_difference(
        Difference(emit.to_point(), reflect_1.to_point(), settings={"direct": True})
    )
    plot.add_event(reflect_1)
    plot.draw("doppler_length_third")

    plot.add_difference(
        Difference(
            reflect_1.to_point(), reflect_2.to_point(), settings={"direct": True}
        )
    )
    plot.add_event(reflect_2)
    plot.draw("doppler_length_fourth")

    plot.add_difference(
        Difference(
            reflect_1.to_point(), receive_1.to_point(), settings={"direct": True}
        )
    )
    plot.add_difference(
        Difference(
            reflect_2.to_point(), receive_2.to_point(), settings={"direct": True}
        )
    )
    plot.add_event(receive_1)
    plot.add_event(receive_2)
    plot.draw("doppler_length_fifth")
