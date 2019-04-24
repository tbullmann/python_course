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

#print matrix
for i in range(n):
	for j in range(m):
		print(values[i][j],"\t", end='')
	print()
	
#fill first row with gap penalty
for j in range(1,m):
	values[0][j] = values[0][j-1] + gap_penalty
	
#print matrix
print()
for i in range(n):
	for j in range(m):
		print(values[i][j],"\t", end='')
	print()
	
#fill first column with gap penalty
for i in range(1,n):
	values[i][0] = values[i-1][0] + gap_penalty

#print matrix
print()
for i in range(n):
	for j in range(m):
		print(values[i][j],"\t", end='')
	print()
	
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
print()
for i in range(n):
	for j in range(m):
		print(""values[i][j],"\t", end='')
	print()

#perform traceback, upper way first
align1, align2, alignm = '', '', ''
i = n-1
j = m-1
while i > 0 or j > 0:
	if values[i-1][j] + gap_penalty == values[i][j]:
		print("up", end=" ")
		align1 = '-' + align1
		align2 = seq2[i-1] + align2
		alignm = ' ' + alignm
		i = i - 1
	elif values[i-1][j-1] + score(seq1[j-1], seq2[i-1]) == values[i][j]:
		print("left up", end=" ")
		align1 = seq1[j-1] + align1
		align2 = seq2[i-1] + align2
		alignm = ('|' if seq1[j-1] == seq2[i-1] else '*') + alignm
		i = i - 1
		j = j - 1
	elif values[i][j-1] + gap_penalty == values[i][j]:
		print("left", end=" ")
		align1 = seq1[j-1] + align1
		align2 = '-' + align2
		alignm = ' ' + alignm
		j = j - 1
	else:
		print("path broken")
		break
print()

print(align1)
print(alignm)
print(align2)
