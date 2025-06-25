import math # модуль для работы с числами

def triangle_of_coins(n): # функция для поиска количества монет в треугольнике
    return int((math.isqrt(1 + 8 * n) - 1) // 2) # возвращаем количество монет в треугольнике


print(triangle_of_coins(3))
print(triangle_of_coins(5))
print(triangle_of_coins(6))








