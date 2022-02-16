import numpy as np
import pandas as pd
import os
from wordcloud import WordCloud
import plotly
import plotly.express as px
import matplotlib.pyplot as plt

def save_bar_plot(data, ngram, nwords=20):
    fig = px.bar(data[:nwords], x='Слово', y = 'Частота')
    fig.update_layout(title={'text': f"Частота всречаемости {ngram}-грамм в корпусе из 100.000 вопросов"})
    fig.update_xaxes(tickangle = -45)
    plotly.offline.plot(fig, filename=f'../figures/bar_{ngram}grams.html', auto_open=False)

def save_wordcloud(data, ngram, nwords):
    d = dict(zip(data['Слово'][:nwords], data['Частота'][:nwords]))
    wordcloud = WordCloud(width=2000,height=1200, background_color='white').generate_from_frequencies(d)
    wordcloud.to_file(f'../figures/cloud_{ngram}grams.png')

def plot_both(ngram, nwords1, nwords2):
    data = pd.read_csv(f'../data/top_ngrams/top_{ngram}grams.csv', names=['Слово', 'Частота'], header=0)
    save_bar_plot(data, ngram, nwords1)
    save_wordcloud(data, ngram, nwords2)

if __name__ == '__main__':
    for ngram in [1, 2, 3]:
        plot_both(ngram, 20, 100)
