import pandas as pd
import numpy as np

data = {
    'city': ['Lille', 'Paris', 'Lyon', 'Marseille', 'Aubenas'],
    'year': [2000, 2001, 2002, 2001, 2020],
    'pop': [0.232, 2.141, np.nan, 0.861, 0.012]
}

df = pd.DataFrame(data, index=['59', '75', '69', '13', '07'])

print(df)

# accéder à la colonne
# dataFrame
print(type( df[ ['city'] ]) )
# series
print(type( df['city' ]) )

print(df[ df['pop'] > 0.5 ])
# dataFrame
print(type( df[ df['pop'] > 0.5 ]))

print("--------------------------")
# les lignes pour slicing 
print(df[0:2])

print("--------------------------")
# syntaxe pour agir sur les lignes et les colonnes
print( df.loc['75':'07'] )
# pour les index et colonnes
print( df.loc['75':'07', 'city':'year'] )

print("----------------------------")
# slicing avec des valeurs numériques 
print(df.iloc[1:, 1:])