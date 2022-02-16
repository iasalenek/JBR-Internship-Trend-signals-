import numpy as np
import pandas as pd
from stop_words import get_stop_words
import re

def get_stopwords(characters=True):
    stop_words = list(get_stop_words('en'))
    stop_words += ['i', 'you', 'can', 'need', 'tried', 'want', 'get', 'know', 'able', 'like', 'trying', 'help', 'error', 'quot', 't', 's', 'm', 'use', 'using', 'will', 'just', 'also', 'work', 'works', 'fine', 'gt', 'lt', 'amp', 'thanks', 'every', 'best', 'nan', 'div', 'null', 'don']
    if characters:
        stop_words += [chr(i) for i in range(97, 97 + 26)]
    return stop_words

def get_sample(n: int):
    full_data = pd.read_csv('../data/processed/Stackoverflow_clear_sample.csv',index_col=0, header=0)
    full_data = full_data.dropna(subset = ['Body'])
    data = full_data.sample(n)
    data['Body'] = data['Body'].apply(lambda x: re.sub(r'[^a-zA-Z]', ' ', x))
    data['Body'] = data['Body'].apply(lambda x: x.lower())
    return data['Body']

def count_ngrams(series: pd.Series, n: int, stop_words: list) -> pd.Series:
    ngrams = series.copy().str.split().explode()
    ind = ngrams.apply(lambda x: x not in stop_words)
    ngrams = ngrams[ind]
    result = ngrams.copy()
    for i in range(1, n):
        result += ' ' + ngrams.groupby(level=0).shift(-i)
    result = result.dropna()
    return result.value_counts()

def save_top_ngrams(n: int, ngram: int):
    stopwords = get_stopwords()
    sample = get_sample(100000)
    ngrams = count_ngrams(sample, ngram, stopwords)
    ngrams.name = 'Freq'
    ngrams[:n].to_csv(f'../data/top_ngrams/top_{ngram}grams.csv')

if __name__ == '__main__':
    for ngram in range(3):
        save_top_ngrams(1000, ngram + 1)