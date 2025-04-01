import settings
from diagram import *
from settings import *

intro = False  # plot basic plots
time_space = False  # plot time and space like vectors
world_line = False  # plot introduction of worldline
dil_con = False  # plot time dilation and Lorentz contraction
vel_add = True  # plot velocity addition plot.

if intro:
    SETTINGS["LIGHT"] = False
    plot = Diagram()
    plot.draw("empty")

    plot = Diagram()
    plot.add_event(Event(1, 2, settings={}))
    plot.draw("one_point_no_lines")

    plot = Diagram()
    plot.add_event(Event(1, 2, settings={
        "t_first": True,
        "t_second": False,
        "z_first": True,
        "z_second": False
    }))
    plot.draw("one_point_partial_lines")

    plot = Diagram()
    plot.add_event(Event(1, 2, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True
    }))
    plot.draw("one_point_full_lines")

    first = Event(1, 2, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True
    })

    plot = Diagram()
    plot.add_event(first)
    plot.add_event(Event(3, 1, settings={}))
    plot.draw("two_points_one_line")

    plot = Diagram()
    plot.add_event(first)
    plot.add_event(Event(3, 1, settings={
        "t_first": True,
        "t_second": False,
        "z_first": True,
        "z_second": False
    }))
    plot.draw("two_points_partial_lines")

    plot = Diagram()
    plot.add_event(first)
    plot.add_event(Event(3, 1, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True
    }))
    plot.draw("two_points_full_lines")

    second = Event(3, 1, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True
    })

    plot = Diagram()
    plot.add_event(first)
    plot.add_event(second)
    plot.add_difference(Difference(first, second, settings={
        "direct": True
    }))
    plot.draw("two_points_connected")

    plot = Diagram()
    plot.add_event(first)
    plot.add_event(second)
    plot.add_difference(Difference(first, second, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True
    }))
    plot.draw("two_points_connected_coordinates")

if time_space:
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
    plot.add_event(Event(1, 2, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True
    }))
    plot.add_event(Event(3, 1, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True
    }))
    plot.draw("two_points_default_frame")

    wl = WorldLine(
        origin=Point(0.0, 0.0),
        beta=-0.5,
        settings={
            "time": True,
            "time_ticks": True,
            "space": True,
            "space_ticks": True
        })

    plot = Diagram()
    plot.add_world_line(wl)
    plot.add_event(Event(1, 2, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True
    }, world_line=wl))
    plot.add_event(Event(3, 1, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True
    }, world_line=wl))
    plot.draw("two_points_same_time")

    wl = WorldLine(
        origin=Point(0.0, 0.0),
        beta=-0.6,
        settings={
            "time": True,
            "time_ticks": True,
            "space": True,
            "space_ticks": True
        })

    plot = Diagram()
    plot.add_world_line(wl)
    plot.add_event(Event(1, 2, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True
    }, world_line=wl))
    plot.add_event(Event(3, 1, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True
    }, world_line=wl))
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
    plot.add_event(Event(1, 3, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True,
    }))
    plot.add_event(Event(2, 1, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True,
    }))
    plot.draw("two_points_causality_default_frame")

    wl = WorldLine(
        origin=Point(0.0, 0.0),
        beta=-0.6,
        settings={
            "time": True,
            "time_ticks": True,
            "space": True,
            "space_ticks": True
        })

    plot = Diagram()
    plot.add_world_line(wl)
    plot.add_event(Event(1, 3, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True
    }, world_line=wl))
    plot.add_event(Event(2, 1, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True
    }, world_line=wl))
    plot.draw("two_points_causality_inverted")

    wl = WorldLine(
        origin=Point(0.0, 0.0),
        beta=0.6,
        settings={
            "time": True,
            "time_ticks": True,
            "space": True,
            "space_ticks": True
        })

    plot = Diagram()
    plot.add_world_line(wl)
    plot.add_event(Event(1, 3, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True
    }, world_line=wl))
    plot.add_event(Event(2, 1, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True
    }, world_line=wl))
    plot.draw("two_points_causality_forward")


if world_line:

    # Sixth image: Introduction of worldlines
    plot = Diagram()
    plot.add_event(Event(0.0, 0, settings={}))
    plot.draw("worldline_first_point")

    plot.add_event(Event(0.6, 1, settings={
        "t_first": True,
        "t_second": False,
        "z_first": True,
        "z_second": False
    }))
    plot.draw("worldline_second_point")

    plot.add_event(Event(1.2, 2, settings={
        "t_first": True,
        "t_second": False,
        "z_first": True,
        "z_second": False
    }))
    plot.draw("worldline_third_point")

    plot.add_event(Event(1.8, 3, settings={
        "t_first": True,
        "t_second": False,
        "z_first": True,
        "z_second": False
    }))
    plot.draw("worldline_fourth_point")

    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={"time": True}))
    plot.draw("worldline_introduce_line")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={"time": True}))
    plot.draw("worldline_time")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={"time": True, "time_angle": True}))
    plot.draw("worldline_time_angle")

    plot = Diagram()
    plot.add_event(Event(0.0, 0.0, settings={}))
    plot.add_event(Event(1.0, 0.0, settings={}))
    plot.add_event(Event(2.0, 0.0, settings={}))
    plot.add_event(Event(3.0, 0.0, settings={}))
    plot.draw("worldline_space_points")

    plot = Diagram()
    plot.add_event(Event(0.0, 0.0, settings={}))
    plot.add_event(Event(1.0, 0.6, settings={
        "t_first": True,
        "t_second": False,
        "z_first": True,
        "z_second": False
    }))
    plot.add_event(Event(2.0, 1.2, settings={
        "t_first": True,
        "t_second": False,
        "z_first": True,
        "z_second": False
    }))
    plot.add_event(Event(3.0, 1.8, settings={
        "t_first": True,
        "t_second": False,
        "z_first": True,
        "z_second": False
    }))
    plot.draw("worldline_space_points_on_line")

    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={"space": True}))
    plot.draw("worldline_introduce_line_space")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={"space": True, "space_angle": True}))
    plot.draw("worldline_space_angle")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={"space": True, "time": True}))
    plot.draw("worldline_all")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "space_angle": True,
        "time_angle": True
    }))
    plot.draw("worldline_all_angle")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.draw("worldline_all_angle_ticks")

    list = [-0.99, -0.95, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, -0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7,
            0.8, 0.9, 0.95, 0.99]

    for i, value in enumerate(list):
        plot = Diagram()
        plot.add_world_line(WorldLine(Point(0, 0), beta=value, settings={"time": True, "space": True}))
        plot.draw(f"gif/beta_{i}")

    plot = Diagram()
    plot.add_event(Event(0.75, 1.25, settings={}))
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": False,
        "space_ticks": False
    }))
    plot.draw("worldline_one_point_on_line")

    plot = Diagram()
    plot.add_event(Event(0.75, 1.25, settings={}))
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.draw("worldline_one_point_on_scale")

    plot = Diagram()
    plot.add_event(Event(3, 3, settings={}))
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.draw("point_read_no_lines")

    plot = Diagram()
    plot.add_event(Event(3, 3, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True
    }))
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.draw("point_read_basic_lines")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(3, 3, settings={
        "t_first": True,
        "t_second": True,
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("point_read_moving_lines")

if dil_con:
    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(1.5, 2.5, settings={}, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("dilatation_first_point")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(1.5, 2.5, settings={
        "z_first": True,
        "z_second": True
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("dilatation_first_rest_frame")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(1.5, 2.5, settings={
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("dilatation_first_moving_frame")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(0, 2, settings={}, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("dilatation_second_point")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(0, 2, settings={
        "z_first": True,
        "z_second": True
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("dilatation_second_rest_frame")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(0, 2, settings={
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("dilatation_second_moving_frame")

    plot = Diagram()
    plot.add_event(Event(1.5, 2.5, settings={
        "z_first": True,
        "z_second": True,
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(0.0, 2.0, settings={
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("dilatation_both")

    plot = Diagram()
    plot.add_event(Event(1.5, 2.5, settings={
        "z_first": True,
        "z_second": True,
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(0.0, 2.0, settings={
        "z_first": True,
        "z_second": True,
        "use_world_line_as_default": True,
        "hyperbel": True
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("dilatation_both_hyperbel")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(2.5, 1.5, settings={}, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("contraction_first_point")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(2.5, 1.5, settings={
        "t_first": True,
        "t_second": True,
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("contraction_first_rest_frame")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(2.5, 1.5, settings={
        "t_first": True,
        "t_second": True,
        "use_world_line_as_default": True
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("contraction_first_moving_frame")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(2, 0, settings={}, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("contraction_second_point")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(2, 0, settings={
        "t_first": True,
        "t_second": True,
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("contraction_second_rest_frame")

    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(2, 0, settings={
        "t_first": True,
        "t_second": True,
        "use_world_line_as_default": True
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("contraction_second_moving_frame")

    plot = Diagram()
    plot.add_event(Event(2.5, 1.5, settings={
        "t_first": True,
        "t_second": True,
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(2, 0, settings={
        "t_first": True,
        "t_second": True,
        "use_world_line_as_default": True
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("contraction_both")

    plot = Diagram()
    plot.add_event(Event(2.5, 1.5, settings={
        "t_first": True,
        "t_second": True,
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "time_ticks": True,
        "space_ticks": True
    }))
    plot.add_event(Event(2, 0, settings={
        "t_first": True,
        "t_second": True,
        "use_world_line_as_default": True,
        "hyperbel": True
    }, world_line=Line(Point(0, 0), beta=0.6)))
    plot.draw("contraction_both_hyperbel")

if vel_add:
    plot = Diagram()
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.6, settings={
        "space": True,
        "time": True,
        "angle_space": True,
        "angle_time": True,
    }))
    plot.add_world_line(WorldLine(Point(0, 0), beta=0.8, settings={
        "space": True,
        "time": True,
        "angle_space": True,
        "angle_time": True,
    }))
    plot.draw("two_velocities")
