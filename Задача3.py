# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


n = [2, 5, 7, 8, 9, 2, 5, 8, 9, 4, 7]
n = set(n)
n = list(n)
print(n)


d = [1, 2, 2, 2, 2, 3, 4, 4, 7, 0, 10]
newList = []
for i in range(len(d)):
    trueFalse = True
    for j in range(len(d)):
        if i != j:
            if d[i] == d[j]:
                trueFalse = False
                break
    if trueFalse: newList += [d[i]]
print(newList)