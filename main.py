from pathlib import Path

import pandas as pd

CSV_PATH = Path(__file__).parent / "titanic.csv"

df = pd.read_csv(CSV_PATH)

# On garde la trace des âges connus avant l'imputation, pour l'analyse enfants/adultes
df["age_connu"] = df["Age"].notna()
df["Age"] = df["Age"].fillna(df["Age"].median())
df = df.drop(columns=["Cabin"])
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])


print("La proportion de survivants :")
print(df["Survived"].value_counts(normalize=True))

print("\nLa proportion de survivants par sexe est :")
print(df.groupby("Sex")["Survived"].mean())

print("\nLa proportion de survivants par classe est :")
print(df.groupby("Pclass")["Survived"].mean())

print("\nLa proportion de survivants par sexe et par classe est :")
print(df.groupby(["Sex", "Pclass"])["Survived"].mean())

print("\nTableau croisé du taux de survie (sexe x classe) :")
print(df.pivot_table(index="Sex", columns="Pclass", values="Survived", aggfunc="mean"))

print("\nTableau croisé du nombre de passagers (sexe x classe) :")
print(df.pivot_table(index="Sex", columns="Pclass", values="Survived", aggfunc="count"))

# Analyse enfants/adultes sur les seuls passagers dont l'âge est connu :
# les âges imputés (médiane = 28 ans) classeraient à tort tous ces passagers parmi les adultes.
df_age = df[df["age_connu"]].copy()
df_age["enfant"] = df_age["Age"] < 12

print("\nLa proportion de survivants par enfant est (âges connus uniquement) :")
print(df_age.groupby("enfant")["Survived"].mean())

print("\nLa proportion de survivants par sexe et par enfant est (âges connus uniquement) :")
print(df_age.pivot_table(index="Sex", columns="enfant", values="Survived", aggfunc="mean"))

print("\nLe prix moyen du billet par classe est :")
print(df.groupby("Pclass")["Fare"].mean())
