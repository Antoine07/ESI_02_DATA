import pandas as pd

# Créer un DataFrame exemple
data = {'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 35, 45, 55, 65]}

df = pd.DataFrame(data)

# Définir les limites des tranches d'âge
limites_tranches = [0, 30, 40, 50, 60, 100]

# Définir les étiquettes des tranches d'âge
etiquettes_tranches = ['0-30', '31-40', '41-50', '51-60', '61+']

# Ajouter une nouvelle colonne "Tranche d'âge" au DataFrame
df['Tranche d\'âge'] = pd.cut(df['Age'], bins=limites_tranches, labels=etiquettes_tranches, right=False)

# Afficher le DataFrame résultant
print(df[ df["Tranche d'âge"] == '31-40' ])
