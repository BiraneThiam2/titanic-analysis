# Analyse des survivants du Titanic

Analyse exploratoire du jeu de données Titanic (891 passagers) avec **pandas**.
Le but est de voir quels facteurs (sexe, classe, âge) ont joué sur la survie.

## Contenu du projet

| Fichier       | Description                                             |
|---------------|---------------------------------------------------------|
| `main.py`     | Script d'analyse : nettoyage des données et statistiques |
| `titanic.csv` | Jeu de données (891 lignes, 12 colonnes)                 |
| `requirements.txt` | Dépendances Python                                  |
| `.gitignore`  | Fichiers exclus de Git (`.venv/`, `__pycache__/`, etc.)  |

## Installation

Prérequis : Python 3.10 ou plus récent.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Utilisation

Le CSV est cherché dans le dossier du script : on peut donc lancer `main.py` depuis n'importe quel dossier.

```bash
python main.py
```

## Étapes de l'analyse

### 1. Nettoyage des données

| Colonne    | Valeurs manquantes | Traitement                                      |
|------------|--------------------|-------------------------------------------------|
| `Age`      | 177                | Remplacées par la médiane (28 ans)              |
| `Cabin`    | 687                | Colonne supprimée (trop de valeurs manquantes)  |
| `Embarked` | 2                  | Remplacées par le port le plus fréquent (`S`)   |

### 2. Statistiques calculées

- Taux de survie global
- Taux de survie par sexe
- Taux de survie par classe (`Pclass`)
- Taux de survie et effectifs croisés sexe × classe (tableaux croisés)
- Taux de survie des enfants (moins de 12 ans) par rapport aux adultes, puis par sexe (calculé uniquement sur les 714 passagers dont l'âge est connu)
- Prix moyen du billet (`Fare`) par classe

## Principaux résultats

| Indicateur                         | Taux de survie |
|------------------------------------|----------------|
| Ensemble des passagers             | 38,4 %         |
| Femmes                             | 74,2 %         |
| Hommes                             | 18,9 %         |
| 1re classe                         | 63,0 %         |
| 2e classe                          | 47,3 %         |
| 3e classe                          | 24,2 %         |
| Enfants (< 12 ans)                 | 57,4 %         |
| Femmes de 1re classe               | 96,8 %         |
| Hommes de 3e classe                | 13,5 %         |

**Conclusions :**

- Le sexe est le facteur le plus marqué : les femmes ont environ 4 fois plus survécu que les hommes, ce qui reflète la règle « les femmes et les enfants d'abord ».
- La classe compte aussi : plus la classe est haute, plus le taux de survie l'est. Le billet moyen coûte environ 84 £ en 1re classe, contre 21 £ en 2e et 14 £ en 3e.
- Les enfants ont mieux survécu que les adultes (57 % contre 39 %). Chez les garçons, l'écart est fort : 56 % pour les moins de 12 ans, contre 18 % pour les hommes adultes.

## Limites

- Les 177 âges manquants sont remplacés par 28 ans. Pour ne pas les compter à tort comme adultes, l'analyse enfants/adultes ne garde que les passagers dont l'âge est connu (714 sur 891).
- L'analyse est descriptive : elle compare des moyennes sans tester leur significativité statistique.

## Pistes d'amélioration

- Ajouter des graphiques (matplotlib ou seaborn)
- Imputer l'âge selon le titre du passager (Mr, Mrs, Miss, Master)
- Entraîner un modèle de prédiction de la survie (par exemple avec scikit-learn)

## Source des données

Jeu de données Titanic issu de la compétition Kaggle [Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic) (fichier `train.csv`).

## Auteur

**Birane Thiam** — [@BiraneThiam2](https://github.com/BiraneThiam2)
