import gzip
import pandas as pd
#from Bio.PDB import PDBParser

#parser = PDBParser()

protein = {}

atoms = []
residues = set()
chains = set()
# Open the .gz file in text mode ('rt') and pass the handle to the parser
with gzip.open("1crn.pdb.gz", "rt") as f:
    for line in f:
        if line.startswith("ATOM"):
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