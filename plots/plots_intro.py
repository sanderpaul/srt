import settings
from diagram import *
from settings import *


@with_global_settings
@with_output_folder
def run():
    SETTINGS["LIGHT"] = False
    plot = Diagram()
    plot.draw("empty")

    plot = Diagram()
    plot.add_event(Event(1, 2, settings={}))
    plot.draw("one_point_no_lines")

    plot = Diagram()
    plot.add_event(
        Event(
            1,
            2,
            settings={
                "t_first": True,
                "t_second": False,
                "z_first": True,
                "z_second": False,
            },
        )
    )
    plot.draw("one_point_partial_lines")

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
    plot.draw("one_point_full_lines")

    first = Event(
        1,
        2,
        settings={"t_first": True, "t_second": True, "z_first": True, "z_second": True},
    )

    plot = Diagram()
    plot.add_event(first)
    plot.add_event(Event(3, 1, settings={}))
    plot.draw("two_points_one_line")

    plot = Diagram()
    plot.add_event(first)
    plot.add_event(
        Event(
            3,
            1,
            settings={
                "t_first": True,
                "t_second": False,
                "z_first": True,
                "z_second": False,
            },
        )
    )
    plot.draw("two_points_partial_lines")

    plot = Diagram()
    plot.add_event(first)
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
    plot.draw("two_points_full_lines")

    second = Event(
        3,
        1,
        settings={"t_first": True, "t_second": True, "z_first": True, "z_second": True},
    )

    plot = Diagram()
    plot.add_event(first)
    plot.add_event(second)
    plot.add_difference(Difference(first, second, settings={"direct": True}))
    plot.draw("two_points_connected")

    plot = Diagram()
    plot.add_event(first)
    plot.add_event(second)
    plot.add_difference(
        Difference(
            first,
            second,
            settings={
                "t_first": True,
                "t_second": True,
                "z_first": True,
                "z_second": True,
            },
        )
    )
    plot.draw("two_points_connected_coordinates")