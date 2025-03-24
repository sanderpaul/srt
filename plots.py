from diagram import *
from settings import *

# First image: only showing the axis
SETTINGS["LIGHT"] = False
plot = Diagram()
plot.draw("empty")

# Second images: introduce a datapoint
plot = Diagram()
plot.add_data_point(DataPoint(1, 2, time=None, space=None))
plot.draw("one_point_no_lines")

plot = Diagram()
plot.add_data_point(DataPoint(1, 2, time="PART", space="PART"))
plot.draw("one_point_partial_lines")

plot = Diagram()
plot.add_data_point(DataPoint(1, 2, time="FULL", space="FULL"))
plot.draw("one_point_full_lines")

# Third images: introduce a second datapoint

first = DataPoint(1, 2, time="FULL", space="FULL")

plot = Diagram()
plot.add_data_point(first)
plot.add_data_point(DataPoint(3, 1, time=None, space=None))
plot.draw("two_points_one_line")

plot = Diagram()
plot.add_data_point(first)
plot.add_data_point(DataPoint(3, 1, time="PART", space="PART"))
plot.draw("two_points_partial_lines")

plot = Diagram()
plot.add_data_point(first)
plot.add_data_point(DataPoint(3, 1, time="FULL", space="FULL"))
plot.draw("two_points_full_lines")

second = DataPoint(3, 1, time="FULL", space="FULL")

plot = Diagram()
plot.add_data_point(first)
plot.add_data_point(second)
plot.add_difference(Difference(first, second))
plot.draw("two_points_connected")

plot = Diagram()
plot.add_data_point(first)
plot.add_data_point(second)
plot.add_difference(Difference(first, second, connection="COORDINATES"))
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
plot.add_data_point(DataPoint(1, 2, time=None, space=None))
plot.add_data_point(DataPoint(3, 1, time=None, space=None))
plot.draw("two_points_no_lines")

plot = Diagram()
plot.add_data_point(DataPoint(1, 2, time=None, space=None, future=True))
plot.add_data_point(DataPoint(3, 1, time=None, space=None, future=True))
plot.draw("two_points_future")

plot = Diagram()
plot.add_data_point(DataPoint(1, 2, time=None, space=None, past=True))
plot.add_data_point(DataPoint(3, 1, time=None, space=None, past=True))
plot.draw("two_points_past")

plot = Diagram()
plot.add_data_point(DataPoint(1, 2, time=None, space=None, future=True, past=True))
plot.add_data_point(DataPoint(3, 1, time=None, space=None, future=True, past=True))
plot.draw("two_points_future_past")

# Sixth image: Introduction of worldlines
plot = Diagram()
plot.add_data_point(DataPoint(0.0, 0, time=None, space=None))
plot.draw("worldline_first_point")

plot.add_data_point(DataPoint(0.6, 1, time="HALF", space="HALF"))
plot.draw("worldline_second_point")

plot.add_data_point(DataPoint(1.2, 2, time="HALF", space="HALF"))
plot.draw("worldline_third_point")

plot.add_data_point(DataPoint(1.8, 3, time="HALF", space="HALF"))
plot.draw("worldline_fourth_point")

plot.add_world_line(WorldLine(0, 0, 0.6, time=True, space=False))
plot.draw("worldline_introduce_line")

plot = Diagram()
plot.add_world_line(WorldLine(0, 0, 0.6, time=True, space=False))
plot.draw("worldline_time_angle")
