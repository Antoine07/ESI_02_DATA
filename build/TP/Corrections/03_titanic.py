import pandas as pd
import numpy as np

from main import titanic_data

# print(titanic_data.head(5))

"""

Vous êtes responsable de la gestion des données pour une entreprise. Mettez en place le processus de traitement des données.

1. Combien de femme de moins de 18 ont survécu

2. Parmi ces femmes (question 1) déterminer la répartition par classe sur le bateau.

3. Déterminer si le port d'embarquemen a une influence sur la survie (calculer la répartiti  des morts et des survivants en fonction du port de départ)

4. Déterminer la répartition par sexe et par âge (faites des tranches ) des passagers du navire.

- 0 < 18

- 18 - 59

- 60 ...

Model de données
    "sex"
    "class" 
    "age" 
    "survived"
    "embarked"

"""

# afficher le nom des colonnes
# print(titanic_data.columns.values)

# renommer les colonnes et modifier le dataFrame avec inplace=True
titanic_data.rename(
    columns={"Survived" : "survived", "Sex" : "sex", "Pclass" : "class", "Age" : "age", "Embarked" : "embarked"}, 
    inplace=True
)

# garder que certaines colonnes 
# titanic_data = titanic_data[ ["survived", "sex", "class", "age", "embarked"]]

# print(titanic_data)

mask = (titanic_data["age"] < 18) & (titanic_data["sex"] == "female") & (titanic_data["survived"] == 1)
# 1. Combien de femme de moins de 18 ont survécu
totalFemale = sum( mask )
print(f"Nombre de femme de moins de 18 ans ayant survécus: {totalFemale }")

# 2. Parmi ces femmes (question 1) déterminer la répartition par classe sur le bateau.
groupClass = titanic_data [ (titanic_data["age"] < 18) & (titanic_data["sex"] == "female") ].groupby(by=['class'])

print(f"Répartition des personnes qui ont survécu par class {round( groupClass[['survived']].sum() / totalFemale, 2 ) * 100} %")

# 3. Déterminer si le port d'embarquement a une influence sur la survie (calculer la répartition des morts et des survivants en fonction du port de départ)

groupEmbarked = titanic_data.groupby(by=['embarked'])

# répartition du nombre de survivant par port 
print( groupEmbarked[['survived']].sum().sort_values(by="survived") )

# 4. Déterminer la répartition par sexe et par âge (faites des tranches ) des passagers du navire.

bins = [0, 18, 59, 81]

# # Définir les étiquettes des tranches d'âge
labels = ['0-18', '19-59', '60-81']

titanic_data['bins age'] = pd.cut(titanic_data['age'], bins=bins , labels=labels, right=False) 

groupBinsAge = titanic_data.groupby(by=['bins age', 'sex'])

print(groupBinsAge[['survived']].sum())