# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

numbers = list(map(float, input('Введите числа списка через пробел: ').split()))
res = list(map((lambda x: x - (x * 10 // 10)), numbers))
print(f'Разница между max и min значением дробной части элементов: {round(max(res) - min(res), 2)}')