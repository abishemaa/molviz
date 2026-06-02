# viewer.py

from parser import df
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
# Simple atom coloring.
# Convention:
    # Carbon   -> black
    # Nitrogen -> blue
    # Oxygen   -> red
    # Sulfur   -> yellow
# Future: Use standard CPK coloring scheme.
colors = []

for atom in df["atom_name"]:
    if atom.startswith("C"):
        colors.append("black")
    elif atom.startswith("N"):
        colors.append("blue")
    elif atom.startswith("O"):
        colors.append("red")
    elif atom.startswith("S"):
        colors.append("yellow")
    else:
        colors.append("gray")
# First visualization stage.
# Each atom is rendered as a single point.
# Representation:
    # Atom
    #   ↓
    # Point
# Future representations:
    # - point cloud
    # - ball-and-stick
    # - space-filling (CPK)
    # - ribbon/cartoon
    # - surface rendering
ax.scatter(
    df["x"],
    df["y"],
    df["z"],
    c=colors,
    s=20
)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()