# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

numbers = list(map(int,input('Введите числа через пробел: ').split()))
# list = [2, 3, 5, 9, 3]
list = [numbers[i] for i in range(1, len(numbers), 2)] 
print(f'Сумма элементов на нечетных позициях =', sum(list))
