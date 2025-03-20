import numpy as np
import matplotlib.pyplot as plt

def layout(grid = True, axis = True, light = True):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    ax.set_title('Minkowski Space')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    if axis:
        ax.plot([-5, 5], [0, 0], color='black')
        ax.plot([0, 0], [-5, 5], color='black')
        ax.set_xlabel('Space [z]')
        ax.set_ylabel('Time [ct]')

    if light:
        ax.plot([-5, 5], [-5, 5], color='gray')
        ax.plot([-5, 5], [5, -5], color='gray')

    if grid:
        ax.grid()

    return fig, ax

def worldlines(ax, beta, z=0, t=0, time=True, space=True, color='C0', linestyle='--'):
    r = np.linspace(-10, 10, 100)

    if space:
        ax.plot(r, beta * (r - t) + z, linestyle=linestyle, color=color)
    if time:
        ax.plot(beta * (r-z) + t, r, linestyle=linestyle, color=color)


fig, ax = layout()
worldlines(ax, 0.6, 2, 1)
plt.show()