import numpy as np
"""
1 Exercice minimum

Soit le tableau a suivant on cherche les valeurs minimales par ligne.

Nous aimerions à l'aide d'un script Python trouver tous les indices de tableau par ligne des minimaux et les enregistrer dans une liste de tuples comme dans l'exemple ci-dessous :

"""

a = np.array([
    [13, 22, 28, 66, 40],
    [16, 59, 37, 33, 28],
    [34, 98, 54, 48, 96],
    [13, 84, 93, 79, 76],
    [63, 50, 12, 69, 12]
])

# Résultat attendu une liste des minimaux et leur position sur chaque ligne
minTabLine = [(0, 13), (0, 16), (0, 34), (0, 13), (2, 12)]

# zip permet de rassembler les données dans un zip 
mins = zip( a.argmin(1), a.min(1) ) # générateur prends pas de place
# print(list( mins) ) # attention à la taille de vos données
for pos, m in mins:
    print(pos, m)


"""
2 Exercice éliminer les doublons

Dans le tableau suivant éliminer tous les doublons de lettres, voyez le tableau sanitize que nous aimerions avoir une fois votre script exécuté ci-dessous :

"""
a = np.array([
    ["aaabbfffhjik", "hhhkkkiooo", "hhjuuk"],
    ["rrrtttyyuuii", "rroooiiiuuu", "jjjhhhaa"],
    ["aaabbgghhh", "iiikkkooomml", "hhhiijjjuu"],
    ["hhhyyytttuu", "xxxnnnooii", "kkkjjjuuppp"],
    ["qqqfffgghhh", "qqqkkklll", "ooohhhjjj"],
])

sanitized = lambda l : [ "".join( set(e) ) for e in l ]

"""
def sanitized(l):

    return [ "".join( set(e) ) for e in l ]
"""

sanitize = np.apply_along_axis(sanitized, 1, a) 
print(sanitize[0][0])