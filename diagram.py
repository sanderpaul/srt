import copy
import matplotlib.pyplot as plt
import numpy as np
from settings import *


class Point:

    def __init__(self, z, t):
        self.z = z
        self.t = t


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


class WorldLine:

    def __init__(self, origin: Point, beta, settings: dict, linestyle=SETTINGS["WORLD_LINE"],
                 color=SETTINGS["WORLD_LINE_COLOR"]):

        self.beta = beta
        self.origin = origin
        self.lines = []

        outer_corner = max(SETTINGS["WIDTH"], SETTINGS["HEIGHT"])

        r = np.linspace(- outer_corner, outer_corner, 2)

        label = fr"$\beta =$ {beta}" if (float(origin.t) != 0.0 or float(
            origin.z) != 0.0) else fr"$\beta =$ {beta}, z: {origin.z}, t: {origin.t}"

        if "time" in settings.keys() and settings["time"]:
            self.lines.append(plt.Line2D(beta * (r - origin.t) + origin.z, r,
                                         color=color, linestyle=linestyle, label=label))

            if "space" in settings.keys() and settings["space"]:
                self.lines.append(plt.Line2D(r, beta * (r - origin.z) + origin.t, color=color, linestyle=linestyle))

        elif "space" in settings.keys() and settings["space"]:
            self.lines.append(
                plt.Line2D(r, beta * (r - origin.z) + origin.t, color=color, linestyle=linestyle, label=label))


class Difference:

    def __init__(self, first: Point, second: Point, settings: dict, beta=0.0, color=SETTINGS["DIFF_COLOR"],
                 linestyle=SETTINGS["DIFF_LINE"]):
        self.lines = []

        if "direct" in settings.keys() and settings["direct"]:
            self.lines.append(plt.Line2D([first.z, second.z], [first.t, second.t], color=color, linestyle=linestyle))
            return

        zT, tT = intersect(first, second, beta)  # Intersection with Time Axis
        zS, tS = intersect(second, first, beta)  # Intersection with Space Axis

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
        for line in world_line.lines:
            self._lines.append(line)

        return self

    def add_event(self, event: Event):
        self._events.append(event)

        for line in event.lines:
            self._lines.append(line)

        return self

    def add_difference(self, difference: Difference):
        for diff in difference.lines:
            self._lines.append(diff)

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


def intersect(first: Point, second: Point, beta):
    z = (beta * (second.t - first.t) - beta ** 2 * second.z + first.z) / (1 - beta ** 2)
    t = beta * (z - second.z) + second.t

    return round(z, 2), round(t, 2)
