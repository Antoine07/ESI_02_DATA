
matrix = [
	[1,2,3], # i = 0 
	[4,5,6], # i = 1
	[7,8,9],  # i = 2
    [10, 11, 12]  # i = 3
]


t = [ [ matrix[i][0]for i in range(0, len(matrix)) ] for j in range(0, len(matrix[0])) ]
print(t)

t = [ [ matrix[i][j]for i in range(0, len(matrix)) ] for j in range(0, len(matrix[0])) ]

print(t)


print("-----")

t = []
# trois colonnes fixes à parcourir
for i in range(0, len(matrix[0])) :
	# pour chaque ligne 
	r = []
	# on parcour le nombre de lignes 
	for j in range(0, len(matrix)):
		r.append( matrix[j][i] )

	t.append(r)

print(t)
