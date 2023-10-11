import pandas as pd
import numpy as np

# print(help(pd))

temperatures = np.array([
    [25, 28.5, 30],
    [33, 29, 35],
    [38, 39, 44],
])

temperatures_df = pd.DataFrame(
    temperatures,
    index = ['Bordeaux', 'Paris', 'Lille'],
    columns = ['2001', '2002', '2003']
)

# print(temperatures_df['2001'])
# print(temperatures_df['2001']['Paris'])

# les fonctions sur le DataFrame

# print(temperatures_df.info())
print(temperatures_df.describe())