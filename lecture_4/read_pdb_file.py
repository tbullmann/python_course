"""
Reading a PDB file and print atom coordinates
"""

file = open("1PQS.pdb", "r")

for line in file:
    if line.startswith("ENDMDL") or line.startswith("TER"):
        break
    if line.startswith("ATOM"):
        atomname = line[12:16]
        resname = line[17:20]
        resseq = int(line[22:26])
        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])
        print(atomname, resname, resseq, x, y, z)

file.close()
