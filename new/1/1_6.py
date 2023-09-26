import pandas as pd
import os
from sklearn.datasets import fetch_california_housing

def getContent():
    data = fetch_california_housing(as_frame=True)
    return data

def interpolateData(data, column):
    df = pd.DataFrame(data)
    df['interpolated_values'] = df[column].interpolate()
    return df

def getMaxValue(data):
    return max(data.MedInc)

def getMinValue(data):
    return min(data.MedInc)

def getAvgValue(data):
    print(data.name, data.mean())

def init():
    data = getContent().data
    inp = ''

    while not inp == '0':
        print('Введите номер команды для выполнения. \n 1. Вывести данные \n 2. Вывести информацию о данных \n 3. Вывести количество пропущенных данных \n 4. Интерполировать данные в \
определённом столбце \n 5. Вывести записи, где средний возраст домов в районе более 50 лет и\
население более 2500 человек \n 6. Вывести максимальное значение стоимости дома \n 7. Вывести минимальное значение стоимости дома \n \
8. Вывести на экран название признака и его среднее значение. \n 0. Выход')
        inp = input()
        if inp == '1':
            print(data)
        elif inp == '2':
            print(data.info())
        elif inp == '3':
            print(data.isna().sum())
        elif inp == '4':
            print('Введите столбец для интерполяции')
            column = input()
            print(interpolateData(data, column))
        elif inp == '5':
            print(data.loc[(data.HouseAge > 50) & (data.Population > 2500)])
        elif inp == '6': 
            print(getMaxValue(data))
        elif inp == '7': 
            print(getMinValue(data))
        elif inp == '8':
            data.apply(getAvgValue, axis=0)



init()
