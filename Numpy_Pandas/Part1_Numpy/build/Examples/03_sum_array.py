import numpy as np 

# deux dimensions 0, 1 
a = np.array([
    [5, 5, 1, 6, 5],
    [7, 7, 8, 9, 6],
    [1, 7, 2, 4, 5],
    [3, 4, 7, 0, 8],
    [1, 8, 2, 0, 2]
])


# la somme de chaque ligne 
print( a.sum(1) )

# la somme de chaque colonne 
print( a.sum(0) )

# Somme totale de toutes les valeurs 
print(a.sum())

print(a.sum(0).sum(0))