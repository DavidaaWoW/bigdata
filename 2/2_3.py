import numpy as np

def getMatrix(size):
    return np.random.randint(0, 10, size=(size, size))

def getVectorFromMatrix(matrix):
    vector = []
    for i in range(matrix.shape[0]):
        for j in range(len(matrix[i])):
            vector.append(matrix[i][j])
    return vector

def init():
    print('Введите размерность матрицы')
    digit = input()
    if(not digit.isdigit):
        return ('Неправильный ввод')
    digit = int(digit)
    if(int(digit) < 0):
        return ('Неправильный ввод')
    
    matrix = getMatrix(digit)
    print(matrix)
    return getVectorFromMatrix(matrix)

print(init())