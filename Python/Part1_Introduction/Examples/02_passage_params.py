def g(*t):
	return t

# ça permet de récupérer des paramètres variables sous forme de tuple ( structure de données )
# (1, 2, 3)
print( g(1, 2, 3) )

def h(**t):
    return t 

# retourne un dictionnaire 
# {'a': 1, 'b': 2, 'c': 3}
print( h(a=1, b=2, c=3) )
