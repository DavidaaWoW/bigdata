def getNumberOutput(digit):
    list_ = []
    for i in range(digit):
        for j in range(i):
            if(len(list_) == digit):
                return list_
            list_.append(i)
    return list_

def init():
    print('Введите целое неотрицательное число')
    digit = input()
    if(not digit.isdigit):
        return ('Неправильный ввод')
    digit = int(digit)
    if(int(digit) < 0):
        return ('Неправильный ввод')
    return getNumberOutput(digit)

print(init())
    
