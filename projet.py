import numpy as np             
import pandas as pd             
import os                       
import matplotlib.pyplot as plt 
from IPython.display import display
from random import seed
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score

# Chargement des données
filepath = os.path.join(os.path.dirname(__file__), 'financement.csv')
financement = pd.read_csv(filepath, sep=',', header=0, index_col=0)

# Convertir les dates en format YYYY-MM-DD
financement['lancement'] = pd.to_datetime(financement['lancement']).dt.strftime('%Y-%m-%d')

# Calcul du nouvel attribut : écart en jours entre la date de lancement et la date butoire
financement['ecart_days'] = (pd.to_datetime(financement['date_butoire']) - pd.to_datetime(financement['lancement'])).dt.days

# Création de champs supplémentaires avec les années et mois de date_butoire et de lancement
financement['annee_lancement'] = pd.to_datetime(financement['lancement']).dt.year
financement['mois_lancement'] = pd.to_datetime(financement['lancement']).dt.month
financement['annee_date_butoire'] = pd.to_datetime(financement['date_butoire']).dt.year
financement['mois_date_butoire'] = pd.to_datetime(financement['date_butoire']).dt.month

# Affichage des premières lignes
print(financement[['lancement', 'annee_lancement', 'mois_lancement']].head(10))
print(financement[['date_butoire', 'annee_date_butoire', 'mois_date_butoire']].head(10))

# Filtrer les données pour inclure uniquement les projets financés
financement_finance = financement[financement['etat'] == 'financé']

# Préparation des données pour la modélisation
X = financement_finance[['ecart_days', 'objectif', 'supporters']]  
y = financement_finance['promesse_usd1']  

# Division des données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle de régression logistique
model = LogisticRegression()
model.fit(X_train, y_train)

# Prédiction sur l'ensemble de test
y_pred = model.predict(X_test)

# Évaluation du modèle
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)
