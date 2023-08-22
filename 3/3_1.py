import pandas as pd
import os
import plotly
import plotly.graph_objs as go
import plotly.express as px
import matplotlib.pyplot as plt

def getContent(path):
    data = pd.read_csv(path, sep=',')
    return data

def interpolateData(data, column):
    df = pd.DataFrame(data)
    df['interpolated_values'] = df[column].interpolate()
    return df

def generateBarDiagram(data, x, y):
        data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
        aggregated_data = data.groupby(x)[y].mean().reset_index()
        aggregated_data = aggregated_data.sort_values(by=x)
        fig = px.bar(aggregated_data, x=x, y=y, color=y, color_continuous_scale='viridis', title='Столбчатая диаграмма зависимости ' + y + ' от ' + x,)
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

def generatePieDiagram(data, x, y):
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
    data['Year'] = data['Date'].dt.year
    if x == 'Date':
        print('success')
        aggregated_data = data.groupby('Year')[y].mean().reset_index()
        title = 'Круговая диаграмма зависимости ' + y + ' от ' + x + ' по годам'
        x = 'Year'
    else:
        aggregated_data = data.groupby(x)[y].mean().reset_index()
        title = 'Круговая диаграмма зависимости ' + y + ' от ' + x
    aggregated_data = aggregated_data.sort_values(by=x)
    fig = px.pie(aggregated_data, names=x, values=y,
             title=title,
             hole=0.3,
             template='plotly')
    fig.update_traces(marker=dict(line=dict(color='black', width=2)))
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

def generateLineDiagram(data, x, y):
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
    aggregated_data = data.groupby(x)[y].mean().reset_index()
    aggregated_data = aggregated_data.sort_values(by=x)
    fig = px.line(aggregated_data, x=x, y=y,
             title='Круговая диаграмма зависимости ' + y + ' от ' + x,
             template='plotly')
    fig.update_traces(line=dict(color='crimson', width=2),
                  marker=dict(color='white', line=dict(color='black', width=2)))
    fig.update_layout(title_x=0.5, title_y=0.95, title_font_size=20, xaxis_title=x, yaxis_title=y,
            xaxis_tickangle=315,
            xaxis_title_font=dict(size=16),
            yaxis_title_font=dict(size=16),
            xaxis_tickfont=dict(size=14),
            yaxis_tickfont=dict(size=14),
            width=None,
            height=700,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis_gridcolor='ivory', yaxis_gridcolor='ivory',
            xaxis_gridwidth=2, yaxis_gridwidth=2)
    fig.show()

def generateBarDiagramMatplotlib(data, x, y):
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
    aggregated_data = data.groupby(x)[y].mean().reset_index()
    aggregated_data = aggregated_data.sort_values(by=x)
    
    plt.figure(figsize=(10, 6))

    plt.bar(aggregated_data[x], aggregated_data[y], edgecolor=plt.cm.viridis(range(len(aggregated_data))), linewidth=2)
    plt.xlabel(x, fontsize=16)
    plt.ylabel(y, fontsize=16)
    plt.title('Столбчатая диаграмма зависимости ' + y + ' от ' + x, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(axis='y', linestyle='--', linewidth=0.7, color='ivory')
    plt.tight_layout()
    plt.show()

def generatePieDiagramMatplotlib(data, x, y):
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
    data['Year'] = data['Date'].dt.year
    if x == 'Date':
        print('success')
        aggregated_data = data.groupby('Year')[y].mean().reset_index()
        title = 'Круговая диаграмма зависимости ' + y + ' от ' + x + ' по годам'
        x = 'Year'
    else:
        aggregated_data = data.groupby(x)[y].mean().reset_index()
        title = 'Круговая диаграмма зависимости ' + y + ' от ' + x
    aggregated_data = aggregated_data.sort_values(by=x)
    
    plt.figure(figsize=(8, 8))

    colors = plt.cm.viridis(range(len(aggregated_data)))

    plt.pie(aggregated_data[y], labels=aggregated_data[x], autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=dict(edgecolor='black', linewidth=2))
    plt.title('Круговая диаграмма зависимости ' + y + ' от ' + x, fontsize=20)
    plt.axis('equal')
    
    plt.tight_layout()
    plt.show()

def generateLineDiagramMatplotlib(data, x, y):
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
    aggregated_data = data.groupby(x)[y].mean().reset_index()
    aggregated_data = aggregated_data.sort_values(by=x)
    
    plt.figure(figsize=(10, 6))

    plt.plot(aggregated_data[x], aggregated_data[y], color='crimson', linewidth=2, marker='o', markersize=8, markerfacecolor='white', markeredgewidth=2, markeredgecolor='black')
    plt.xlabel(x, fontsize=16)
    plt.ylabel(y, fontsize=16)
    plt.title('Линейная диаграмма зависимости ' + y + ' от ' + x, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(axis='y', linestyle='--', linewidth=0.7, color='ivory')
    
    plt.tight_layout()
    plt.show()


def init():
    absolute_path = os.path.join(os.path.dirname(__file__), 'Walmart_Store_sales.csv')
    data = getContent(absolute_path)
    inp = ''
    print('Введите номер команды для выполнения. \n 1. Вывести данные \n 2. Вывести информацию о данных \n 3. Вывести количество пропущенных данных \n 4. Интерполировать данные в определённом столбце \n 5. Вывести столбчатую диаграмму \n 6. Вывести круговую диаграмму \n 7. Вывести линейную диаграмму \n 0. Выход')
    while not inp == '0':
        inp = input()
        if inp == '1':
            print(data)
        elif inp == '2':
            print(data.info(), data.head())
        elif inp == '3':
            print(data.isna().sum())
        elif inp == '4':
            print('Введите столбец для интерполяции')
            column = input()
            print(interpolateData(data, column))
        elif inp == '5' or inp == '6' or inp == '7':
            print('Выберите параметр оси x \n 1. Дата \n 2. ID магазина')
            x = input()
            if(x != '1' and x != '2'):
                print('Неправильно введены данные')
                continue
            print('Выберите параметр оси y \n 1. Недельные продажи \n 2. Флаг выходных \n 3. Температура \n 4. Цена за топливо \n 5. CPI \n 6. Коэффициент безработицы')
            y = input()
            if(y != '1' and y != '2' and y != '3' and y != '4' and y != '5' and y != '6'):
                print('Неправильно введены данные')
                continue
            if(x == '2'):
                x = 'Store'
            elif (x == '1'):
                x = 'Date'
            if(y == '1'):
                y = 'Weekly_Sales'
            elif(y == '2'):
                y = 'Holiday_Flag'
            elif(y == '3'):
                y = 'Temperature'
            elif(y == '4'):
                y = 'Fuel_Price'
            elif(y == '5'):
                y = 'CPI'
            elif(y == '6'):
                y = 'Unemployment'
            print('Введите библиотеку для генерации диаграммы \n 1. Pyplot \n 2. MatPlotLib')
            lib = input()
            if(lib != '1' and lib != '2'):
                print('Неправильно введены данные')
                continue
            if(inp == '5'):
                if(lib == '1'):
                    generateBarDiagram(data, x, y)
                else:
                    generateBarDiagramMatplotlib(data, x, y)
            elif(inp == '6'):
                if(lib == '1'):
                    generatePieDiagram(data, x, y)
                else:
                    generatePieDiagramMatplotlib(data, x, y)
            elif(inp == '7'):
                if(lib == '1'):
                    generateLineDiagram(data, x, y)
                else:
                    generateLineDiagramMatplotlib(data, x, y)

init()
