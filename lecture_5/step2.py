
seq1 = "BIERGARTEN"
seq2 = "STERNWARTE"

m = len(seq1)+1
n = len(seq2)+1

class matrix():
    def __init__(self, n, m):
        self.m = n
        self.n = m
        self.values = list(list(0 for x in range(self.m)) for x in range(self.n))


    def show(self):
        for i in range(self.n):
            for j in range(self.m):
                print("{:4d}".format(self.values[i][j]), end='')
            print()



values = matrix(m,n)
values.show()


