import matplotlib.pyplot as plt
import numpy as np
from zmq.backend import first

from settings import *


class Diagram:

    def __init__(self):
        self._world_lines = []
        self._data_points = []
        self._differences = []

        self.figure = None
        self.axes = None

    def add_world_line(self, line):
        self._world_lines.append(line)
        return self

    def add_data_point(self, point):
        self._data_points.append(point)
        return self

    def add_difference(self, difference):
        self._differences.append(difference)


    def draw(self, plot_name):
        if self.figure is None:
            self.prepare()

        plt.figure(self.figure)
        plt.savefig(f"./img/{plot_name}.png")

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
            ax.plot([-SETTINGS["WIDTH"], SETTINGS["WIDTH"]], [-SETTINGS["HEIGHT"], SETTINGS["HEIGHT"]],
                    color=SETTINGS["LIGHT_COLOR"])
            ax.plot([-SETTINGS["WIDTH"], SETTINGS["WIDTH"]], [SETTINGS["HEIGHT"], -SETTINGS["HEIGHT"]],
                    color=SETTINGS["LIGHT_COLOR"])

        if SETTINGS["GRID"]:
            ax.grid()

        for line in self._world_lines:
            r = np.linspace(-SETTINGS["WIDTH"], SETTINGS["WIDTH"], 100)

            label = r"$\beta =$" + str(line.beta)
            if line.t != 0.0 or line.z != 0.0:
                label = label + ", z: " + str(line.z) + ", t: " + str(line.t)

            if line.space:
                ax.plot(r, line.beta * (r - line.z) + line.t, linestyle=line.linestyle,
                        color=line.color, label=label)
                if line.time:
                    ax.plot(line.beta * (r - line.t) + line.z, r, linestyle=line.linestyle,
                            color=line.color)

            elif line.time:
                ax.plot(line.beta * (r - line.t) + line.z, r, linestyle=line.linestyle,
                        color=line.color, label=label)

        for i, data_point in enumerate(self._data_points):
            ax.plot(data_point.z, data_point.t, marker=SETTINGS["DATA_MARKER"], color=SETTINGS["DATA_COLOR"],
                    linestyle="None", label=rf"$z_{i}$: " + str(data_point.z) + rf", $t_{i}$: " + str(data_point.t))

            z0 = 0
            t0 = 0
            zS = 0
            zT = data_point.z
            tS = data_point.t
            tT = 0

            if type(data_point.world_line) == WorldLine:
                zT, tT = intersect(data_point.z, data_point.t, data_point.world_line.z, data_point.world_line.t,
                                   data_point.world_line.beta)
                zS, tS = intersect(data_point.world_line.z, data_point.world_line.t, data_point.z, data_point.t,
                                   data_point.world_line.beta)

            if data_point.time is not None:
                ax.plot([zT, data_point.z], [tT, data_point.t], color=SETTINGS["DATA_COLOR"],
                        linestyle=SETTINGS["DATA_LINE"])

                if data_point.time == "FULL":
                    ax.plot([z0, zT], [t0, tT], color=SETTINGS["DATA_COLOR"], linestyle=SETTINGS["DATA_LINE"])

            if data_point.space is not None:
                ax.plot([zS, data_point.z], [tS, data_point.t], color=SETTINGS["DATA_COLOR"],
                        linestyle=SETTINGS["DATA_LINE"])

                if data_point.time == "FULL":
                    ax.plot([z0, zS], [t0, tS], color=SETTINGS["DATA_COLOR"], linestyle=SETTINGS["DATA_LINE"])

        for diff in self._differences:
            if diff.connection == "DIRECT":
                ax.plot([diff.first.z, diff.second.z], [diff.first.t, diff.second.t], color=SETTINGS["DIFF_COLOR"],
                        linestyle=SETTINGS["DIFF_LINE"])

            elif diff.connection == "COORDINATES":
                if diff.beta == 0.0:
                    ax.plot([diff.first.z, diff.first.z], [diff.first.t, diff.second.t], color=SETTINGS["DIFF_COLOR"],
                            linestyle=SETTINGS["DIFF_LINE"])
                    ax.plot([diff.first.z, diff.second.z], [diff.first.t, diff.first.t], color=SETTINGS["DIFF_COLOR"],
                            linestyle=SETTINGS["DIFF_LINE"])
                    ax.plot([diff.second.z, diff.second.z], [diff.first.t, diff.second.t], color=SETTINGS["DIFF_COLOR"],
                            linestyle=SETTINGS["DIFF_LINE"])
                    ax.plot([diff.first.z, diff.second.z], [diff.second.t, diff.second.t], color=SETTINGS["DIFF_COLOR"],
                            linestyle=SETTINGS["DIFF_LINE"])
                else:
                    zT, tT = intersect(diff.first.z, diff.first.t, diff.second.z, diff.second.t,
                                       diff.beta)
                    zS, tS = intersect(diff.second.z, diff.second.t, diff.first.z, diff.first.t,
                                       diff.beta)

                    ax.plot([zT, diff.first.z], [tT, diff.first.t], color=SETTINGS["DIFF_COLOR"],
                            linestyle=SETTINGS["DIFF_LINE"])
                    ax.plot([diff.second.z, zT], [diff.second.t, tT], color=SETTINGS["DIFF_COLOR"],
                            linestyle=SETTINGS["DIFF_LINE"])
                    ax.plot([zS, diff.first.z], [tS, diff.first.t], color=SETTINGS["DIFF_COLOR"],
                            linestyle=SETTINGS["DIFF_LINE"])
                    ax.plot([diff.second.z, zS], [diff.second.t, tS], color=SETTINGS["DIFF_COLOR"],
                            linestyle=SETTINGS["DIFF_LINE"])


        if len(self._world_lines) + len(self._data_points) > 0 and SETTINGS["LEGEND"]:
            ax.legend()

        self.figure = figure
        self.axes = ax


class WorldLine:

    def __init__(self, z, t, beta, time=True, space=True, linestyle=SETTINGS["WORLD_LINE"],
                 color=SETTINGS["WORLD_LINE_COLOR"]):
        self.beta = beta
        self.z = z
        self.t = t
        self.time = time
        self.space = space
        self.linestyle = linestyle
        self.color = color


class DataPoint:

    def __init__(self, z, t, time=None, space=None, world_line=None):
        self.z = z
        self.t = t
        self.time = time
        self.space = space
        self.world_line = world_line


class Difference:

    def __init__(self, first, second, direction=None, connection="DIRECT", beta=0.0):
        self.first = first
        self.second = second
        self.direction = direction
        self.beta = beta
        self.connection = connection

def intersect(z1, t1, z2, t2, beta):
    z = (beta * (t2 - t1) - beta ** 2 * z2 + z1) / (1 - beta ** 2)
    t = beta * (z - z2) + t2

    return z, t
