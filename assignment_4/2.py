"""
Reading a PDB file
"""

filename = "1PQS.pdb"

def pdb_file_to_Calpha_atoms(filename):
    file = open(filename, "r")
    alpha_atoms = []
    for line in file:
        if line.startswith("ENDMDL") or line.startswith("TER"):
            break
        if line.startswith("ATOM"):
            atomname = line[12:16]
            if "CA" in atomname:
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])
                alpha_atoms.append((x, y, z))
    file.close()
    return alpha_atoms

from math import sqrt


def distance(x, y):
    """
    Computes the Euclidean distance between point A and B.
    :param x: first point as a tuple of x,y,z coordinates
    :param y: second point as a tuple of x,y,z coordinates
    :return: distance
    """
    # Remember tuples index starts from 0
    return sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2 + + (x[2]-y[2])**2)


def length(path):
    """
    Computes length of path by calculating the distance between adjacent points.
    :param path: list of points as tuples of coordinates
    :return: length of path as the sum of Euclidean distances
    """
    result = 0
    for index in range(1, len(path)):
        result = result + distance(path[index-1], path[index])
    return result


backbone = pdb_file_to_Calpha_atoms(filename)
number_of_aminoacids = len(backbone)
predicted_length_of_backbone = 3.8 * number_of_aminoacids
length_of_backbone = length(backbone)
average_distance = length_of_backbone/number_of_aminoacids

print('Number of aminoacids:', number_of_aminoacids)
print('Predicted length of backbone: ', predicted_length_of_backbone, chr(197))
print('Measured length of backbone: ', length_of_backbone, chr(197))
print('Average distance between consecutive C alpha atoms:', average_distance, chr(197))
