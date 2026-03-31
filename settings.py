import copy
import functools

SETTINGS = {
    "FIG_HEIGHT": 8,
    "FIG_WIDTH": 8,

    "CORNER": 5,

    "UP": 5,
    "DOWN": 5,
    "LEFT": 5,
    "RIGHT": 5,

    "TITLE": "Minkowski Space",

    "AXIS": True,
    "AXIS_TICK": True,
    "AXIS_COLOR": "black",
    "X_AXIS_LABEL": "Space [z]",
    "Y_AXIS_LABEL": "Time [ct]",
    "TICK_LENGTH": 0.05,

    "GRID": True,
    "LEGEND": True,
    "LEGEND_LOC": "lower left",

    "LIGHT": True,
    "LIGHT_COLOR": "gray",
    "LIGHT_ALPHA": 0.5,

    "SPACE_LIKE": False,
    "SPACE_COLOR": "C2",
    "SPACE_ALPHA": 0.2,

    "TIME_LIKE": False,
    "TIME_COLOR": "C0",
    "TIME_ALPHA": 0.2,

    "WORLD_LINE": "--",
    "WORLD_LINE_COLOR": "C1",

    "DATA_COLOR": "C0",
    "DATA_LINE": "--",
    "DATA_MARKER": "o",

    "HYPERBEL_LINE": ":",
    "HYPERBEL_COLOR": "C0",

    "DIFF_COLOR": "C2",
    "DIFF_LINE": ":"
}


def with_global_settings(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        saved = copy.copy(SETTINGS)
        fn(*args, **kwargs)
        SETTINGS.clear()
        SETTINGS.update(saved)
    return wrapper