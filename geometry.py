from parser import protein, df
from math import sqrt


#dimension of the protein

print(df[["x", "y", "z"]].min())
print(df[["x", "y", "z"]].max())

#protein size
width = df["x"].max() - df["x"].min()
height = df["y"].max() - df["y"].min()
depth = df["z"].max() - df["z"].min()

print(width, height, depth)

#protein center
center = (
    df["x"].mean(),
    df["y"].mean(),
    df["z"].mean()
)
print(center)
print("\n")

#protein distance
def distance(atom1, atom2):
    dx = atom1["x"] - atom2["x"]
    dy = atom1["y"] - atom2["y"]
    dz = atom1["z"] - atom2["z"]
    return sqrt(dx**2 + dy**2 + dz**2)

print(distance(df.iloc[0], df.iloc[1]))

#protein bounding box
def bounding_box(df):
    return {
        "xmin": df["x"].min(),
        "xmax": df["x"].max(),
        "ymin": df["y"].min(),
        "ymax": df["y"].max(),
        "zmin": df["z"].min(),
        "zmax": df["z"].max(),
    }
print(bounding_box(df))