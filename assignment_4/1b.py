"""
Solution to 1)
"""


def read_concat_sequences(filename):
    """
    Read all sequences from FASTA file into single string.
    :param filename: path to FASTA file
    :return: a string containing the concatenated sequences
    """
    fasta_file = open(filename)
    sequences = ""                      # Initialize empty sequence
    for line in fasta_file:
        line = line.replace("\r", "").replace("\n", "")  # Remove carriage return and newline
        if line.startswith(">"):
            pass                        # Ignore annotation after ">"
        elif line.startswith(";"):
            pass                        # Ignore chain information after ";"
        else:
            sequences += line           # Append sequence with line
    fasta_file.close()
    return sequences


one_letter_code = set('ARNDBCEQZGHILKMFPSTWYV')


def probability_letters(sequence, alphabet=one_letter_code):
    """
    Counting the number of occurrences of a letter in a given
    alphabet and returning the probability for each letter.
    :param sequence: string of letters
    :param alphabet: an unordered set of letters, default is the one letter code for aminoacids
    :return:
    """
    count = {}
    length = len(sequence)
    for letter in alphabet:
        count[letter] = sequence.count(letter) / length
    return count


# Read sample and compute aminoacid probabilities
sample_filename = '3IZ0.fasta.txt'
sample = read_concat_sequences(sample_filename)
aminoacid_probabilities = probability_letters(sample)

# Print table nicely
for aminoacid, probability in aminoacid_probabilities.items():
    print(aminoacid, ": %1.3f" % (probability * 100), '%')

