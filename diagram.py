import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D

from settings import *


class Point:

    def __init__(self, z, t):
        self.z = np.round(z, 2)
        self.t = np.round(t, 2)

    def __str__(self):
        return "Point(z=%f, t=%f)" % (self.z, self.t)


class Event(Point):

    def __init__(self, z, t, settings: dict, world_line=None):
        super().__init__(z, t)
        self.lines = []
        self.settings = settings
        self.secondary_coordinates = None

        if ("use_world_line_as_default" in settings.keys() and
                settings["use_world_line_as_default"]
                and world_line is not None):

            self.lines.extend(
                Difference(first=self, second=world_line.origin, settings=settings,
                           beta=world_line.beta, color=SETTINGS["DATA_COLOR"],
                           linestyle=SETTINGS["DATA_LINE"]
                           ).lines
            )

        else:
            self.lines.extend(
                Difference(first=self, second=Point(0, 0), settings=settings,
                           beta=0.0, color=SETTINGS["DATA_COLOR"],
                           linestyle=SETTINGS["DATA_LINE"]
                           ).lines
            )

        if world_line is not None:
            beta = world_line.beta
            gamma = 1 / np.sqrt(1 - beta ** 2)

            self.secondary_coordinates = Point(
                gamma * (z - beta * t) - world_line.origin.z,
                gamma * (t - beta * z) - world_line.origin.t
            )

        if "hyperbel" in settings.keys() and settings["hyperbel"]:
            absolute = t ** 2 - z ** 2
            label = fr"$\Delta s^2$: {absolute:.2f}"
            if abs(absolute) < 1e-10:
                pass
            elif absolute > 0:
                z = np.linspace(-SETTINGS["WIDTH"], SETTINGS["WIDTH"], 1000)
                if t > 0:
                    self.lines.append(Line2D(z, np.sqrt(absolute + z ** 2),
                                             color=SETTINGS["HYPERBEL_COLOR"],
                                             linestyle=SETTINGS["HYPERBEL_LINE"],
                                             label=label)
                                      )
                else:
                    self.lines.append(Line2D(z, -np.sqrt(absolute + z ** 2),
                                             color=SETTINGS["HYPERBEL_COLOR"],
                                             linestyle=SETTINGS["HYPERBEL_LINE"],
                                             label=label)
                                      )
            else:
                t = np.linspace(-SETTINGS["HEIGHT"], SETTINGS["HEIGHT"], 1000)
                if z > 0:
                    self.lines.append(Line2D(np.sqrt(abs(absolute) + t ** 2), t,
                                             color=SETTINGS["HYPERBEL_COLOR"],
                                             linestyle=SETTINGS["HYPERBEL_LINE"],
                                             label=label)
                                      )
                else:
                    self.lines.append(Line2D(- np.sqrt(abs(absolute) + t ** 2), t,
                                             color=SETTINGS["HYPERBEL_COLOR"],
                                             linestyle=SETTINGS["HYPERBEL_LINE"],
                                             label=label)
                                      )

    def to_point(self):
        return Point(self.z, self.t)


class Line():

    def __init__(self, origin: Point, beta):
        if abs(beta) > 1:
            raise ValueError("beta must be in [-1, 1]")

        self.origin = origin
        self.beta = beta


class WorldLine(Line):

    def __init__(self, origin: Point, beta, settings: dict, linestyle=SETTINGS["WORLD_LINE"],
                 color=SETTINGS["WORLD_LINE_COLOR"]):
        super().__init__(origin, beta)

        self.gamma = 1 / np.sqrt(1 - beta ** 2)
        self.angles = []
        self.ticks = []
        self.time = None
        self.space = None

        outer_corner = max(SETTINGS["WIDTH"], SETTINGS["HEIGHT"])

        r = np.linspace(- outer_corner, outer_corner, 2)

        label = fr"$\beta$: {beta:.2f}" if (
                abs(origin.t) < 1e-3 or abs(origin.z) < 1e-3
        ) else fr"$\beta$: {beta:.2f}, z: {origin.z:.2f}, t: {origin.t:.2f}"

        if "time" in settings.keys() and settings["time"]:
            self.time = plt.Line2D(beta * (r - origin.t) + origin.z, r, color=color, linestyle=linestyle, label=label)

            if "time_angle" in settings.keys() and settings["time_angle"] and abs(beta) > 1e-3:
                if beta > 0:
                    self.angles.append(patches.Arc(
                        xy=(origin.z, origin.t), width=3 * beta, height=3 * beta, angle=0,
                        theta1=np.arctan(1 / beta) * 180 / np.pi,
                        theta2=90, color=color)
                    )
                else:
                    self.angles.append(patches.Arc(
                        xy=(origin.z, origin.t), width=-3 * beta, height=-3 * beta, angle=0,
                        theta1=90,
                        theta2=90 + np.arctan(-beta) * 180 / np.pi, color=color)
                    )

            if "time_ticks" in settings.keys() and settings["time_ticks"]:
                n_ticks = 4 * outer_corner + 1
                dz = SETTINGS["TICK_LENGTH"] * np.cos(np.arctan(self.beta))
                dt = SETTINGS["TICK_LENGTH"] * np.sin(np.arctan(self.beta))

                r = np.linspace(- 2 * outer_corner, 2 * outer_corner, n_ticks, endpoint=True)
                t = origin.t + r * self.gamma
                z = origin.z + r * self.beta * self.gamma

                if abs(beta) < 1e-3:
                    self.time = plt.Line2D(z, t, color=color, label=label)
                else:
                    self.time = plt.Line2D(z, t, color=color, label=label)

                for z_i, t_i in zip(z, t):
                    self.ticks.append(plt.Line2D(
                        [z_i + dz, z_i - dz], [t_i - dt, t_i + dt], color=color
                    ))

        if "space" in settings.keys() and settings["space"]:
            if "time" in settings.keys() and settings["time"]:
                self.space = plt.Line2D(r, beta * (r - origin.z) + origin.t, color=color, linestyle=linestyle)
            else:
                self.space = plt.Line2D(r, beta * (r - origin.z) + origin.t, color=color, linestyle=linestyle,
                                        label=label)

            if "space_angle" in settings.keys() and settings["space_angle"] and abs(beta) > 1e-3:
                if beta > 0:
                    self.angles.append(patches.Arc(
                        xy=(origin.z, origin.t), width=3 * beta, height=3 * beta, angle=0, theta1=0,
                        theta2=np.arctan(beta) * 180 / np.pi, color=color
                    ))
                else:
                    self.angles.append(patches.Arc(
                        xy=(origin.z, origin.t), width=-3 * beta, height=-3 * beta, angle=0,
                        theta1=180 - np.arctan(-beta) * 180 / np.pi,
                        theta2=180, color=color
                    ))

            if "space_ticks" in settings.keys() and settings["space_ticks"]:
                self.space = None
                n_ticks = 4 * outer_corner + 1
                dz = SETTINGS["TICK_LENGTH"] * np.sin(np.arctan(self.beta))
                dt = SETTINGS["TICK_LENGTH"] * np.cos(np.arctan(self.beta))

                r = np.linspace(- 2 * outer_corner, 2 * outer_corner, n_ticks, endpoint=True)
                t = origin.t + r * self.beta * self.gamma
                z = origin.z + r * self.gamma

                if "time" in settings.keys() and settings["time"]:
                    self.space = plt.Line2D(z, t, color=color)
                else:
                    self.space = plt.Line2D(z, t, color=color, label=label)

                for z_i, t_i in zip(z, t):
                    self.ticks.append(plt.Line2D(
                        [z_i + dz, z_i - dz], [t_i - dt, t_i + dt], color=color
                    ))


class Difference:

    def __init__(self, first: Point, second: Point, settings: dict, beta=0.0, color=SETTINGS["DIFF_COLOR"],
                 linestyle=SETTINGS["DIFF_LINE"]):
        self.lines = []

        if "direct" in settings.keys() and settings["direct"]:
            self.lines.append(plt.Line2D(
                [first.z, second.z], [first.t, second.t], color=color, linestyle=linestyle))
            return

        intersections = connect(first, second, beta)  # Intersection with Space Axis

        if "t_first" in settings.keys() and settings["t_first"]:
            self.lines.append(plt.Line2D(
                [intersections["time_space"].z, first.z],
                [intersections["time_space"].t, first.t],
                color=color, linestyle=linestyle)
            )

        if "t_second" in settings.keys() and settings["t_second"]:
            self.lines.append(plt.Line2D(
                [intersections["time_space"].z, second.z],
                [intersections["time_space"].t, second.t],
                color=color, linestyle=linestyle)
            )

        if "z_first" in settings.keys() and settings["z_first"]:
            self.lines.append(plt.Line2D(
                [intersections["space_time"].z, first.z],
                [intersections["space_time"].t, first.t],
                color=color, linestyle=linestyle)
            )

        if "z_second" in settings.keys() and settings["z_second"]:
            self.lines.append(plt.Line2D(
                [intersections["space_time"].z, second.z],
                [intersections["space_time"].t, second.t],
                color=color, linestyle=linestyle)
            )


class Diagram:

    def __init__(self):
        self._lines = []
        self._events = []
        self._patches = []

        self.figure = None
        self.axes = None

    def __del__(self):
        del self._events
        del self._lines
        del self.figure

    def add_world_line(self, world_line: WorldLine):
        if world_line.time is not None:
            self._lines.append(world_line.time)
        if world_line.space is not None:
            self._lines.append(world_line.space)
        for angle in world_line.angles:
            self._patches.append(angle)
        for tick in world_line.ticks:
            self._lines.append(tick)

        return self

    def add_event(self, event: Event):
        self._events.append(event)

        for line in event.lines:
            self._lines.append(line)

        return self

    def add_difference(self, difference: Difference):
        for diff in difference.lines:
            self._lines.append(diff)

        return self

    def draw(self, plot_name):
        if self.figure is None:
            self.prepare()

        plt.figure(self.figure)
        plt.savefig(f"./img/{plot_name}.png")
        plt.close(self.figure)

        self.figure = None

    def prepare(self):
        figure = plt.figure(figsize=(SETTINGS["FIG_WIDTH"], SETTINGS["FIG_HEIGHT"]))
        figure.text(0.57, 0.12, "Paul Sander, ETH Zürich", fontsize=15, color="gray", alpha=0.2)
        ax = figure.add_subplot(111)

        inner_corner = min(SETTINGS["WIDTH"], SETTINGS["HEIGHT"])
        outer_corner = max(SETTINGS["WIDTH"], SETTINGS["HEIGHT"])

        ax.set_title(SETTINGS["TITLE"])
        ax.set_xlim(-SETTINGS["WIDTH"], SETTINGS["WIDTH"])
        ax.set_ylim(-SETTINGS["HEIGHT"], SETTINGS["HEIGHT"])

        if SETTINGS["AXIS"]:
            ax.plot([-SETTINGS["WIDTH"], SETTINGS["WIDTH"]], [0, 0], color=SETTINGS["AXIS_COLOR"])
            ax.plot([0, 0], [-SETTINGS["HEIGHT"], SETTINGS["HEIGHT"]], color=SETTINGS["AXIS_COLOR"])
            ax.set_xlabel(SETTINGS["X_AXIS_LABEL"])
            ax.set_ylabel(SETTINGS["Y_AXIS_LABEL"])

            if SETTINGS["AXIS_TICK"]:
                for i in range(-outer_corner, outer_corner + 1):
                    ax.plot([i, i], [-SETTINGS["TICK_LENGTH"], SETTINGS["TICK_LENGTH"]],
                            color=SETTINGS["AXIS_COLOR"]
                            )
                    ax.plot([-SETTINGS["TICK_LENGTH"], SETTINGS["TICK_LENGTH"]], [i, i],
                            color=SETTINGS["AXIS_COLOR"]
                            )

        if SETTINGS["LIGHT"]:
            ax.plot([-inner_corner, inner_corner], [-inner_corner, inner_corner],
                    color=SETTINGS["LIGHT_COLOR"], alpha=SETTINGS["LIGHT_ALPHA"])
            ax.plot([-inner_corner, inner_corner], [inner_corner, -inner_corner],
                    color=SETTINGS["LIGHT_COLOR"], alpha=SETTINGS["LIGHT_ALPHA"])

            if SETTINGS["SPACE_LIKE"]:
                ax.fill_between([0, inner_corner, SETTINGS["WIDTH"]], [0, inner_corner, SETTINGS["WIDTH"]],
                                [0, -inner_corner, -SETTINGS["WIDTH"]], alpha=SETTINGS["SPACE_ALPHA"],
                                color=SETTINGS["SPACE_COLOR"])
                ax.fill_between([0, -inner_corner, -SETTINGS["WIDTH"]], [0, inner_corner, SETTINGS["WIDTH"]],
                                [0, -inner_corner, -SETTINGS["WIDTH"]], alpha=SETTINGS["SPACE_ALPHA"],
                                color=SETTINGS["SPACE_COLOR"])

            if SETTINGS["TIME_LIKE"]:
                ax.fill_between([-inner_corner, 0, inner_corner], [inner_corner, 0, inner_corner],
                                [SETTINGS["HEIGHT"], SETTINGS["HEIGHT"], SETTINGS["HEIGHT"]],
                                alpha=SETTINGS["TIME_ALPHA"],
                                color=SETTINGS["TIME_COLOR"])
                ax.fill_between([-inner_corner, 0, inner_corner],
                                [-SETTINGS["HEIGHT"], -SETTINGS["HEIGHT"], -SETTINGS["HEIGHT"]],
                                [-inner_corner, 0, -inner_corner],
                                alpha=SETTINGS["TIME_ALPHA"], color=SETTINGS["TIME_COLOR"])

        if SETTINGS["GRID"]:
            ax.grid()

        for line in self._lines:
            ax.add_line(copy.deepcopy(line))

        for patch in self._patches:
            ax.add_patch(patch)

        for i, event in enumerate(self._events):
            if event.secondary_coordinates is not None:
                ax.plot(event.z, event.t,
                        marker=SETTINGS["DATA_MARKER"],
                        color=SETTINGS["DATA_COLOR"],
                        linestyle="None",
                        label=(rf"$z_{i + 1}$: {event.z:.2f}, "
                               rf"$ct_{i + 1}$: {event.t:.2f} || "
                               rf"$z_{i + 1}'$: {event.secondary_coordinates.z:.2f}, "
                               rf"$ct_{i + 1}'$: {event.secondary_coordinates.t:.2f}")
                        )
            else:
                ax.plot(event.z, event.t, marker=SETTINGS["DATA_MARKER"], color=SETTINGS["DATA_COLOR"],
                        linestyle="None",
                        label=rf"$z_{i + 1}$: {event.z:.2f}, $ct_{i + 1}$: {event.t:.2f}"
                        )

            if "future" in event.settings.keys() and event.settings["future"]:
                ax.fill_between(
                    [-SETTINGS["WIDTH"], event.z, SETTINGS["WIDTH"]],
                    [SETTINGS["WIDTH"] + event.z + event.t, event.t, SETTINGS["WIDTH"] - event.z + event.t],
                    [SETTINGS["HEIGHT"], SETTINGS["HEIGHT"], SETTINGS["HEIGHT"]],
                    alpha=SETTINGS["TIME_ALPHA"], color=SETTINGS["DATA_COLOR"]
                )

            if "past" in event.settings.keys() and event.settings["past"]:
                ax.fill_between(
                    [-SETTINGS["WIDTH"], event.z, SETTINGS["WIDTH"]],
                    [-SETTINGS["HEIGHT"], -SETTINGS["HEIGHT"], -SETTINGS["HEIGHT"]],
                    [-SETTINGS["WIDTH"] - event.z + event.t, event.t, -SETTINGS["WIDTH"] + event.z + event.t],
                    alpha=SETTINGS["TIME_ALPHA"], color=SETTINGS["TIME_COLOR"]
                )

            if "independent" in event.settings.keys() and event.settings["independent"]:
                ax.fill_between([-outer_corner, event.z], [-outer_corner - event.z + event.t, event.t],
                                [outer_corner + event.t + event.z, event.t],
                                alpha=SETTINGS["SPACE_ALPHA"],
                                color=SETTINGS["SPACE_COLOR"])
                ax.fill_between([outer_corner, event.z], [-outer_corner + event.z + event.t, event.t],
                                [outer_corner + event.t - event.z, event.t],
                                alpha=SETTINGS["SPACE_ALPHA"],
                                color=SETTINGS["SPACE_COLOR"])

        if len(self._lines) + len(self._events) > 0 and SETTINGS["LEGEND"]:
            ax.legend(loc=SETTINGS["LEGEND_LOC"])

        self.figure = figure
        self.axes = ax

    def get_axes(self):
        return self.axes

    def get_figure(self):
        return self.figure

    def clear_axes(self):
        self.axes = None
        self.figure.axes = []


def connect(first: Point, second: Point, beta):
    return intersect(Line(first, beta), Line(second, beta), settings={
        "time_space": True,
        "space_time": True
    })


def intersect(first: Line, second: Line, settings: dict):
    result = {}

    def intersection(p1: Point, m1: float, p2: Point, m2: float):
        z = (p2.t - p1.t + m1 * p1.z - m2 * p2.z) / (m1 - m2)
        t = m1 * (z - p1.z) + p1.t

        return Point(z, t)

    if "time_time" in settings.keys() and settings["time_time"]:
        if abs(first.beta - second.beta) < 1e-3:
            raise ValueError("The two lines share the same slope. They have no or infinite intersections.")
        elif abs(first.beta) < 1e-3:
            result["time_time"] = Point(
                first.origin.z, (first.origin.z - second.origin.z) / second.beta + second.origin.t
            )
        elif abs(second.beta) < 1e-3:
            result["time_time"] = Point(
                second.origin.z, (second.origin.z - first.origin.z) / first.beta + first.origin.t
            )
        else:
            result["time_time"] = intersection(p1=first.origin, m1=1 / first.beta,
                                               p2=second.origin, m2=1 / second.beta)

    if "time_space" in settings.keys() and settings["time_space"]:
        if abs(first.beta) < 1e-3:
            result["time_space"] = Point(
                first.origin.z, second.beta * (first.origin.z - second.origin.z) + second.origin.t
            )
        else:
            result["time_space"] = intersection(p1=first.origin, m1=1 / first.beta,
                                                p2=second.origin, m2=second.beta)

    if "space_time" in settings.keys() and settings["space_time"]:
        if abs(second.beta) < 1e-3:
            result["space_time"] = Point(
                second.origin.z, first.beta * (second.origin.z - first.origin.z) + first.origin.t
            )
        else:
            result["space_time"] = intersection(p1=first.origin, m1=first.beta,
                                                p2=second.origin, m2=1 / second.beta)

    if "space_space" in settings.keys() and settings["space_space"]:
        result["space_space"] = intersection(p1=first.origin, m1=first.beta,
                                             p2=second.origin, m2=second.beta)

    return result
