import pandas as pd
import numpy as np

dataset_fruit_01 = {
    'Rapsberry' : [30 ],
    'Cherries' : [20 ]
}

df_fruit_01 = pd.DataFrame(dataset_fruit_01)
# print(df_fruit_01)

dataset_fruit_02 = {
    'fig' : [130 , 309 ],
    'wine' : [120,290 ]
}

df_fruit_02 = pd.DataFrame(dataset_fruit_02, index=['2020', '2019'])
# print(df_fruit_02)

# 1 Total fruit 
# La première somme c'est la somme des lignes, puis la deuxième somme fait la somme totale
# print( df_fruit_01.sum().sum() )
# print( df_fruit_02.sum().sum() )

print(df_fruit_02.sum(1).idxmax())

# print( df_fruit_02[fruit] )

# print(df_fruit_02)
