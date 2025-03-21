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
plot.draw("two_points_no_lines")

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

# FOurth image: introduction of light
SETTINGS["LIGHT"] = True
plot = Diagram()
plot.draw("light")
