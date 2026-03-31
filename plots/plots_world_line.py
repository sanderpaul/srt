import settings
from diagram import *
from settings import *


@with_global_settings
def run():
    # Sixth image: Introduction of worldlines
    plot = Diagram()
    plot.add_event(Event(0.0, 0, settings={}))
    plot.draw("worldline_first_point")

    plot.add_event(
        Event(
            0.6,
            1,
            settings={
                "t_first": True,
                "t_second": False,
                "z_first": True,
                "z_second": False,
            },
        )
    )
    plot.draw("worldline_second_point")

    plot.add_event(
        Event(
            1.2,
            2,
            settings={
                "t_first": True,
                "t_second": False,
                "z_first": True,
                "z_second": False,
            },
        )
    )
    plot.draw("worldline_third_point")

    plot.add_event(
        Event(
            1.8,
            3,
            settings={
                "t_first": True,
                "t_second": False,
                "z_first": True,
                "z_second": False,
            },
        )
    )
    plot.draw("worldline_fourth_point")

    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={"time": True}))
    plot.draw("worldline_introduce_line")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={"time": True}))
    plot.draw("worldline_time")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(Point(0, 0), beta=0.6, settings={"time": True, "time_angle": True})
    )
    plot.draw("worldline_time_angle")

    plot = Diagram()
    plot.add_event(Event(0.0, 0.0, settings={}))
    plot.add_event(Event(1.0, 0.0, settings={}))
    plot.add_event(Event(2.0, 0.0, settings={}))
    plot.add_event(Event(3.0, 0.0, settings={}))
    plot.draw("worldline_space_points")

    plot = Diagram()
    plot.add_event(Event(0.0, 0.0, settings={}))
    plot.add_event(
        Event(
            1.0,
            0.6,
            settings={
                "t_first": True,
                "t_second": False,
                "z_first": True,
                "z_second": False,
            },
        )
    )
    plot.add_event(
        Event(
            2.0,
            1.2,
            settings={
                "t_first": True,
                "t_second": False,
                "z_first": True,
                "z_second": False,
            },
        )
    )
    plot.add_event(
        Event(
            3.0,
            1.8,
            settings={
                "t_first": True,
                "t_second": False,
                "z_first": True,
                "z_second": False,
            },
        )
    )
    plot.draw("worldline_space_points_on_line")

    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={"space": True}))
    plot.draw("worldline_introduce_line_space")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(Point(0, 0), beta=0.6, settings={"space": True, "space_angle": True})
    )
    plot.draw("worldline_space_angle")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(Point(0, 0), beta=0.6, settings={"space": True, "time": True})
    )
    plot.draw("worldline_all")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "space_angle": True,
                "time_angle": True,
            },
        )
    )
    plot.draw("worldline_all_angle")

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
    plot.draw("worldline_all_angle_ticks")

    beta_values = [
        -0.99, -0.95, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, -0.0,
        0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99,
    ]

    for i, value in enumerate(beta_values):
        plot = Diagram()
        plot.add_world_line(
            WorldLine(Point(0, 0), beta=value, settings={"time": True, "space": True})
        )
        plot.draw(f"gif/beta_{i}")

    plot = Diagram()
    plot.add_event(Event(0.75, 1.25, settings={}))
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.6,
            settings={
                "space": True,
                "time": True,
                "time_ticks": False,
                "space_ticks": False,
            },
        )
    )
    plot.draw("worldline_one_point_on_line")

    plot = Diagram()
    plot.add_event(Event(0.75, 1.25, settings={}))
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
    plot.draw("worldline_one_point_on_scale")

    plot = Diagram()
    plot.add_event(Event(3, 3, settings={}))
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
    plot.draw("point_read_no_lines")

    plot = Diagram()
    plot.add_event(
        Event(
            3,
            3,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
            },
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
    plot.draw("point_read_basic_lines")

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
            3,
            3,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
                "use_world_line_as_default": True,
            },
            world_line=Line(Point(0, 0), beta=0.6),
        )
    )
    plot.draw("point_read_moving_lines")