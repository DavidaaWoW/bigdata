def isnumber(str):
    try:
        number = float(str)
        result = True
    except ValueError:
        result = False
    return result

def calculateSquareSum(arr):
    sum = 0
    for ar in arr:
        sum += (ar ** 2)
    return sum

def init():
    print('Ввод чисел, пока их сумма не будет равна нулю')
    sum = None
    arr = []
    while (sum != 0):
        a = input()
        if(not isnumber(a)):
            print('Вводить можно только числоа!')
            continue
        a = float(a)
        if(sum == None):
            sum = a
        else:
            sum += a
        arr.append(a)
        print('Сумма чисел: ', sum)
    return calculateSquareSum(arr)

print(init())