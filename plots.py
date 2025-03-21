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
plot = Diagram()
plot.add_data_point(DataPoint(1, 2, time="FULL", space="FULL"))
plot.add_data_point(DataPoint(3, 1, time=None, space=None))
plot.draw("two_points_no_lines")

plot = Diagram()
plot.add_data_point(DataPoint(1, 2, time="FULL", space="FULL"))
plot.add_data_point(DataPoint(3, 1, time="PART", space="PART"))
plot.draw("two_points_partial_lines")

plot = Diagram()
plot.add_data_point(DataPoint(1, 2, time="FULL", space="FULL"))
plot.add_data_point(DataPoint(3, 1, time="FULL", space="FULL"))
plot.draw("two_points_ful_lines")

# FOurth image: introduction of light
SETTINGS["LIGHT"] = True
plot = Diagram()
plot.draw("light")
