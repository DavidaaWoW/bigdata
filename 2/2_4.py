import pandas as pd
import os

def getContent(path):
    data = pd.read_csv(path, sep=',')
    return data

def interpolateData(data, column):
    df = pd.DataFrame(data)
    df['interpolated_values'] = df[column].interpolate()
    return df

def isLargeFamily(childs):
    childs['isLargeFamily'] = int(childs['children']) >= 3
    return childs

def init():
    absolute_path = os.path.join(os.path.dirname(__file__), 'insurance.csv')
    data = getContent(absolute_path)
    inp = ''
    print('Введите номер команды для выполнения. \n 1. Вывести данные \n 2. Вывести информацию о данных \n 3. Вывести количество пропущенных данных \n 4. Интерполировать данные в определённом столбце \n 5. Добавить столбец "многодетная семья" \n 0. Выход')
    while not inp == '0':
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
            print(data.apply(isLargeFamily, axis=1))

init()
