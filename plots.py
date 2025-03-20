from main import layout
import matplotlib.pyplot as plt

# First image: only showing the axis
fig, ax = layout(light=False)
plt.savefig("./img/empty.svg")

# Second image: introduction of light
fig, ax = layout()
plt.savefig("./img/light.svg")
