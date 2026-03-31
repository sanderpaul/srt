import settings
from diagram import *
from settings import *


@with_global_settings
def run():
    SETTINGS["DOWN"] = 1
    SETTINGS["LEFT"] = 1
    SETTINGS["RIGHT"] = 40
    SETTINGS["UP"] = 40
    SETTINGS["CORNER"] = 40

    SETTINGS["LEGEND_LOC"] = "lower right"

    SETTINGS["X_AXIS_LABEL"] = r"Space [z / c$\tau$]"
    SETTINGS["Y_AXIS_LABEL"] = r"Time [ct / c$\tau$]"

    plot = Diagram()
    plot.draw("muon_first")

    world_line = WorldLine(
        Point(0, 0),
        beta=0.99,
        settings={
            "space": True,
            "time": True,
            "time_ticks": True,
            "space_ticks": True,
        },
    )

    plot.add_world_line(world_line)
    plot.draw("muon_second")

    plot.add_event(
        Event(
            32.355,
            32.68,
            settings={
                "use_world_line_as_default": True,
            },
            world_line=world_line,
        )
    )
    plot.draw("muon_third")

    plot = Diagram()
    plot.add_world_line(world_line)
    plot.add_event(
        Event(
            32.35,
            32.68,
            settings={
                "t_first": True,
                "z_first": True,
                "t_second": True,
                "z_second": True,
            },
            world_line=world_line,
        )
    )
    plot.draw("muon_fourth")
    plot.add_event(
        Event(
            32.35,
            32.027,
            settings={
                "t_first": True,
                "z_first": True,
                "t_second": True,
                "z_second": True,
            },
            world_line=world_line,
        )
    )
    plot.draw("muon_fifth")