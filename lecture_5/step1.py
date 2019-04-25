
seq1 = "BIERGARTEN"
seq2 = "STERNWARTE"

m = len(seq1)+1
n = len(seq2)+1


def init(m, n):
    values = list(list(0 for x in range(m)) for x in range(n))
    return(values)


def show(values, m, n):
    print()
    for i in range(n):
        for j in range(m):
            print("{:4d}".format(values[i][j]), end='')
        print()
    print()

values = init(m,n)
show(values, m, n)