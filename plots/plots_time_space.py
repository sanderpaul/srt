import settings
from diagram import *
from settings import *


@with_global_settings
@with_output_folder
def run():
    SETTINGS["LIGHT"] = True
    plot = Diagram()
    plot.draw("light")

    plot = Diagram()
    SETTINGS["TIME_LIKE"] = True
    plot.draw("light_with_time")

    plot = Diagram()
    SETTINGS["SPACE_LIKE"] = True
    plot.draw("light_with_both")

    plot = Diagram()
    SETTINGS["TIME_LIKE"] = False
    plot.draw("light_with_space")

    SETTINGS["SPACE_LIKE"] = False

    plot = Diagram()
    plot.add_event(Event(1, 2, settings={}))
    plot.add_event(Event(3, 1, settings={}))
    plot.draw("two_points_no_lines")

    plot = Diagram()
    plot.add_event(Event(1, 2, settings={"future": True}))
    plot.add_event(Event(3, 1, settings={"future": True}))
    plot.draw("two_points_future")

    plot = Diagram()
    plot.add_event(Event(1, 2, settings={"past": True}))
    plot.add_event(Event(3, 1, settings={"past": True}))
    plot.draw("two_points_past")

    plot = Diagram()
    plot.add_event(Event(1, 2, settings={"future": True, "past": True}))
    plot.add_event(Event(3, 1, settings={"future": True, "past": True}))
    plot.draw("two_points_future_past")

    plot = Diagram()
    plot.add_event(Event(1, 2, settings={"independent": True}))
    plot.add_event(Event(3, 1, settings={"independent": True}))
    plot.draw("two_points_independent")

    plot = Diagram()
    plot.add_event(
        Event(
            1,
            2,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
            },
        )
    )
    plot.add_event(
        Event(
            3,
            1,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
            },
        )
    )
    plot.draw("two_points_default_frame")

    wl = WorldLine(
        origin=Point(0.0, 0.0),
        beta=-0.5,
        settings={"time": True, "time_ticks": True, "space": True, "space_ticks": True},
    )

    plot = Diagram()
    plot.add_world_line(wl)
    plot.add_event(
        Event(
            1,
            2,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
            },
            world_line=wl,
        )
    )
    plot.add_event(
        Event(
            3,
            1,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
            },
            world_line=wl,
        )
    )
    plot.draw("two_points_same_time")

    wl = WorldLine(
        origin=Point(0.0, 0.0),
        beta=-0.6,
        settings={"time": True, "time_ticks": True, "space": True, "space_ticks": True},
    )

    plot = Diagram()
    plot.add_world_line(wl)
    plot.add_event(
        Event(
            1,
            2,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
            },
            world_line=wl,
        )
    )
    plot.add_event(
        Event(
            3,
            1,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
            },
            world_line=wl,
        )
    )
    plot.draw("two_points_inverted")

    plot = Diagram()
    plot.add_event(Event(1, 3, settings={}))
    plot.add_event(Event(2, 1, settings={}))
    plot.draw("two_points_causality")

    plot = Diagram()
    plot.add_event(Event(1, 3, settings={"future": True}))
    plot.add_event(Event(2, 1, settings={"future": True}))
    plot.draw("two_points_causality_future")

    plot = Diagram()
    plot.add_event(Event(1, 3, settings={"past": True}))
    plot.add_event(Event(2, 1, settings={"past": True}))
    plot.draw("two_points_causality_past")

    plot = Diagram()
    plot.add_event(Event(1, 3, settings={"future": True, "past": True}))
    plot.add_event(Event(2, 1, settings={"future": True, "past": True}))
    plot.draw("two_points_causality_future_past")

    plot = Diagram()
    plot.add_event(Event(1, 3, settings={"independent": True}))
    plot.add_event(Event(2, 1, settings={"independent": True}))
    plot.draw("two_points_causality_independent")

    plot = Diagram()
    plot.add_event(
        Event(
            1,
            3,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
            },
        )
    )
    plot.add_event(
        Event(
            2,
            1,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
            },
        )
    )
    plot.draw("two_points_causality_default_frame")

    wl = WorldLine(
        origin=Point(0.0, 0.0),
        beta=-0.6,
        settings={"time": True, "time_ticks": True, "space": True, "space_ticks": True},
    )

    plot = Diagram()
    plot.add_world_line(wl)
    plot.add_event(
        Event(
            1,
            3,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
            },
            world_line=wl,
        )
    )
    plot.add_event(
        Event(
            2,
            1,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
            },
            world_line=wl,
        )
    )
    plot.draw("two_points_causality_inverted")

    wl = WorldLine(
        origin=Point(0.0, 0.0),
        beta=0.6,
        settings={"time": True, "time_ticks": True, "space": True, "space_ticks": True},
    )

    plot = Diagram()
    plot.add_world_line(wl)
    plot.add_event(
        Event(
            1,
            3,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
            },
            world_line=wl,
        )
    )
    plot.add_event(
        Event(
            2,
            1,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
            },
            world_line=wl,
        )
    )
    plot.draw("two_points_causality_forward")