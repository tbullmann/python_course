

class matrix()
    def __init__(self, m, n):
        self.values = list(list(0 for x in range(m)) for x in range(n))

    def print_matrix(self):
        n = len(self.values)     # matrix = list of rows
        m = len(self.values[0])  # len of first row = number of columns
        print()
        for i in range(n):
            for j in range(m):
                print("{:4d}".format(matrix[i][j]), end='')
            print()
        print()

