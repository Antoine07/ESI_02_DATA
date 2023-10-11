# Analyse de données

**DataOps avec Python données du Titanic**

**Description :**

Vous êtes responsable de la gestion des données pour une entreprise. Mettez en place le processus de traitement des données.

1. Combien de femme de moins de 18 ont survécu

2. Parmi ces femmes (question 1) déterminer la répartition par classe sur le bateau.

3. Déterminer si le port d'embarquemen a une influence sur la survie (calculer la répartiti  des morts et des survivants en fonction du port de départ)

4. Déterminer la répartition par sexe et par âge des passagers du navire

5. Conclusion, écrire un document qui vous présentera votre analyse lors de la soutenance.

Indications :
- Utilisez Python pour automatiser certaines tâches répétitives.
- Intégrez des bibliothèques telles que Pandas, NumPy, ou d'autres outils modules Python.

**Tâches :**

- Proposez une méthode de récupération des données pour optimiser l'analyse.

- On aimerait à partir des données bruts du titanic mettre en place un modèle (JSON) plus simple que l'on pourrait conserver (enregistrer) pour nos traitements. Vous utiliserez le modèle suivant :

```python
passenger = {
    "sex"
    "class" 
    "age" 
    "survived"
    "price" 
    "embarked"
}
```

1. **Pipeline :**
   - Mettez en place le pipeline de bout en bout pour la récupération des données.
   - Créez des fonctions pour mettre en place ce pipeline. Vous pouvez par exemple créer les fonctions suivantes.
   - Pensez à nettoyer les données ( données aberrantes )

```python

# request data
def requestUrl(url):
    pass

# création d'un modèle à partir des données téléchargées
def extract_model(url):
    pass

# nettoyage/formatage des données
def transform(data):
    pass

# Enregistrement des données
def load(data):
    pass

```

**Mise en œuvre des Changements avec Python :**
  

3. **Documentation :**
   - Rédigez une documentation complète expliquant le nouveau pipeline DataOps, y compris les choix technologiques, les dépendances, et les instructions pour les utilisateurs futurs.

**Rendu :**
- Un script Python optimisé pour le pipeline DataOps.
- Un rapport documentant les améliorations apportées, les choix technologiques, et vos résultats.
