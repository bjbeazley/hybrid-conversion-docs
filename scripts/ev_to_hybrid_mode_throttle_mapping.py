#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# EV throttle mapping
x1 = [0, 0.25, 1.0]
y1 = [-1.0, 0.0, 1.0]

# Hybrid throttle mapping
x2 = [0, 0.25, 1.0]
y2 = [-1.0, 0.0, 1.5]

# Create the plot
plt.figure()
plt.plot(x1, y1)
plt.plot(x2, y2)

# get the axis 
ax = plt.gca()

# enforce placement of x-axis at y=0
ax.spines['bottom'].set_position('zero')

# Hide the top spine
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ticks = np.arange(-1.0, 1.01, 0.25)
# ax.set_xticks(ticks)
ax.set_xticks([])
ax.set_yticks([])

# Labels and annotations
plt.text(0.03, -0.95, "100% regen", ha="left", va="bottom")
plt.text(0.98, 0.55, "Electric Motor Throttle Mapping", ha="right", va="top")
plt.text(0.93, 1.45, "Hybrid Throttle mapping", ha="right", va="top")

# Axis limits
plt.xlim(0, 1)
plt.ylim(-1, 1.5)

# Axis labels
plt.xlabel("Accelerator Position")
plt.ylabel("Motor Power Request")

# Grid (optional, easy to remove)
# plt.grid(True)

# Annotate ev to hybrid shift
plt.annotate("",
             xy=(0.6, 0.7),  # Point to (1.57, 1.0)
             xytext=(0.6, 0.48),    # Text location
             arrowprops=dict(arrowstyle="->", # Arrow style
                             color='red',     # Arrow color
                             lw=2),           # Line width
)
plt.annotate('EV to Hybrid', 
             xy=(0.7, 0.65),  # Point to (1.57, 1.0)
             xytext=(0.7, 0.7),    # Text location
             fontsize=12,
             ha='center') # Horizontal alignment of text

# Annotate hybrid to ev shift
plt.annotate("",
             xy=(0.8, 0.73),  # Point to (1.57, 1.0)
             xytext=(0.8, 1.08),    # Text location
             arrowprops=dict(arrowstyle="->", # Arrow style
                             color='red',     # Arrow color
                             lw=2),           # Line width
)
plt.annotate('Hybrid to EV', 
             xy=(0.0, 0.0),  # Point to (1.57, 1.0)
             xytext=(0.88, 1.0),    # Text location
             fontsize=12,
             ha='center') # Horizontal alignment of text

# Show the plot
plt.show()
