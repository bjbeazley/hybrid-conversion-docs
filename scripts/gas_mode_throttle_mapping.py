#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# Define the segments
x1 = [0, 1]
y1 = [0, 1]


# Create the plot
plt.figure()
plt.plot(x1, y1)

# get the axis 
ax = plt.gca()

# enforce placement of x-axis at y=0
ax.spines['bottom'].set_position('zero')

# Hide the top spine
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ticks = np.arange(0.0, 1.01, 0.25)
ax.set_xticks(ticks)

# Labels and annotations
plt.text(0.03, -0.95, "100% regen", ha="left", va="bottom")
plt.text(0.93, 0.95, "100% power", ha="right", va="top")

# Axis limits
plt.xlim(0, 1)
plt.ylim(0, 1)

# Axis labels
plt.xlabel("Accelerator Position")
plt.ylabel("Motor Power Request")

# Grid (optional, easy to remove)
# plt.grid(True)

# Show the plot
plt.show()
