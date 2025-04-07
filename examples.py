from diagram import *
from settings import *

# SETTINGS (settings.py) contains global settings.
# Overwriting will change the settings permanently
SETTINGS["LIGHT"] = True

# Create a new Diagram. The Diagram contains all objects which are
# plotted. It uses the global settings.
plot = Diagram()

# Create a world line
a_world_line = WorldLine(
    origin=Point(0, 0),  # The origin is the center of the coordniate system.
    beta=0.5,  # The relative speed of the reference system [-1, 1]
    settings={  # settings, which parts will be plotted
        "time": True,  # Time axis
        "time_ticks": True,  # Ticks on the time axis
        "space": True,  # Space axis
        "space_ticks": True,  # Ticks on the space axis
        "time_angle": True,  # Angle between time coordinate system and time axis
        "space_angle": True,  # Angle between space coordinate system and space axis
    }
    # **kwargs allow to set the color or line style locally
)

# Add the world_line to the Diagram
plot.add_world_line(a_world_line)

# Create a new Event
an_event = Event(1,  # z coordinate
                 3,  # t coordinate
                 settings={  # settings, which parts will be plotted
                     "t_first": True,  # Connect point to the time axis
                     "t_second": False,  # Connect intersection with time axis to intersection
                     "z_first": True,  # Connect point to the space axis
                     "z_second": False,  # Connect intersection with space axis to intersection
                     "future": False,  # Show the future of the events
                     "past": False,  # Show the past of the events
                     "independent": False,  # Show the independent regions
                     "use_world_line_as_default": True
                     # If a world line is provided, lines are drawn to this world line
                 },
                 world_line=a_world_line  # This allows to choose a world line the point belongs to.
                 # **kwargs allow to set the color or line style locally
                 )

# Add the world_line to the Diagram
plot.add_event(an_event)

# Plot the diagram and save it as ./img/<name>.png
# The plot can be reused after plotting.
plot.draw("example_one")

# Create an Event with coordinates in a_world_line
# First convert the coordinates to the base or another reference system
moving_coordinates = convert(
    first=Point(z=2, t=0),  # The coordinates in the moving system
    input=a_world_line,  # Coordinate system in which the position is provided
    output=None  # optional coordinate system to transform coordinates to. If None, the base is used
)

# Then convert the point to an event by providing plot settings
# If settings are not provided, they are considered 'False'
another_event = moving_coordinates.to_event(
    settings={  # settings as before
        "t_first": True,  # Connect point to the time axis
        "z_first": True,  # Connect point to the space axis
        "use_world_line_as_default": True
        # If a world line is provided, lines are drawn to this world line
    },
    world_line=a_world_line  # This allows to choose a world line the point belongs to.
    # **kwargs allow to set the color or line style locally
)

# Add another event
plot.add_event(another_event)
plot.draw("example_two")

# Create a Difference between two events. This can either be direct or with respect to a coordinate system
a_difference = Difference(
    first=an_event,  # The first event
    second=another_event,  # The second event
    settings={  # How to connect the two points
        "direct": False,  # A direct line,
        "t_first": True,  # Connect first to the intersection with second at time
        "t_second": True,  # Connect second to the intersection with first at time
        "z_first": True,  # Connect first to the intersection with second at space
        "z_second": True,  # Connect second to the intersection with first at space
    },
    beta=0.5,
    # **kwargs allow to set the color or line style locally
)

# Add difference to the Diagram
plot.add_difference(a_difference)
plot.draw("example_three")
