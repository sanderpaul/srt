import settings
from diagram import *
from settings import *


@with_global_settings
def run():
    SETTINGS["DOWN"] = 1
    SETTINGS["LEFT"] = 1
    SETTINGS["RIGHT"] = 5
    SETTINGS["UP"] = 11
    SETTINGS["CORNER"] = 5
    SETTINGS["LEGEND_LOC"] = "lower right"

    beta = 0.6
    t_emit = 2.0

    t_bounce = t_emit / (1 - beta)
    z_bounce = beta * t_bounce
    t_receive = t_bounce + z_bounce  # = t_emit * (1 + beta) / (1 - beta)

    world_line = WorldLine(
        Point(0, 0),
        beta=beta,
        settings={
            "space": True,
            "time": True,
            "time_ticks": True,
            "space_ticks": True,
        },
    )

    emit = Event(0, t_emit, settings={})
    bounce = Event(z_bounce, t_bounce, settings={}, world_line=world_line)
    receive = Event(0, t_receive, settings={})

    signal_out = Difference(emit.to_point(), bounce.to_point(), settings={"direct": True})
    signal_return = Difference(bounce.to_point(), receive.to_point(), settings={"direct": True})

    plot = Diagram()
    plot.add_world_line(world_line)
    plot.draw("doppler_echo_first")

    plot.add_event(emit)
    plot.draw("doppler_echo_second")

    plot.add_difference(signal_out)
    plot.add_event(bounce)
    plot.draw("doppler_echo_third")

    plot.add_difference(signal_return)
    plot.add_event(receive)
    plot.draw("doppler_echo_fourth")

    delta_t = 0.5

    t_emit_2 = t_emit + delta_t
    t_bounce_2 = t_emit_2 / (1 - beta)
    z_bounce_2 = beta * t_bounce_2
    t_receive_2 = t_bounce_2 + z_bounce_2

    emit_2 = Event(0, t_emit_2, settings={})
    bounce_2 = Event(z_bounce_2, t_bounce_2, settings={}, world_line=world_line)
    receive_2 = Event(0, t_receive_2, settings={})

    signal_out_2 = Difference(emit_2.to_point(), bounce_2.to_point(), settings={"direct": True})
    signal_return_2 = Difference(bounce_2.to_point(), receive_2.to_point(), settings={"direct": True})

    plot.add_event(emit_2)
    plot.draw("doppler_echo_fifth")

    plot.add_difference(signal_out_2)
    plot.add_event(bounce_2)
    plot.draw("doppler_echo_sixth")

    plot.add_difference(signal_return_2)
    plot.add_event(receive_2)
    plot.draw("doppler_echo_seventh")