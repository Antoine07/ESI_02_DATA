"""
1. Reprenez le dataset suivant et donnez le nombre d'enfant(s) par ville dans un tableau à deux colonnes **city** & **num_children**.

2. Quel est l'écart des ages des habitants par ville ?

3. Est-ce que les femmes mariées ont plus d'enfant que les hommes divorcés ?

4. Quelle est la ville ou les femmes ont le plus de chien ? Même question pour les hommes ?
"""

import pandas as pd
import numpy as np 

dataset = {
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'city':['Paris','Lille','Paris','Lille',
    'Paris','Bordeaux','Bordeaux'],
    'num_children':[3,0,2,4,3,1,5],
    'num_pet':[5,1,0,5,2,2,3],
    'status' : ['married', 'married', 'married', 'divorced', 'divorced', 'married', 'married']
}

dfCity = pd.DataFrame(dataset)

groupCity = dfCity.groupby(by=['city'])

# 1. Reprenez le dataset suivant et donnez le nombre d'enfant(s) par ville dans un tableau à deux colonnes **city** & **num_children**. 
print( groupCity[['num_children']].sum() )

# 2. Quel est l'écart des ages des habitants par ville ?
print( groupCity[['age']].aggregate( lambda x: np.max(x) - np.min(x)) )
print( groupCity.agg({'age': lambda x: x.max() - x.min()}) )
# 3. Est-ce que les femmes mariées ont plus d'enfant que les hommes divorcés ?

cond = dfCity[ (dfCity['gender'] == 'F') & (dfCity['status'] == 'married') ]['num_children'].sum() > dfCity[ (dfCity['gender'] == 'M') & (dfCity['status'] == 'divorced') ]['num_children'].sum() 
r = "oui" if cond else "non"
print( f"Réponse :  {r}")

#  4. Quelle est la ville où les femmes ont le plus de chien ? Même question pour les hommes ?
groupCityF = dfCity[ dfCity['gender'] == 'F'].groupby(by=['city'])
groupCityM = dfCity[ dfCity['gender'] == 'M'].groupby(by=['city'])

# Répondre
print( groupCityF['num_pet'].sum().idxmax() )
print( groupCityM['num_pet'].sum().idxmax() )

# deuxième solution 
groupCityF = dfCity.groupby(by=['city', 'gender'])
groupCityM = dfCity.groupby(by=['city', 'gender'])

print( groupCityF[['num_pet']].sum())
# print( groupCityM['num_pet'].sum().idxmax() )
