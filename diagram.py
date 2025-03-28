import copy
import matplotlib.pyplot as plt
import numpy as np
from settings import *


class Point:

    def __init__(self, z, t):
        self.z = z
        self.t = t

    def __str__(self):
        return "Point(z=%f, t=%f)" % (self.z, self.t)


class Event(Point):

    def __init__(self, z, t, settings: dict, world_line=None):
        super().__init__(z, t)
        self.lines = []
        self.settings = settings

        if world_line is not None:
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

    def to_point(self):
        return Point(self.z, self.t)


class Line():

    def __init__(self, origin: Point, beta):
        if beta > 1:
            raise ValueError("beta must be <= 1")
        if beta < 0:
            raise ValueError("beta must be >= 0")

        self.origin = origin
        self.beta = beta


class WorldLine(Line):

    def __init__(self, origin: Point, beta, settings: dict, linestyle=SETTINGS["WORLD_LINE"],
                 color=SETTINGS["WORLD_LINE_COLOR"]):
        super().__init__(origin, beta)

        self.angles = []
        self.time = None
        self.space = None

        outer_corner = max(SETTINGS["WIDTH"], SETTINGS["HEIGHT"])

        r = np.linspace(- outer_corner, outer_corner, 2)

        label = fr"$\beta =$ {beta}" if (
                abs(origin.t) < 1e-3 or abs(origin.z) < 1e-3
        ) else fr"$\beta =$ {beta}, z: {origin.z}, t: {origin.t}"

        if "time" in settings.keys() and settings["time"]:
            self.time = plt.Line2D(beta * (r - origin.t) + origin.z, r, color=color, linestyle=linestyle, label=label)

            if "space" in settings.keys() and settings["space"]:
                self.space = plt.Line2D(r, beta * (r - origin.z) + origin.t, color=color, linestyle=linestyle)

        elif "space" in settings.keys() and settings["space"]:
            self.space = plt.Line2D(r, beta * (r - origin.z) + origin.t, color=color, linestyle=linestyle, label=label)

        if "time_angle" in settings.keys() and settings["time_angle"]:
            # ToDo
            pass

        if "space_angle" in settings.keys() and settings["space_angle"]:
            # ToDo
            pass


class Difference:

    def __init__(self, first: Point, second: Point, settings: dict, beta=0.0, color=SETTINGS["DIFF_COLOR"],
                 linestyle=SETTINGS["DIFF_LINE"]):
        self.lines = []

        if "direct" in settings.keys() and settings["direct"]:
            self.lines.append(plt.Line2D(
                [first.z, second.z], [first.t, second.t], color=color, linestyle=linestyle))
            return

        zT, tT, zS, tS = connect(first, second, beta)  # Intersection with Space Axis

        if "t_first" in settings.keys() and settings["t_first"]:
            self.lines.append(plt.Line2D([zT, first.z], [tT, first.t], color=color, linestyle=linestyle))

        if "t_second" in settings.keys() and settings["t_second"]:
            self.lines.append(plt.Line2D([zT, second.z], [tT, second.t], color=color, linestyle=linestyle))

        if "z_first" in settings.keys() and settings["z_first"]:
            self.lines.append(plt.Line2D([zS, first.z], [tS, first.t], color=color, linestyle=linestyle))

        if "z_second" in settings.keys() and settings["z_second"]:
            self.lines.append(plt.Line2D([zS, second.z], [tS, second.t], color=color, linestyle=linestyle))


class Diagram:

    def __init__(self):
        self._lines = []
        self._events = []

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
        ax = figure.add_subplot(111)

        ax.set_title(SETTINGS["TITLE"])
        ax.set_xlim(-SETTINGS["WIDTH"], SETTINGS["WIDTH"])
        ax.set_ylim(-SETTINGS["HEIGHT"], SETTINGS["HEIGHT"])

        if SETTINGS["AXIS"]:
            ax.plot([-SETTINGS["WIDTH"], SETTINGS["WIDTH"]], [0, 0], color=SETTINGS["AXIS_COLOR"])
            ax.plot([0, 0], [-SETTINGS["HEIGHT"], SETTINGS["HEIGHT"]], color=SETTINGS["AXIS_COLOR"])
            ax.set_xlabel(SETTINGS["X_AXIS_LABEL"])
            ax.set_ylabel(SETTINGS["Y_AXIS_LABEL"])

        if SETTINGS["LIGHT"]:
            corner = min(SETTINGS["WIDTH"], SETTINGS["HEIGHT"])
            ax.plot([-corner, corner], [-corner, corner],
                    color=SETTINGS["LIGHT_COLOR"], alpha=SETTINGS["LIGHT_ALPHA"])
            ax.plot([-corner, corner], [corner, -corner],
                    color=SETTINGS["LIGHT_COLOR"], alpha=SETTINGS["LIGHT_ALPHA"])

            if SETTINGS["SPACE_LIKE"]:
                ax.fill_between([0, corner, SETTINGS["WIDTH"]], [0, corner, SETTINGS["WIDTH"]],
                                [0, -corner, -SETTINGS["WIDTH"]], alpha=SETTINGS["SPACE_ALPHA"],
                                color=SETTINGS["SPACE_COLOR"])
                ax.fill_between([0, -corner, -SETTINGS["WIDTH"]], [0, corner, SETTINGS["WIDTH"]],
                                [0, -corner, -SETTINGS["WIDTH"]], alpha=SETTINGS["SPACE_ALPHA"],
                                color=SETTINGS["SPACE_COLOR"])

            if SETTINGS["TIME_LIKE"]:
                ax.fill_between([-corner, 0, corner], [corner, 0, corner],
                                [SETTINGS["HEIGHT"], SETTINGS["HEIGHT"], SETTINGS["HEIGHT"]],
                                alpha=SETTINGS["TIME_ALPHA"],
                                color=SETTINGS["TIME_COLOR"])
                ax.fill_between([-corner, 0, corner],
                                [-SETTINGS["HEIGHT"], -SETTINGS["HEIGHT"], -SETTINGS["HEIGHT"]], [-corner, 0, -corner],
                                alpha=SETTINGS["TIME_ALPHA"], color=SETTINGS["TIME_COLOR"])

        if SETTINGS["GRID"]:
            ax.grid()

        for line in self._lines:
            ax.add_line(copy.deepcopy(line))

        for i, event in enumerate(self._events):
            ax.plot(event.z, event.t, marker=SETTINGS["DATA_MARKER"], color=SETTINGS["DATA_COLOR"],
                    linestyle="None",
                    label=rf"$z_{i + 1}$: " + str(event.z) + rf", $t_{i + 1}$: " + str(event.t))

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

        if len(self._lines) + len(self._events) > 0 and SETTINGS["LEGEND"]:
            ax.legend()

        self.figure = figure
        self.axes = ax


def connect(first: Point, second: Point, beta):
    zT = (beta * (second.t - first.t) - beta ** 2 * second.z + first.z) / (1 - beta ** 2)
    tT = beta * (zT - second.z) + second.t

    zS = (beta * (first.t - second.t) - beta ** 2 * first.z + second.z) / (1 - beta ** 2)
    tS = beta * (zS - first.z) + first.t

    return round(zT, 2), round(tT, 2), round(zS, 2), round(tS, 2)


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

    if "time_space" in settings.keys() and settings["time_time"]:
        if abs(first.beta) < 1e-3:
            result["time_space"] = Point(
                first.origin.z, second.beta * (first.origin.z - second.origin.z) + second.origin.t
            )
        else:
            result["time_space"] = intersection(p1=first.origin, m1=1 / first.beta,
                                                p2=second.origin, m2=second.beta)

    if "space_time" in settings.keys() and settings["time_time"]:
        if abs(second.beta) < 1e-3:
            result["space_time"] = Point(
                second.origin.z, first.beta * (second.origin.z - first.origin.z) + first.origin.t
            )
        else:
            result["space_time"] = intersection(p1=first.origin, m1=first.beta,
                                                p2=second.origin, m2=1 / second.beta)

    if "space_space" in settings.keys() and settings["time_time"]:
        result["space_space"] = intersection(p1=first.origin, m1=first.beta,
                                             p2=second.origin, m2=second.beta)

    return result
