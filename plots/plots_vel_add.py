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
                "space_angle": True,
                "time_angle": True,
            },
        )
    )
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.8,
            settings={
                "space": True,
                "time": True,
                "space_angle": True,
                "time_angle": True,
            },
            color="C4",
        )
    )
    plot.draw("two_velocities")

    plot = Diagram()
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=-0.6,
            settings={
                "space": True,
                "time": True,
                "space_angle": True,
                "time_angle": True,
            },
        )
    )
    plot.add_world_line(
        WorldLine(
            Point(0, 0),
            beta=0.38,
            settings={
                "space": True,
                "time": True,
                "space_angle": True,
                "time_angle": True,
            },
            color="C4",
        )
    )
    plot.draw("two_velocities_switch")