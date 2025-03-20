from diagram import *
from settings import *
import matplotlib.pyplot as plt

settings = SETTINGS

# First image: only showing the axis
settings["LIGHT"] = False
plot = Diagram("empty", settings)
plot.draw()

# Second image: introduction of light
settings["LIGHT"] = True
plot = Diagram("light", settings)
plot.draw()

# Third image: world line at 0.6
plot = Diagram("world", settings)
world_line = WorldLine(0, 0, 0.6)
plot.add_world_line(world_line)
plot.draw()
