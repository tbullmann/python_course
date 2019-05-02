
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
        print(seq1)
        print(seq2)
        matrix.__init__(self, len(seq1) + 1, len(seq2) + 1)


class needlemann_wunsch(alignement):
    def __init__(self, seq1, seq2):
        alignement.__init__(self, seq1, seq2)
        self.gap_penalty = -1
        for i in range(1,self.n):
            self.values[i][0] = self.values[i-1][0] + self.gap_penalty
        for j in range(1,self.m):
            self.values[0][j] = self.values[0][j-1] + self.gap_penalty


    def score(self, a, b):
        if a == b:
            return 1
        else:
            return 0

    def fill(self):
        for i in range(1, self.n):
            for j in range(1, self.m):
                self.values[i][j] = max([
                    self.values[i-1][j] + self.gap_penalty,
                    self.values[i][j-1] + self.gap_penalty,
                    self.values[i-1][j-1] + self.score(self.seq1[i - 1], self.seq2[j - 1])
                ])

    def traceback(self):
        self.print_alignment(self.n-1, self.m-1,'','','')

    def print_alignment(self, i, j, align1, align2, alignm):
        if i == 0 and j == 0:
            print(align1)
            print(alignm)
            print(align2)
        else:
            if self.values[i - 1][j - 1] + self.score(self.seq1[i - 1], self.seq2[j - 1]) == self.values[i][j]:
                self.print_alignment(i - 1,
                                     j - 1,
                                     self.seq1[i - 1] + align1,
                                     self.seq2[j - 1] + align2,
                                     ('|' if seq1[i - 1] == seq2[j - 1] else '*') + alignm)

            if self.values[i - 1][j] + self.gap_penalty == self.values[i][j]:
                self.print_alignment(i - 1,
                                     j,
                                     self.seq1[i - 1] + align1,
                                     '-' + align2,
                                     ' ' + alignm)

            if self.values[i][j - 1] + self.gap_penalty == self.values[i][j]:
                self.print_alignment(i,
                                     j - 1,
                                     '-' + align1,
                                     self.seq2[j - 1] + align2,
                                     ' ' + alignm)


values = needlemann_wunsch(seq1, seq2)
values.show()
values.fill()
values.show()
values.traceback()



