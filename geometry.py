#geometry.py
from parser import df, atoms
from math import sqrt


#dimension of the protein

#print(df[["x", "y", "z"]].min())
#print(df[["x", "y", "z"]].max())

#protein size
width = df["x"].max() - df["x"].min()
height = df["y"].max() - df["y"].min()
depth = df["z"].max() - df["z"].min()

#print(width, height, depth)

#protein center
center = (
    df["x"].mean(),
    df["y"].mean(),
    df["z"].mean()
)
#print(center)
#print("\n")

#protein distance
    # Euclidean distance between two atoms.
    # Coordinates are measured in Angstroms (Å).
    # Distance formula:
        # d = sqrt(
        #     (x2-x1)^2 +
        #     (y2-y1)^2 +
        #     (z2-z1)^2
        # )
    # Used for:
        # - bond detection
        # - neighbor searches
        # - molecular measurements
        # - spatial analysis
def distance(atom1, atom2):
    dx = atom1["x"] - atom2["x"]
    dy = atom1["y"] - atom2["y"]
    dz = atom1["z"] - atom2["z"]
    return sqrt(dx**2 + dy**2 + dz**2)

#print(distance(df.iloc[0], df.iloc[1]))

#protein bounding box
    # Axis-aligned bounding box.
        # Returns the minimum and maximum coordinates occupied by the protein.
    # Future uses:
        # - camera placement
        # - zoom limits
        # - spatial partitioning
        # - scene centering
def bounding_box(df):
    return {
        "xmin": df["x"].min(),
        "xmax": df["x"].max(),
        "ymin": df["y"].min(),
        "ymax": df["y"].max(),
        "zmin": df["z"].min(),
        "zmax": df["z"].max(),
    }
#print(bounding_box(df))

#bonds
    # Simple bond detection.
    # Current method:
        # Two atoms are considered bonded if:
            # distance(atom1, atom2) <= max_distance
    # This is a visualization heuristic only.
    # Default cutoff: 2.0 Å Why? Most covalent bonds are roughly:
        # C-H ≈ 1.1 Å
        # C-C ≈ 1.5 Å
        # C-N ≈ 1.5 Å
        # C-O ≈ 1.4 Å
        # S-S ≈ 2.0 Å
    # Limitations:
        # - ignores atom type
        # - ignores chemistry
        # - may create false bonds
        # - may miss unusual bonds
    # Professional molecular viewers typically use:
        # 1. Explicit CONECT records from PDB files
        # 2. Covalent radii:
        #    bond if
        #
        #    distance <
        #    radius(atom1) +
        #    radius(atom2) +
        #    tolerance

        # 3. Chemical topology information
        # 4. Force-field or structure-derived bonding
    # Future:
    # Replace fixed cutoff with covalent-radius based bonding.
def find_bonds(atoms, max_distance=2.0):
    bonds = []

    for i in range(len(atoms)):
        for j in range(i + 1, len(atoms)):

            d = distance(atoms[i], atoms[j])

            if d <= max_distance:
                bonds.append((i, j))

    return bonds

bonds = find_bonds(atoms)
print(len(bonds))
print(bonds[:10])

