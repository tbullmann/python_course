#!/usr/bin/python3
def score(a, b):
	assert all([type(a) is str, type(b) is str, len(a) == 1, len(b) == 1])
	if a == b:
		return 1
	else:
		return 0

gap_penalty = -1

seq1 = "BIERGARTEN"
seq2 = "STERNWARTE"

m = len(seq1)+1
n = len(seq2)+1

values = list(list(0 for x in range(m)) for x in range(n))


def print_matrix(matrix):
	n = len(matrix)     # matrix = list of rows
	m = len(matrix[0])  # len of first row = number of columns
	print()
	for i in range(n):
		for j in range(m):
			print("{:4d}".format(matrix[i][j]), end='')
		print()
	print()


print_matrix(values)

#fill first row with gap penalty
for j in range(1,m):
	values[0][j] = values[0][j-1] + gap_penalty
	
#print matrix
print_matrix(values)
	
#fill first column with gap penalty
for i in range(1,n):
	values[i][0] = values[i-1][0] + gap_penalty

#print matrix
print_matrix(values)
	
#fill complete matrix
for j in range(1,m):
	for i in range(1,n):
		#calculate value
		values[i][j] = max([
			values[i-1][j] + gap_penalty,
			values[i][j-1] + gap_penalty,
			values[i-1][j-1] + score(seq1[j-1], seq2[i-1])
			])

#print matrix
print_matrix(values)

#perform traceback, upper way first
align1, align2, alignm = '', '', ''
i = n-1
j = m-1

def print_alignment(i,j,align1, align2, alignm):
    if i==0 and j==0:
        print(align1)
        print(alignm)
        print(align2)
    else:
        if values[i-1][j] + gap_penalty == values[i][j]:
            align1 = '-' + align1
            align2 = seq2[i-1] + align2
            alignm = ' ' + alignm
            print_alignment(i - 1, j, align1, align2, alignm)
        if values[i-1][j-1] + score(seq1[j-1], seq2[i-1]) == values[i][j]:
            align1 = seq1[j-1] + align1
            align2 = seq2[i-1] + align2
            alignm = ('|' if seq1[j-1] == seq2[i-1] else '*') + alignm
            print_alignment(i - 1, j - 1, align1, align2, alignm)
        if values[i][j-1] + gap_penalty == values[i][j]:
            align1 = seq1[j-1] + align1
            align2 = '-' + align2
            alignm = ' ' + alignm
            print_alignment(i, j - 1, align1, align2, alignm)

print_alignment(n-1, m-1, '','','')
