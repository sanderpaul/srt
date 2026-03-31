import settings
from diagram import *
from settings import *


@with_global_settings
def run():
    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(Event(1.5, 2.5, settings={}, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("dilatation_first_point")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(
        Event(
            1.5,
            2.5,
            settings={"t_first": True, "t_second": True},
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("dilatation_first_rest_frame")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(
        Event(
            1.5,
            2.5,
            settings={
                "t_first": True,
                "t_second": True,
                "use_world_line_as_default": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("dilatation_first_moving_frame")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(Event(0, 2, settings={}, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("dilatation_second_point")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(
        Event(
            0,
            2,
            settings={"t_first": True, "t_second": True},
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("dilatation_second_rest_frame")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(
        Event(
            0,
            2,
            settings={
                "t_first": True,
                "t_second": True,
                "use_world_line_as_default": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("dilatation_second_moving_frame")

    plot = Diagram()
    plot.add_event(
        Event(
            1.5,
            2.5,
            settings={
                "t_first": True,
                "t_second": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(
        Event(
            0.0,
            2.0,
            settings={
                "t_first": True,
                "t_second": True,
                "use_world_line_as_default": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("dilatation_both")

    plot = Diagram()
    plot.add_event(
        Event(
            1.5,
            2.5,
            settings={
                "t_first": True,
                "t_second": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(
        Event(
            0.0,
            2.0,
            settings={
                "t_first": True,
                "t_second": True,
                "use_world_line_as_default": True,
                "hyperbel": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("dilatation_both_hyperbel")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(Event(2.5, 1.5, settings={}, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("contraction_first_point")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(
        Event(
            2.5,
            1.5,
            settings={
                "z_first": True,
                "z_second": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("contraction_first_rest_frame")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(
        Event(
            2.5,
            1.5,
            settings={
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("contraction_first_moving_frame")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(Event(2, 0, settings={}, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("contraction_second_point")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(
        Event(
            2,
            0,
            settings={
                "z_first": True,
                "z_second": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("contraction_second_rest_frame")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(
        Event(
            2,
            0,
            settings={
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("contraction_second_moving_frame")

    plot = Diagram()
    plot.add_event(
        Event(
            2.5,
            1.5,
            settings={
                "z_first": True,
                "z_second": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(
        Event(
            2,
            0,
            settings={
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("contraction_both")

    plot = Diagram()
    plot.add_event(
        Event(
            2.5,
            1.5,
            settings={
                "z_first": True,
                "z_second": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": True,
                "space_ticks": True,
            },
        )
    )
    plot.add_event(
        Event(
            2,
            0,
            settings={
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
                "hyperbel": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("contraction_both_hyperbel")