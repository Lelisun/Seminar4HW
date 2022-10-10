# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
#
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0


path = 'task4.5.1.txt'
path2 = 'task4.5.2.txt'
strOne = ''
strTwo = ''
with open(path, 'r') as f: strOne = f.readline()
with open(path2, 'r') as f: strTwo = f.readline()

if len(strOne) > len(strTwo):
    helpStr = strOne
    strOne = strTwo
    strTwo = helpStr
strOne = strOne.split(' + ')
strTwo = strTwo.split(' + ')
print(strOne, strTwo)

countOne = 0
countTwo = len(strTwo) - len(strOne)
newStr = ''
for i in range(countTwo):
    newStr += strTwo[i] + ' + '

numberOne = ''
numberTwo = ''
for i in range(len(strTwo) - len(strOne), len(strTwo)):
    result = 0
    if i == len(strTwo) - 1:
        result += int(strOne[-1][:-4]) + int(strTwo[-1][:-4])
        newStr += str(result) + strOne[-1][-4:]
    elif i == len(strTwo) - 2:
        result += int(strOne[-2][:-2]) + int(strTwo[-2][:-2])
        newStr += str(result) + strOne[-2][-2:] + ' + '
    else:
        result += int(strOne[countOne][:-4]) + int(strTwo[countTwo][:-4])
        newStr += str(result) + strOne[countOne][-4:] + ' + '
        countOne += 1
        countTwo += 1
print(newStr)

pathThree = 'task.5.3.txt'
with open(pathThree, 'w') as f:
    f.writelines(newStr)