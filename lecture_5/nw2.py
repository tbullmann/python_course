#!/usr/bin/python3
GAP_PENALTY = -8
AA_INDICES = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
BLOSUM62 = [
	[4], # Ala
	[-1, 5], # Arg
	[-2, 0, 6], # Asn
	[-2, -2, 1, 6], #Asp
	[0, -3, -3, -3, 9], # Cys
	[-1, 1, 0, 0, -3, 5], # Gln
	[-1, 0, 0, 2, -4, 2, 5], # Glu
	[0, -2, 0, -1, -3, -2, -2, 6], # Gly
	[-2, 0, 1, -1, -3, 0, 0, -2, 8], # His
	[-1, -3, -3, -3, -1, -3, -3, -4, -3, 4], # Ile
	[-1, -2, -3, -4, -1, -2, -3, -4, -3, 2, 4], # Leu
	[-1, 2, 0, -1, -3, 1, 1, -2, -1, -3, -2, 5], # Lys
	[-1, -1, -2, -3, -1, 0, -2, -3, -2, 1, 2, -1, 5], #Met
	[-2, -3, -3, -3, -2, -3, -3, -3, -1, 0, 0, -3, 0, 6], # Phe
	[-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4, 7], # Pro
	[1, -1, 1, 0, -1, 0, 0, 0, -1, -2, -2, 0, -1, -2, -1, 4], # Ser
	[0, -1, 0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1, 1, 5], # Thr
	[-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1, 1, -4, -3, -2, 11], # Trp
	[-2, -2, -2, -3, -2, -1, -2, -3, 2, -1, -1, -2, -1, 3, -3, -2, -2, 2, 7], # Tyr
	[0, -3, -3, -3, -1, -2, -2, -3, -3, 3, 1, -2, 1, -1, -2, -2, 0, -3, -1, 4] # Val
]

def score(a, b):
	assert all([type(a) is str, type(b) is str, len(a) == 1, len(b) == 1])
	index1, index2 = 0, 0
	for i in range(len(AA_INDICES)):
		if AA_INDICES[i] == a:
			index1 = i
			break
	for j in range(len(AA_INDICES)):
		if AA_INDICES[j] == b:
			index2 = j
			break
	
	if index1 < index2:
		index1, index2 = index2, index1
	
	return BLOSUM62[index1][index2]

"""
seq1 = ("GSELRSIAFSRAVFAEFLATLLFVFFGLGSALNWPQALPSVLQIAMAFGLGIGTLVQALGHISGAHINPAVTVACLVGCH"
	"VSVLRAAFYVAAQLLGAVAGAALLHEITPADIRGDLAVNALSNSTTAGQAVTVELFLTLQLVLCIFASTDERRGENPGTP"
	"ALSIGFSVALGHLLGIHYTGCSMNPARSLAPAVVTGKFDDHWVFWIGPLVGAILGSLLYNYVLFPPAKSLSERLAVLKGL"
	"EP")
seq2 = ("SHVMWELRSIAFSRAVFAEFLATLLFVFFGLGSALNWPQALPSVLQIAMAFGLGIGTLVQALGHISGAHINPAVTVACLV"
	"GCHVSVLRAAFYVAAQLLGAVAGAALLHEITPADIRGDLAVNALSNSTTAGQAVTVELFLTLQLVLCIFASTDERRGENP"
	"GTPALSIGFSVALGHLLGIHYTGCSMNPARSLAPAVVTGKFDDHWVFWIGPLVGAILGSLLYNYVLFPPAKSLSERLAVL"
	"KGLEPDTDWEEREVRRRQAVELHSPQSLPRGTKA")
"""

seq1 = ("MSKKEVCSVAFLKAVFAEFLATLIFVFFGLGSALKWPSALPTILQIALAFGLAIGTLAQALGPVSGGHINPAITLALLVG"
	"NQISLLRAFFYVAAQLVGAIAGAGILYGVAPLNARGNLAVNALNNNTTQGQAMVVELILTFQLALCIFASTDSRRTSPVG"
	"SPALSIGLSVTLGHLVGIYFTGCSMNPARSFGPAVVMNRFSPAHWVFWVGPIVGAVLAAILYFYLLFPNSLSLSERVAII"
	"KGTYEPDEDWEEQREERKKTMELTTR") # 3d9s:a
seq2 = ("QAFWKAVTAEFLAMLIFVLLSLGSTINWGGTEKPLPVDMVLISLCFGLSIATMVQCFGHISGGHINPAVTVAMVCTRKIS"
	"IAKSVFYIAAQCLGAIIGAGILYLVTPPSVVGGLGVTMVHGNLTAGHGLLVELIITFQLVFTIFASCDSKRTDVTGSIAL"
	"AIGFSVAIGHLFAINYTGASMNPARSFGPAVIMGNWENHWIYWVGPIIGAVLAGGLYEYVFCP") # 3gd8:a

m = len(seq1)+1
n = len(seq2)+1

values = list(list(0 for x in range(m)) for x in range(n))
	
#fill first row with gap penalty
for j in range(1,m):
	values[0][j] = values[0][j-1] + GAP_PENALTY
		
#fill first column with gap penalty
for i in range(1,n):
	values[i][0] = values[i-1][0] + GAP_PENALTY
	
#fill complete matrix
for j in range(1,m):
	for i in range(1,n):
		#calculate value
		v1 = values[i-1][j] + GAP_PENALTY
		v2 = values[i][j-1] + GAP_PENALTY
		v3 = values[i-1][j-1] + score(seq1[j-1], seq2[i-1])
		values[i][j] = max([v1, v2, v3])


#perform traceback, upper way first
align1, align2, alignm = '', '', ''
i = n-1
j = m-1
while i > 0 or j > 0:
	if values[i-1][j] + GAP_PENALTY == values[i][j]:
		align1 = '-' + align1
		align2 = seq2[i-1] + align2
		alignm = ' ' + alignm
		i = i - 1
	elif values[i-1][j-1] + score(seq1[j-1], seq2[i-1]) == values[i][j]:
		align1 = seq1[j-1] + align1
		align2 = seq2[i-1] + align2
		alignm = ('|' if seq1[j-1] == seq2[i-1] else '*') + alignm
		i = i - 1
		j = j - 1
	elif values[i][j-1] + GAP_PENALTY == values[i][j]:
		align1 = seq1[j-1] + align1
		align2 = '-' + align2
		alignm = ' ' + alignm
		j = j - 1
	else:
		print("path broken")
		break

print(align1)
print(alignm)
print(align2)
