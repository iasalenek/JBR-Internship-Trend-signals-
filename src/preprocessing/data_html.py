import numpy as np
import pandas as pd
import re

colnames = ['Id', 'Title', 'Body', 'CreationDate']

def clean_html(text):
    text = re.sub(r'<code>[\S\s]*?<\/code>', '', text)
    text = re.sub(r'<a href.*?<\/a>', '', text)
    text = re.sub(r'<.*?>', '', text)

    return text

data = pd.read_csv('../../data/data_unique/data_unique.csv', names=colnames,index_col=False, header=0)

data['Body'] = data['Body'].astype(str)
data['Body'] = data['Body'].apply(clean_html)

data.to_csv('../../data/processed/Stackoverflow_clear.csv')