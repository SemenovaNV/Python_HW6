# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

numbers = list(map(int,input('Введите числа через пробел: ').split()))
# print(f'Исходный список {numbers}')
unic_num = list(filter(lambda x: numbers.count(x)==1, numbers))
print(f'Неповторяющиеся элементы {unic_num}')