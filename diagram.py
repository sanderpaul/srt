import matplotlib.pyplot as plt
import numpy as np
from settings import *


class Diagram:

    def __init__(self, plot_name, settings=SETTINGS):
        self._world_lines = []
        self._data_points = []
        self._settings = settings
        self._plot_name = plot_name

        self.figure = None
        self.axes = None

    def add_world_line(self, line):
        self._world_lines.append(line)

    def add_data_point(self, point):
        self._data_points.append(point)

    def draw(self):
        if self.figure is None:
            self.prepare()

        plt.figure(self.figure)
        plt.savefig(f"./img/{self._plot_name}.svg")

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

            if line.space:
                ax.plot(r, line.beta * (r - line.t) + line.z, linestyle=SETTINGS["WORLD_LINE"],
                        color=SETTINGS["WORLD_LINE_COLOR"], label=r"$\beta =$" + str(line.beta))
            if line.time:
                ax.plot(line.beta * (r - line.z) + line.t, r, linestyle=SETTINGS["WORLD_LINE"],
                        color=SETTINGS["WORLD_LINE_COLOR"])

        if len(self._world_lines) > 0 and SETTINGS["LEGEND"]:
            ax.legend()

        self.figure = figure
        self.axes = ax


class WorldLine:

    def __init__(self, z, t, beta, time=True, space=True):
        self.beta = beta
        self.z = z
        self.t = t
        self.time = time
        self.space = space


class DataPoint:

    def __init__(self, z, t, beta=0, time=False, space=False):
        self.z = z
        self.t = t
        self.time = time
        self.space = space
        self.beta = beta
