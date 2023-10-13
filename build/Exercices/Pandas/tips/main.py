import pandas as pd
import numpy as np

tips = pd.read_csv('./tips.csv')

print(tips.head(2))

"""
1. Ajoutez une colonne **tips_perct** au DataFrame tips, 
elle calculera le pourcentage de chaque pourboire par 
rapport au total de la note.
"""

tips['tips_perct'] = tips['tip'] / tips['total_bill']

"""
2. Quelles sont les pourcentages des pourboires par rapport 
au sex et à la consommation de tabac ? Donnez leurs moyennes 
et écarts types.

"""

print( tips.groupby(['sex', 'smoker'])['tips_perct'].agg(['mean', 'std']) )


"""

3. Calculez l'étendue des pourboires pour les femmes 
qu'elles fument ou ne fument pas. Créez une fonction 
peak_to_peak et appliquez cette fonction, comme une 
fonction d'agrégation, à votre groupement à l'aide de 
la fonction agg de Pandas.

"""

def peak_to_peak(arr):
    
    return arr.max() - arr.min()


print( tips.groupby('smoker')['tip'].agg(peak_to_peak) )


"""
 4. En utilisant le même regroupement par sex et smoker 
et en utilisant la fonction agg de Pandas, calculez le max 
des pourboires ainsi que le nombre. Vous pouvez passer 
à la méthode agg un dictionnaire pour spécifier les fonctions 
à appliquer par colonne.
"""

print( tips.groupby(['sex', 'smoker'])['tip'].agg(lambda x: [x.max() , x.count()]) )

