# SRT Plotting

A Python library for generating Minkowski spacetime diagrams to visualise Special Relativity. Built as a companion to teaching material at ETH Zürich.

## Requirements

```
pip install numpy matplotlib
```

## Usage

Run `create_plots.py` from the project root to generate all diagrams:

```bash
python create_plots.py
```

Output PNGs are written to `img/`. The folder is created automatically if it does not exist.

To generate only specific sections, comment out entries in the `sections` list inside `create_plots.py`:

```python
sections = [
    "plots_intro",
    # "plots_time_space",
    "plots_world_line",
    ...
]
```

## Project Structure

```
create_plots.py      # Entry point — lists which sections to run
settings.py          # Global SETTINGS dict and with_global_settings decorator
diagram.py           # Core library: Point, Event, Line, WorldLine, Difference, Diagram
plots/               # One file per topic
    plots_intro.py
    plots_time_space.py
    plots_world_line.py
    plots_dil_con.py
    plots_vel_add.py
    plots_doppler.py
    plots_muon.py
    plots_twins.py
img/                 # Generated output (git-ignored)
    gif/             # Frame sequence for worldline animation
```

## Core Concepts

### Coordinate Convention

All diagrams use natural units with *c* = 1. The horizontal axis is space (*z*), the vertical axis is time (*ct*). A worldline with velocity β has slope dt/dz = 1/β on the diagram.

### Key Classes

| Class | Description |
|---|---|
| `Point(z, t)` | Bare spacetime coordinate |
| `Event(z, t, settings, ...)` | Point with optional coordinate lines drawn to the axes |
| `Line(origin, beta)` | Inertial worldline (mathematical, not drawn) |
| `WorldLine(origin, beta, settings, ...)` | Drawn worldline with optional ticks and angle arcs |
| `Difference(first, second, settings, ...)` | Coordinate separation lines between two points |
| `Diagram()` | Accumulates elements and saves to PNG via `.draw(name)` |

### Key Functions

| Function | Description |
|---|---|
| `lorentz(point, beta)` | Lorentz boost: transforms a point to the frame moving at β |
| `convert(point, input, output)` | Converts a point from the `input` frame's local coordinates to `output` frame (or to the lab frame if no output given) |
| `connect(first, second, beta)` | Finds the axis intersections needed to draw coordinate lines between two events |
| `intersect(first, second, settings)` | Finds intersections between time/space axes of two lines |

### Event Settings

An `Event` accepts a `settings` dict controlling which coordinate lines are drawn:

| Key | Effect |
|---|---|
| `t_first` / `t_second` | Draw time-coordinate line from this event / the reference |
| `z_first` / `z_second` | Draw space-coordinate line from this event / the reference |
| `use_world_line_as_default` | Measure coordinates relative to the given `world_line` instead of the lab axes |
| `future` / `past` / `independent` | Shade the future/past/spacelike region of this event's light cone |
| `hyperbel` | Draw the Minkowski-invariant hyperbola through this event |

### WorldLine Settings

| Key | Effect |
|---|---|
| `time` | Draw the time axis (worldline) |
| `time_ticks` | Add proper-time tick marks along the time axis |
| `time_angle` | Draw an arc showing the angle from the *ct*-axis |
| `space` | Draw the space axis (simultaneity surface) |
| `space_ticks` | Add proper-length tick marks along the space axis |
| `space_angle` | Draw an arc showing the angle from the *z*-axis |

### Global Settings

All visual parameters live in the `SETTINGS` dict in `settings.py`. Key entries:

| Key | Default | Description |
|---|---|---|
| `CORNER` / `UP` / `DOWN` / `LEFT` / `RIGHT` | 5 | Axis extents |
| `LIGHT` | `True` | Show light cone diagonals |
| `TIME_LIKE` / `SPACE_LIKE` | `False` | Shade timelike / spacelike regions |
| `LEGEND_LOC` | `"lower left"` | Legend position |
| `X_AXIS_LABEL` / `Y_AXIS_LABEL` | `"Space [z]"` / `"Time [ct]"` | Axis labels |
| `TICK_LENGTH` | `0.05` | Length of axis and worldline tick marks |

Each plot section's `run()` function is decorated with `@with_global_settings`, which saves and restores the full `SETTINGS` dict so sections cannot affect each other.

## Adding a New Section

1. Create `plots/plots_mysection.py`:

```python
import settings
from diagram import *
from settings import *


@with_global_settings
def run():
    plot = Diagram()
    plot.add_event(Event(1, 2, settings={}))
    plot.draw("mysection_first")
```

2. Add one line to `create_plots.py`:

```python
sections = [
    ...
    "plots_mysection",
]
```