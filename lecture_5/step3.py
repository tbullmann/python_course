
seq1 = "BIERGARTEN"
seq2 = "STERNWARTE"


class matrix():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.values = list(list(0 for x in range(self.m)) for x in range(self.n))


    def show(self):
        for i in range(self.n):
            for j in range(self.m):
                print("{:4d}".format(self.values[i][j]), end='')
            print()


class alignement(matrix):
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        matrix.__init__(self, len(seq1) + 1, len(seq2) + 1)


values = alignement(seq1, seq2)
values.show()


