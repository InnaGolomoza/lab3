"""Напишіть програму для отримання рядка Фібоначчі від 0 до n, де n - ціле число.
Послідовність Фібоначчі - це серія чисел 0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
Кожне наступне число знайдено шляхом додавання двох чисел перед ним.
Голомоза Інна Андріївна"""

n = int(input("Введіть кількість чисел Фібоначчі (n): "))

# Ініціалізація змінних
a = 1
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
