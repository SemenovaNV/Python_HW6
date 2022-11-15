# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

from math import factorial

number = int(input('Введите целое число: '))
f = lambda x:((x == 1) and 1) or x * factorial(x -1)
list = list(f(i) for i in range(1, number +1))
print(list)