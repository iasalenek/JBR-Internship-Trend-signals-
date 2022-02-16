import numpy as np
import pandas as pd
import os

colnames = ['Id', 'Title', 'Body', 'CreationDate']
data_unique = pd.DataFrame(columns=colnames)

for filename in os.listdir('../../data/raw_data'):
    cur_data =  pd.read_csv(f"../../data/raw_data/{filename}", names=colnames,index_col=False, header=0)
    data_unique = pd.concat([data_unique, cur_data])
    data_unique = data_unique.drop_duplicates(subset=['Id'])

data_unique.to_csv('../../data/data_unique/data_unique.csv', index=False)