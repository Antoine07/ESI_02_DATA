import pandas as pd
import numpy as np

names1880 = pd.read_csv('./names/yob1880.txt', names=['name', 'sex', 'birth'])

# print(names1880.head(2))

"""
2. Donnez le nombre de naissances par sex pour l'année 1880.
"""

grouped = names1880.groupby('sex')['birth']
print(grouped.sum())

"""
3. Créez un script permettant de récupérer les prénons de 1880 à 2018 à partir des fichiers du dossier names et utiliser la méthode concat pour les rassembler.
""" 

columns = ['names', 'sex', 'birth']
yobs = []

for year in range(1880, 2019):
    path = f'./names/yob{year}.txt'
    df = pd.read_csv(path, names=columns)
    df['year'] = year
    yobs.append(df)

# voir au niveau des index
names = pd.concat(yobs, ignore_index=True)

print( names.head(2) )

"""
4. Agrégez les données pour avoir deux colonnes F et M. Et faites la sommes des naissances par sex et year. Vous pouvez utiliser la méthode pivot_table
"""