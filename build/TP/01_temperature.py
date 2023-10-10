"""
Exercice température

Nous avons relevé des températures au mois de Janvier. Répondez aux questions suivantes :

1. Donnez toutes les températures qui sont supérieures à 0.

2. Comparez les températures supérieures et inférieures à 0 (lesquelles ont été les plus prépondérantes ... )

3. Donnez le pourcentage des températures positives sur le mois.

4. Créez un tableau days pour les jours du mois et donnez les jours pour lesquels la température était supérieure à 0.

5. Donnez toutes les températures supérieures à 0 à partir du dixième jour du mois.

6. Remplacez maintenant les températures négatives par la moyenne des températures positives.

"""
import numpy as np 

january = np.array([-2,  5, -5,  6, -2,  0,  6,  2,  8,  0,  6, -1,  3,  3,  7,  0, -5,
        7,  4,  7,  8, -1,  5, -2,  3, -3, -2,  7,  8,  4,  2], dtype='float64')

print( "1. Donnez toutes les températures qui sont supérieures à 0.")

mask = january > 0
print(january[mask])

print("2. Comparez les températures supérieures et inférieures à 0.")
# il y a plus de température positive ?
print( "Plus de t positives." if sum(january > 0 ) > sum(january <= 0) else "Plus de négatives." )

print("3. Donnez le pourcentage des températures positives sur le mois.")
nbPositives = sum(january > 0) # sum des True == 1 une autre de les compter
nbNegatives = sum(january <= 0)
total = len(january)

print(f"Températures positives { round(nbPositives/total, 2) * 100 }%")
print(f"Températures négatives { round(nbNegatives/total, 2) * 100 }%")

print("4. Créez un tableau days pour les jours du mois et donnez les jours pour lesquels la température était supérieure à 0.")

days = np.array(range(1, len(january) + 1))
# print(days)
print(days[ january > 0 ])

print( "5. Donnez toutes les températures supérieures à 0 à partir du dixième jour du mois.")
# lorsque vous appliquez un masque il faut qu'il est la même dimension attention
print( january[ (days >= 10) & (january > 0) ] )

print( "6. Remplacez maintenant les températures négatives par la moyenne des températures positives." )

total_p = sum( january > 0 ) 

avg_p = round ( sum(january[january > 0]) / total_p, 2 )

print(f"Moyenne des températures positives {avg_p}")

