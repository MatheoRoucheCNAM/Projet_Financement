import numpy as np             
import pandas as pd             
import os                       
import matplotlib.pyplot as plt 
from IPython.display import display
from random import seed

filepath = os.path.join(os.path.dirname(__file__), 'financement.csv')
financement = pd.read_csv(filepath, sep=',', header=0, index_col=0)

#Data préparation --> Calcul montant de financement d'un projet si il est financé

#convertir les dates --> YYYY-MM-DD

financement['lancement'] = pd.to_datetime(financement['lancement']).dt.strftime('%Y-%m-%d')
# print(financement[['lancement']].head(10))

# calcul nouveaux champs écart en date de lancement et date butoire en days
financement['ecart_days'] = (pd.to_datetime(financement['date_butoire']) - pd.to_datetime(financement['lancement'])).dt.days
# print(financement[['lancement', 'date_butoire', 'ecart_days']].head(10))

# Création champ supplémentaire avec les dates --> Année  et mois de date_butoire et lancement

financement['annee_lancement'] = pd.to_datetime(financement['lancement']).dt.year
financement['mois_lancement'] = pd.to_datetime(financement['lancement']).dt.month
print(financement[['lancement', 'annee_lancement', 'mois_lancement']].head(10))

financement['annee_date_butoire'] = pd.to_datetime(financement['date_butoire']).dt.year
financement['mois_date_butoire'] = pd.to_datetime(financement['date_butoire']).dt.month
print(financement[['date_butoire', 'annee_date_butoire', 'mois_date_butoire']].head(10))
