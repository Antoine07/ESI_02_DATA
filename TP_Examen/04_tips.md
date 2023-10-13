# TP pourboires

Vous allez travailler avec un jeu de données : **tips**, pourboires dans un restaurant.

Récupérez la source à l'adresse suivante : [tips](https://github.com/pandas-dev/pandas/blob/master/doc/data/tips.csv)

Vous enregistrerez ce fichier à la racine de vos fichiers pythons, puis :

```python
tips = pd.read_csv('data/tips.csv')
```

1. Ajoutez une colonne **tips_perct** au DataFrame tips, elle calculera le pourcentage de chaque pourboire par rapport au total des pourboires.

2. Quelles sont les pourcentages des pourboires par rapport au sex et à la consommation de tabac ? Donnez leurs moyennes et écarts types.

3. Calculez l'étendue des pourboires pour les femmes qu'elles fument ou ne fument pas. Créez une fonction peak_to_peak et appliquez cette fonction, comme une fonction d'agrégation, à votre groupement à l'aide de la fonction agg de Pandas.

4. En utilisant le même regroupement par sex et smoker et en utilisant la fonction agg de Pandas, calculez le max des pourboires ainsi que le nombre. Vous pouvez passer à la méthode agg un dictionnaire pour spécifier les fonctions à appliquer par colonne.
