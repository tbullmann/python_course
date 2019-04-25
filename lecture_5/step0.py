
seq1 = "BIERGARTEN"
seq2 = "STERNWARTE"


m = len(seq1)+1
n = len(seq2)+1

# initialisiert matrix mit zeros
values = list(list(0 for x in range(m)) for x in range(n))

# show matrix
for row_index in range(n):
    for column_index in range(m):
        print("{:4d}".format(values[row_index][column_index]), end='')
    print()

