"""
Result for 2)
"""


def Hamming_distance(seq1, seq2):
    """
    Calculate the hamming distance between two sequences.
    :param seq1: list of values or string (which is a list of chars)
    :param seq2: list of values or string (which is a list of chars)
    :return: number of non-identical elements
    """
    length1 = len(seq1)
    length2 = len(seq2)
    if length1 != length2:
        print("Cannot compute Hamming distance for two sequences with non-matching lengths!")
        return None
    else:
        result = 0
        for index in range(length1):
            if seq1[index] != seq2[index]:
                result += 1
        return result


s1 = 'ATGC'
s2 = 'AGTC'
s3 = 'ATG'

print('Testing the function...')
print('Hamming distance between', s1, 'and', s1, 'is', Hamming_distance(s1, s1))
print('Hamming distance between', s1, 'and', s2, 'is', Hamming_distance(s1, s2))
print('Hamming distance between', s1, 'and', s3, 'is', Hamming_distance(s1, s3))
