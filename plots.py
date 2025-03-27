from diagram import *
from settings import *

# First image: only showing the axis
SETTINGS["LIGHT"] = False
plot = Diagram()
plot.draw("empty")

# Second images: introduce a datapoint

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

# Third images: introduce a second datapoint

first = Event(1, 2, settings={
    "t_first": True,
    "t_second": True,
    "z_first": True,
    "z_second": True
})

plot = Diagram()
plot.add_event(Event(1, 2, settings={
    "t_first": True,
    "t_second": True,
    "z_first": True,
    "z_second": True
}))
plot.add_event(Event(3, 1, settings={
    "t_first": False,
    "t_second": False,
    "z_first": False,
    "z_second": False
}))
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

# Fourth image: introduction of light
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

# Fifth image: Future and Past
plot = Diagram()
plot.add_event(Event(1, 2, settings={}))
plot.add_event(Event(3, 1, settings={}))

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
plot.draw("worldline_time_angle")
