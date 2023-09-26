import pandas as pd
import os
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import scipy.stats as sts
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.subplots as sp

def getContent(path):
    data = pd.read_csv(path, sep=',')
    return data

def interpolateData(data, column):
    df = pd.DataFrame(data)
    df['interpolated_values'] = df[column].interpolate()
    return df

def generateBarDiagram(data, x, y):
        fig = px.bar(data, x=x, y=y, color=y, color_continuous_scale='viridis', title='Столбчатая диаграмма зависимости ' + y + ' от ' + x,)
        fig.update_traces(marker_line_color='black', marker_line_width=2, opacity=0.8)
        fig.update_layout(title_x=0.5, title_y=0.95, title_font_size=20, xaxis_title=x, yaxis_title=y,
                xaxis_tickangle=315,
                xaxis_title_font=dict(size=16),
                yaxis_title_font=dict(size=16),
                xaxis_tickfont=dict(size=14),
                yaxis_tickfont=dict(size=14),
                width=None,
                height=700,
                margin=dict(l=0, r=0, t=0, b=0))
        fig.show()

def getCentralTendentions(data, y):
    mean = np.mean(data[y])
    mode = sts.mode(data[y])[0][0]
    median = np.median(data[y])
    return {'Среднее арифметическое': mean, 'Мода': mode, 'Медиана': median}

def getScatteredMeasures(data, y):
    range = data[y].max() - data[y].min()
    standart_deviation = data[y].std()
    iqr = sts.iqr(data[y], interpolation='midpoint')
    return {'Размах': range, 'Стандартное отколнение': standart_deviation, 'Межквартильный размах': iqr}

def generateTwoBarDiagrams(data1, data2):
    fig = make_subplots(rows=1, cols=2)  # Создание сетки с двумя столбцами

    fig.add_trace(go.Bar(
        x=list(data1.keys()),
        y=list(data1.values()),
        marker_colorscale='viridis'
    ), row=1, col=1)  # Добавление первого графика в первый столбец

    fig.add_trace(go.Bar(
        x=list(data2.keys()),
        y=list(data2.values()),
        marker_colorscale='viridis'
    ), row=1, col=2)

    fig.update_layout(title_x=0.5, title_y=0.95, title_font_size=20,
        xaxis_tickangle=315,
        xaxis_title_font=dict(size=16),
        yaxis_title_font=dict(size=16),
        xaxis_tickfont=dict(size=14),
        yaxis_tickfont=dict(size=14),
        width=None,
        height=700,
        margin=dict(l=0, r=0, t=0, b=0))
    fig.show()

def generatePlotBox(data, x, y):
    fig = px.box(data, x=x, y=y)
    fig.show()

def generateCLT(data, param):
    # Количество выборок и длины выборок
    num_samples = 300
    sample_lengths = list(range(5, 301))

    # Генерация и анализ выборок
    sample_means = []
    for n in sample_lengths:
        means = []
        for _ in range(num_samples):
            sample = data[param].sample(n)
            means.append(sample.mean())
        sample_means.append(means)
    print(sample_means[0])
    return

    # Подготовка данных для построения гистограммы
    data_for_histogram = []
    labels = []

    for n, means in zip(sample_lengths, sample_means):
        data_for_histogram.extend(means)
        labels.extend([f'n={n}'] * num_samples)

    histogram_data = pd.DataFrame({'Средние значения': data_for_histogram, 'Длина выборки': labels})

    # Сгруппируем данные по длине выборки и среднему значению
    grouped_data = histogram_data.groupby(['Длина выборки', 'Средние значения']).size().reset_index(name='Количество')

    # Построение гистограммы
    fig = px.bar(grouped_data, x='Средние значения', y='Количество', color='Длина выборки',
                title=f'Распределение средних значений выборок для признака {param}',
                labels={'Средние значения': param})
    fig.show()

def init():
    absolute_path = os.path.join(os.path.dirname(__file__), 'insurance.csv')
    data = getContent(absolute_path)
    inp = ''
    print('Введите номер команды для выполнения. \n 1. Вывести данные \n 2. Вывести статистику о данных \n 3. Построить столбчатую диаграмму \n 4. Найти меры центральной тенденции и меры разброса \n 5. Построить ящик с усами \n 6. Проверка центральной предельной теоремы \n 0. Выход')
    while not inp == '0':
        inp = input()
        if inp == '1':
            print(data)
        elif inp == '2':
            print(data.describe())
        elif inp == '3':
            print('Выберите параметр оси y \n 1. ИМТ \n 2. Количество детей \n 3. Расходы')
            y = input()
            if(y != '1' and y != '2' and y != '3'):
                print('Неправильно введены данные')
                continue
            if(y == '1'):
                y = 'bmi'
            elif(y == '2'):
                y = 'children'
            elif(y == '3'):
                y = 'charges'
            aggregated_data = data.groupby('age')[y].mean().reset_index()
            aggregated_data = aggregated_data.sort_values(by='age')
            generateBarDiagram(aggregated_data, 'age', y)

        elif inp == '4':
            print('Выберите столбец для получения данных: \n 1. ИМТ \n 2. Расходы')
            y = input()
            if(y != '1' and y != '2'):
                print('Неправильно введены данные')
                continue
            if(y == '1'):
                y = 'bmi'
            elif(y == '2'):
                y = 'charges'
            central_tendentions = getCentralTendentions(data, y)
            scattered_measures = getScatteredMeasures(data, y)
            generateTwoBarDiagrams(central_tendentions, scattered_measures)
        elif inp == '5':
            print('Выберите параметр оси x: \n 1. Возраст \n 2. Пол \n 3. Признак курильщика \n 4. Регион')
            x = input()
            if(x != '1' and x != '2' and x != '3' and x != '4'):
                print('Неправильно введены данные')
                continue
            if(x == '1'):
                x = 'age'
            elif(x == '2'):
                x = 'sex'
            elif(x == '3'):
                x = 'smoker'
            elif(x == '4'):
                x = 'region'
            print('Выберите параметр оси y: \n 1. ИМТ \n 2. Количество детей \n 3. Расходы')
            y = input()
            if(y != '1' and y != '2' and y != '3'):
                print('Неправильно введены данные')
                continue
            if(y == '1'):
                y = 'bmi'
            elif(y == '2'):
                y = 'children'
            elif(y == '3'):
                y = 'charges'
            generatePlotBox(data, x, y)
        elif inp == '6':
            print('Выберите параметр для генерации: \n 1. ИМТ \n 2. Расходы')
            y = input()
            if(y != '1' and y != '2'):
                print('Неправильно введены данные')
                continue
            if(y == '1'):
                y = 'bmi'
            elif(y == '2'):
                y = 'charges'
            generateCLT(data, y)
init()
