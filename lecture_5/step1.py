
seq1 = "BIERGARTEN"
seq2 = "STERNWARTE"

m = len(seq1)+1
n = len(seq2)+1


def init(n, m):
    values = list(list(0 for x in range(m)) for x in range(n))
    return(values)


def show(values, n, m):
    for i in range(n):
        for j in range(m):
            print("{:4d}".format(values[i][j]), end='')
        print()


values = init(m,n)
show(values, m, n)