
import math

def isnumber(str):
    try:
        number = float(str)
        result = True
    except ValueError:
        result = False
    return result

def calculate(operation, digits):
    if(operation == 1):
        if not isnumber(digits["a"]) or not isnumber(digits["b"]):
            return 'Ошибка во входных параметрах'
        result = (float(digits['a']) + float(digits['b']))
        return result
    elif(operation == 2):
        if not isnumber(digits["a"]) or not isnumber(digits["b"]):
            return 'Ошибка во входных параметрах'
        result = (float(digits['a']) - float(digits['b']))
        return result
    elif(operation == 3):
        if not isnumber(digits["a"]) or not isnumber(digits["b"]):
            return 'Ошибка во входных параметрах'
        result = (float(digits['a']) * float(digits['b']))
        return result
    elif(operation == 4):
        if not isnumber(digits["a"]) or not isnumber(digits["b"]):
            return 'Ошибка во входных параметрах'
        if(digits["b"] == '0'):
            return 'Ошибка во входных параметрах'
        result = (float(digits['a']) / float(digits['b']))
        return result
    elif(operation == 5):
        if not isnumber(digits["a"]) or not isnumber(digits["b"]):
            return 'Ошибка во входных параметрах'
        if(digits["b"] == '0'):
            return 'Ошибка во входных параметрах'
        result = (float(digits['a']) // float(digits['b']))
        return result
    elif(operation == 6):
        if not isnumber(digits["a"]):
            return 'Ошибка во входных параметрах'
        result = (abs(float(digits['a'])))
        return result
    elif(operation == 7):
        if not isnumber(digits["a"]) or not isnumber(digits["b"]):
            return 'Ошибка во входных параметрах'
        try:
            result = (float(digits['a']) ** float(digits['b']))
        except:
            return 'Слишком большое значение'
        return result
    return

def init():
    print('Введите порядковый номер операции: \n 1. Сложение \n 2. Вычитание \n 3. Умножение \n 4. Деление \n 5. Деление по модулю \n 6. Модуль числа \n 7. Возведение числа в степень')
    operation = input()
    if(operation == '1'):
        print('Введите числа')
        a = input()
        b = input()
        return calculate(1, {'a': a, 'b': b})
    elif(operation == '2'):
        print('Введите числа')
        a = input()
        b = input()
        return calculate(2, {'a': a, 'b': b})
    elif(operation == '3'):
        print('Введите числа')
        a = input()
        b = input()
        return calculate(3, {'a': a, 'b': b})
    elif(operation == '4'):
        print('Введите числа')
        a = input()
        b = input()
        return calculate(4, {'a': a, 'b': b})
    elif(operation == '5'):
        print('Введите числа')
        a = input()
        b = input()
        return calculate(5, {'a': a, 'b': b})
    elif(operation == '6'):
        print('Введите число')
        a = input()
        return calculate(6, {'a': a})
    elif(operation == '7'):
        print('Введите число и степень')
        a = input()
        b = input()
        return calculate(7, {'a': a, 'b': b})
    else:
        return 'Введено неверное значение!'

print (init())