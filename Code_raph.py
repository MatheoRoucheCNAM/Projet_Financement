import numpy as np              # linear algebra
import pandas as pd             # data processing, CSV file I/O (e.g. pd.read_csv)
import os                       # files handling
import matplotlib.pyplot as plt # plotting & dataviz
from IPython.display import display
from random import seed

filepath ='C:/Users/rapha/OneDrive/Bureau/fouillesEtEntreposage/projet/financement.csv'
financement = pd.read_csv(filepath,sep=',', header=0,index_col=0)

print(financement.head(20))
