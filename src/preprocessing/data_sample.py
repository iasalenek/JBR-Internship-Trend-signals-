import numpy as np
import pandas as pd

full_data = pd.read_csv('../../data/processed/Stackoverflow_clear.csv',index_col=0, header=0)
full_data = full_data.dropna(subset = ['Body'])
data_sample = full_data[['Id', 'Body', 'CreationDate']].sample(100000)

data_sample.to_csv('../../data/processed/Stackoverflow_clear_sample.csv')