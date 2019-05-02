
seq1 = "BIERGARTEN"
seq2 = "STERNWARTE"


class matrix():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.values = list(list(0 for x in range(self.m)) for x in range(self.n))


    def show(self):
        print()
        for i in range(self.n):
            for j in range(self.m):
                print("{:4d}".format(self.values[i][j]), end='')
            print()
        print()
        return ""


class alignement(matrix):
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        matrix.__init__(self, len(seq1) + 1, len(seq2) + 1)


class dotplot(alignement):

    def score(self, a, b):
        if a == b:
            return 1
        else:
            return 0

    def fill(self):
        for i in range(1, self.n):
            for j in range(1, self.m):
                if self.score(self.seq1[i - 1], self.seq2[j - 1]) == 1:
                    self.values[i][j] = self.values[i-1][j-1] + 1


values = dotplot(seq1, seq2)
values.fill()
values.show()


