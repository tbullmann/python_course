



seq1 = "BIERGARTEN"
seq2 = "STERNWARTE"

m = len(seq1)+1
n = len(seq2)+1

zeros = list(0 for x in range(m))
values = list(zeros for x in range(n))


line = "    "
for j in range(m):
    if j == 0:
        line += "   ."
    else:
        line += "   " + seq1[j-1]
print(line)

for i in range(n):
    if i == 0:
        line = "   ."
    else:
        line = "   " + seq2[i-1]
    for j in range(m):
        line += "{:4d}".format(values[i][j])
    print(line)







