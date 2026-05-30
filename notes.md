# Molecular Visualizer Notes

## Current Goal

Build a protein/molecular visualizer from scratch.

Current focus:

1. Understand PDB files
2. Parse protein data
3. Build internal data structures
4. Prepare data for visualization

---

## Protein Hierarchy

Biological structure:

```text
Protein
 └── Chain
      └── Residue
           └── Atom
```

Example:

```text
Protein
 └── Chain A
      ├── Residue 1 (THR)
      │    ├── N
      │    ├── CA
      │    ├── C
      │    └── O
      │
      └── Residue 2 (THR)
```

---

## PDB ATOM Record

Example:

```text
ATOM      1  N   THR A   1      17.047  14.099   3.625
```

Meaning:

| Field | Meaning |
|---------|---------|
| 1 | Atom serial number |
| N | Atom name |
| THR | Residue name |
| A | Chain ID |
| 1 | Residue number |
| 17.047 | X coordinate |
| 14.099 | Y coordinate |
| 3.625 | Z coordinate |

---

## Parsed Atom Structure

```python
atom = {
    "serial_number": int(line[6:11].strip()),
    "atom_name": line[12:16].strip(),
    "residue_name": line[17:20].strip(),
    "chain_id": line[21].strip(),
    "residue_number": int(line[22:26].strip()),
    "x": float(line[30:38].strip()),
    "y": float(line[38:46].strip()),
    "z": float(line[46:54].strip())
}
```

Order mirrors the PDB file.

---

## Meaning of Fields

### serial_number

Unique atom identifier within the file.

Useful for:

- debugging
- atom selection
- bond records (CONECT)

Not required for basic rendering.

### atom_name

Examples:

```text
N
CA
C
O
CB
```

Specific atom within a residue.

### residue_name

Amino acid name.

Examples:

```text
THR
CYS
SER
GLY
ASN
```

### residue_number

Position of the amino acid within a chain.

Example:

```text
THR = residue 1
THR = residue 2
CYS = residue 3
```

### chain_id

Protein chain identifier.

Examples:

```text
A
B
C
```

### x, y, z

3D coordinates of the atom.

These coordinates are what will eventually be rendered.

---

## Current Data Structures

### Raw Atoms

```python
atoms = []
```

Stores every atom.

### Chains

```python
chains = set()
```

Stores unique chain identifiers.

### Residues

```python
residues = set()
```

Stores:

```python
(chain_id, residue_number)
```

Example:

```python
("A", 1)
("A", 2)
("A", 3)
```

### Protein Hierarchy

```python
protein = {}
```

Structure:

```python
{
    "A": {
        1: [atom, atom, atom],
        2: [atom, atom],
        3: [atom, atom]
    }
}
```

Represents:

```text
Protein
 └── Chain A
      ├── Residue 1
      ├── Residue 2
      └── Residue 3
```

---

## Pandas Table

Master table:

```python
df = pd.DataFrame(atoms)
```

Columns:

```text
serial_number
atom_name
residue_name
chain_id
residue_number
x
y
z
```

Example:

| serial_number | atom_name | residue_name | chain_id | residue_number | x | y | z |
|--------------|------------|---------------|----------|----------------|------|------|------|
| 1 | N | THR | A | 1 | 17.047 | 14.099 | 3.625 |

Current purpose:

- inspect data
- filter atoms
- summarize protein contents
- verify parser output

---

## Project Architecture

```text
PDB File
    ↓
Parser
    ↓
Atom Records
    ↓
Data Structures
    ↓
DataFrame
    ↓
Geometry
    ↓
Rendering
    ↓
Visualization
```

Current position:

DataFrame stage.

---

## Next Steps

- Learn basic pandas querying
- Calculate protein dimensions
- Compute atom-to-atom distances
- Create geometry objects
- Render atoms as spheres
- Build first 3D viewer