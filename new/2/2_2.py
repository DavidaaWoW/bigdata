import os
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import preprocessing
from keras.datasets import fashion_mnist
from sklearn.datasets import load_digits
import umap
import time 

def build_plot(embedding, digits):
    plt.scatter(embedding[:, 0], embedding[:, 1], c=digits.target, cmap='Spectral', s=5)
    plt.gca().set_aspect('equal', 'datalim')
    plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
    plt.show()

def makeTSNE(perplexity):
    start = time.time()
    digits = load_digits()
    reducer = TSNE(n_components=2, perplexity=perplexity, random_state=2234)
    embedding = reducer.fit_transform(digits.data)
    end = time.time()
    print(str(end - start) + ' секунд')
    build_plot(embedding, digits)



def makeUMAP(n_neighbours, min_dist):
    start = time.time()
    digits = load_digits()
    reducer = umap.UMAP(n_neighbors=n_neighbours, min_dist=min_dist)
    embedding = reducer.fit_transform(digits.data)
    end = time.time()
    print(str(end - start) + ' секунд')
    build_plot(embedding, digits)


def init():
    inp = ''
    print('Введите номер команды для выполнения. \n 1. Алгоритм t-SNE \n 2. Алгоритм UMAP \n 0. Выход')
    while not inp == '0':
        inp = input()
        if inp == '1':
            print('Введите параметр perplexity')
            perplexity = input()
            makeTSNE(float(perplexity))
        elif inp == '2':
            print('Введите параметр n_neighbours')
            n_neighbours = input()
            print('Введите параметр min_dist')
            min_dist = input()
            makeUMAP(int(n_neighbours), float(min_dist))

init()