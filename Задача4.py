# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
#
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0


import random

def fillListRandom(size: int):
    lisrStr = []
    for i in range(size):
        lisrStr.append(random.randrange(0, 100))
    return lisrStr

k = int(input('Введите число степени (от 1 и больше): '))
if k < 1:
    print('Введите число от 1!')
else:
    newList = fillListRandom(k + 1)
    print(newList)
    newStr = ''
    indexList = k + 1
    coeff = 1
    for i in range(k + 1):
        if i == 0:
            indexList -= 1
            newStr = str(newList[indexList]) + ' = 0' + newStr
        elif i == 1:
            indexList -= 1
            newStr = str(newList[indexList]) + '*x + ' + newStr
        else:
            indexList -= 1
            coeff += 1
            newStr = str(newList[indexList]) + '*x^' + str(coeff) + ' + ' + newStr
    print(newStr)

    path = 'task4.4.txt'
    with open(path, 'w') as f:
        f.write(newStr)

