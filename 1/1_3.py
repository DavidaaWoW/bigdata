import math

def isnumber(str):
    try:
        number = float(str)
        result = True
    except ValueError:
        result = False
    return result

def getSquareBySides(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def init():
    print('Введите длины трёх сторон треугольника для подсчёта его площади')
    a = input()
    b = input()
    c = input()
    if(not isnumber(a) or not isnumber(b) or not isnumber(c)):
        return('Стороны должны быть числами!')
    a = float(a)
    b = float(b)
    c = float(c)
    if(a <= 0 or b <= 0 or c <= 0):
        return('Стороны ндолжны быть больше, или равны нулю!')
    if(a + b < c or a + c < b or b + c < a):
        return('Сумма двух сторон треугольника должна быть больше третьей!')
    return getSquareBySides(a, b, c)

print (init())
