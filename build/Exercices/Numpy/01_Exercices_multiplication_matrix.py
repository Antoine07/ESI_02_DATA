import numpy as np 

"""
Exercice Multipliez les deux a et b les deux matrices suivantes entres elles, respectivement terme à terme en respectant les dimensions
"""

a = np.array([[1,2,3], [4,5,6]])
b = np.array([[10,20,30], [41,51,61], [72, 73, 83]])

"""
NB de colonnes de la première == NB de ligne de la deuxième matrice

a -> 3 colonnes et b -> 3 lignes

1 2 3    10 20 30
4 5 6    41 51 61
         72 73 83

1*10 + 2*41 + 3*72 =  308
1*20 + 2*51 + 3*73 =  341
1*30 + 2*61 + 3*83 =  401

--- deuxième ligne

4*10 + 5*41 + 6*72 =  677
4*20 + 5*51 + 6*73 =  773
4*30 + 5*61 + 6*83 =  923

"""

print( np.dot( a, b ) )