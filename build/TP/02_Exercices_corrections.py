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

# les axes sont directement liés aux de dimension de la matrice 0 : colonnes;  1 : lignes
sanitize = np.apply_along_axis(lambda l : [ "".join( set(e) ) for e in l ], 1, a) 

print(sanitize)


"""
3 Exercice formater/extraire des données

1. Développez un script permettant de nettoyer le dataset students pour obtenir le tableau sanitize :

"""

students = np.array([
    [  "Name: Luce du Coulon" , "phone: 201-20-30"],
    [  "Name: Auguste Dupont", "phone: 201-22-30"],
    [  "Name: Roger Le Voisi", "phone: 201-27-30"],
    [  "Name: Alexandre Lacri", "phone: 201-10-30"],
    [  "Name: Jacques Humber", "phone: 201-20-35"],
    [  "Name: Thérèse Guille", "phone: 201-20-38"],
    [  "Name: Gilles Gros-Bodin", "phone: 201-20-39"],
    [  "Name: Amélie Pires", "phone: 201-25-39"],
    [  "Name: Marcel Laporte", "phone: 201-20-39"],
    [  "Name: Geneviève Marchal", "phone: 301-20-39"]
])

# Un lambda pour nettoyer les données ( mettre les données conforme à un type )
tranform_str =  lambda s : [ 
    s[0].replace('Name: ', '') , 
    s[1].replace('phone: ', '')
]

sanitize_students = np.apply_along_axis(tranform_str, 1, students ) 
print(sanitize_students)

print("----------------------------------------------------------")
# Deuxième approche

students = np.array([
    [  "Name: Luce du Coulon" , "phone: 201-20-30"],
    [  "Name: Auguste Dupont", "phone: 201-22-30"],
    [  "Name: Roger Le Voisi", "phone: 201-27-30"],
    [  "Name: Alexandre Lacri", "phone: 201-10-30"],
    [  "Name: Jacques Humber", "phone: 201-20-35"],
    [  "Name: Thérèse Guille", "phone: 201-20-38"],
    [  "Name: Gilles Gros-Bodin", "phone: 201-20-39"],
    [  "Name: Amélie Pires", "phone: 201-25-39"],
    [  "Name: Marcel Laporte", "phone: 201-20-39"],
    [  "Name: Geneviève Marchal", "phone: 301-20-39"]
])

def myFormat(v):

    if 'Name: ' in v:
        return  v.replace('Name: ', '')
    elif 'phone: ' in v:
        return  v.replace('phone: ', '')
    else:
        return v


vfuncFormat = np.vectorize(myFormat)

sanitize_students =  vfuncFormat(students)

# une autre syntaxe possible : sanitize_students = np.vectorize(myFormat)(students)

"""
2. Comptez maintenant le nombre du numéro comportant le nombre 30.
Pour ce faire vous pouvez créer ce que l'on appelle un mask, c'est à dire parcourir le tableau et tester si le pattern "30" est présent dans la chaîne. Le mask devra avoir la même dimension que votre tableau. Une fois celui-ci en place vous pourrez alors l'appliquer de la manière suivante :
"""

def count_pattern(l, pattern):
    count = 0
    for e in l:
        if pattern in e :
            count += 1

    return count

# Nombre de ligne ayant le pattern recherché
print(count_pattern(sanitize_students[:,1], "30"))

print(sanitize_students)