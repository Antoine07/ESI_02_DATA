l = [1, 2, 3]


# passage par référence
m = l
m[0] = 100

# question qu'affiche ces deux prints ?
print(m)
print(l)

# Affiche la même chose ( passage par référence )
# Pour faire une copie peu profonde 
r = l[:]
r[0] = 200

print(r)
print(l)

# Attention les : ne font pas de copy profonde 
# des référence dans des références 
p = [[0,1], [2, 3], [4, 5]] 

# shallow copy 
q = p [:]

q[0][0] = 200

print(p)
print(q)

print('---------------')

# Copy profonde

t = []
for el in p:
    # compréhension de liste (syntaxe propre à Python)
    t.append( el[:] )

t[0][0] = 400
print(p)
print(t)

