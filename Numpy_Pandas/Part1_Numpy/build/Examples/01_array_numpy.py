import numpy as np 

# définit un type composite 
dt = np.dtype([
    ('name', np.dtype('U14')), ('grades', np.float64) 
])

dataset = np.array([
      ( "Luce du Coulon" , 12.5),
      ( "Auguste Dupont", 8.5),
      ( "Roger Le Voisi", 1.5)
], dtype=dt)


print(dataset[0])
print(dataset[0]['name'])
print(dataset[0]['grades'])

# Création d'un tableau 2 lignes 8 colonnes que de 1
t = np.ones((2,8), dtype='int8')
print(t)

# Nombre de dimension(s), ici 2
t.ndim
print(t.ndim)

# Forme du tableau (2,8)
t.shape

# taille du tableau 16 valeurs
t.size

# type du tableau int8
t.dtype

a = np.array([[1,2], [2, 3]])

a[0, 1] = 1_000_000_000

print(a)

u = np.array([1, 100, 2], dtype='float64')
u[1] = np.nan

print(u)