
seq1 = "BIERGARTEN"
seq2 = "STERNWARTE"


m = len(seq1)+1
n = len(seq2)+1

# initialisiert matrix mit zeros
values = []
for row_index in range(n):
    row = []
    for column_index in range(m):
        row.append(0)
    values.append(row)

print(values)
