import numpy as np             
import pandas as pd             
import os                       
import matplotlib.pyplot as plt 
from IPython.display import display
from random import seed

filepath = os.path.join(os.path.dirname(__file__), 'financement.csv')
financement = pd.read_csv(filepath, sep=',', header=0, index_col=0)

financement.head(20)

#fonction detail dataframe
def resume_dataframe(df):
    resume_df = pd.DataFrame(index=df.columns)
    resume_df['Type'] = df.dtypes.values
    resume_df['Missing'] = df.isnull().sum().values

    resume_df['Unique'] = df.nunique().values

    for col in df.columns:
        resume_df[f'{col}_1'] = df[col].iloc[0]
        resume_df[f'{col}_2'] = df[col].iloc[1]
        resume_df[f'{col}_3'] = df[col].iloc[2]

    return resume_df

resume_transactions = resume_dataframe(financement)

display(resume_transactions)