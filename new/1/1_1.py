import math

def isnumber(str):
    try:
        number = float(str)
        result = True
    except ValueError:
        result = False
    return result

def getSquareByParams(figure, params):
    if(figure == "triangle"):
        if isnumber(params["basis"]) and isnumber(params["height"]):
            basis = float(params["basis"])
            height = float(params["height"])
            if basis != 0 and height != 0:
                square = (basis * height) / 2
            else:
                square = 'Ошибка во входных параметрах'
        else:
            square = 'Ошибка во входных параметрах'
        return {
            'figure': 'triangle',
            'square': square
        }
    elif(figure == "rectangle"):
        if isnumber(params["a"]) and isnumber(params["b"]):
            a = float(params["a"])
            b = float(params["b"])
            if a != 0 and b != 0:
                square = (a * b)
            else:
                square = 'Ошибка во входных параметрах'
        else:
            square = 'Ошибка во входных параметрах'
        return {
            'figure': 'rectangle',
            'square': square
        }
    elif(figure == "circle"):
        if isnumber(params["radius"]):
            radius = float(params["radius"])
            if radius != 0:
                square = math.pi * (radius ** 2)
            else:
                square = 'Ошибка во входных параметрах'
        else:
            square = 'Ошибка во входных параметрах'
        return {
            'figure': 'circle',
            'square': square
        }
    return

def init():
    print('Выберите фигуру: \n 1. Треугольник \n 2. Прямоугольник \n 3. Круг')
    inp = input()
    if(inp == '1'):
        print('Введите длинну высоты и основания')
        height = input()
        basis = input()
        return getSquareByParams('triangle', {'height': height, 'basis': basis})
    elif(inp == '2'):
        print('Введите размеры сторон')
        a = input()
        b= input()
        return getSquareByParams('rectangle', {'a': a, 'b': b})
    elif(inp == '3'):
        print('Введите длинну радиуса')
        radius = input()
        return getSquareByParams('circle', {'radius': radius})
    else:
        return('Введено неверное значение!')

print (init())
