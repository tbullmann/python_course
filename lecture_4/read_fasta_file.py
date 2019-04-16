"""
Reading a FASTA flat file into a dictionary
"""


def read_fasta(filename):
    """
    Read sequences from FASTA file into dictionary, ignoring chain information.
    :param filename: path to FASTA file
    :return: dictionary with annotations as key
    """
    fasta_file = open(filename)
    sequences = {}                         # Initialize empty dictionary
    for line in fasta_file:
        line = line.replace("\r","").replace("\n","")
        if line.startswith(">"):
            annotation = line[1:]          # Get annotation from the line after ">"
            sequences[annotation] = ""     # Start new sequence with this annotation
        elif line.startswith(";"):
            pass                           # Ignore chain information after ";"
        else:
            sequences[annotation] += line  # Append sequence with this annotation
    fasta_file.close()
    return sequences


fasta_filename = '3IZ0.fasta.txt'
all_sequences = read_fasta(fasta_filename)

for annotation, sequence in all_sequences.items():
    print(annotation, ':', sequence)
