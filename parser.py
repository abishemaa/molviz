import gzip
import pandas as pd
#from Bio.PDB import PDBParser

#parser = PDBParser()

# Protein hierarchy:
#
# Protein
#   └── Chain
#         └── Residue
#               └── Atom
#
# Internal representation:
#
# {
#     "A": {
#         1: [atom, atom, atom],
#         2: [atom, atom]
#     }
# }
protein = {}

atoms = []
residues = set()
chains = set()
# Open the .gz file in text mode ('rt') and pass the handle to the parser
with gzip.open("1crn.pdb.gz", "rt") as f:
    for line in f:
        if line.startswith("ATOM"):
            # PDB ATOM record parser.
            # PDB files use fixed-width columns rather than delimiters.
                # Example: ATOM      1  N   THR A   1      17.047  14.099   3.625
            # Fields currently parsed:
                # - serial_number: unique atom identifier in file
                # - atom_name: atom type within residue (N, CA, C, O, ...)
                # - chain_id: protein chain identifier
                # - residue_name: amino acid name (THR, CYS, GLY, ...)
                # - residue_number: residue position within chain
                # - x,y,z: atom coordinates in Angstroms (Å)
            # Fields NOT yet parsed:
                # - occupancy
                # - B-factor (temperature factor)
                # - element symbol
                # - charge
                # - alternate locations
                # - insertion codes
            # Future:Parse additional fields for more accurate molecular modeling.
            atom = {
                "serial_number": int(line[6:11].strip()),
                "atom_name": line[12:16].strip(),

                "chain_id": line[21].strip(),
                "residue_name": line[17:20].strip(),
                "residue_number": int(line[22:26].strip()),

                "x": float(line[30:38].strip()),
                "y": float(line[38:46].strip()),
                "z": float(line[46:54].strip())
            }
            atoms.append(atom)
            chains.add(atom["chain_id"])
            residues.add((atom["chain_id"], atom["residue_number"]))

            chain = atom["chain_id"]
            if chain not in protein:
                protein[chain] = {}

            residue = atom["residue_number"]
            if residue not in protein[chain]:
                protein[chain][residue] = []

            protein[chain][residue].append(atom)

    df = pd.DataFrame(atoms)
    #print(df, "\n")

    #print(df.iloc[[1]])

    #print(protein.keys())
    #print(len(protein["A"]))
    #print(protein["A"][1])
    #print(atom)
    #print(f"Total atoms: {len(atoms)}")
    #print(f"Total chains: {len(chains)}")
    #print(f"Total residues: {len(residues)}")
    #print(f"resiidue_names: {set(a['residue_name'] for a in atoms)}")
    #chains = set(a["chain_id"] for a in atoms)
    #print(f"Chains: {chains}")
    #residues = set(
    #(a["chain_id"], a["residue_number"])
    #    for a in atoms
    #)
    #print(f"Residues: {residues}")