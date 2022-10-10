# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def simpleMulti(n):
    newList = []
    numValue = 2
    if n == 1:
        return 1
    else:
        while n > 1:
            if n % numValue == 0:
                newList += [numValue]
                n //= numValue
                numValue = 2
            else:
                numValue += 1
        return newList

n = int(input('Введите натуральное число: '))
print(f'Список простых множителей числа {n} = {simpleMulti(n)}')

# Если нужен список уникальных простых множителей, то к решению добавляю:
print(f'Список простых множителей числа {n} = {list(set(simpleMulti(n)))}')

