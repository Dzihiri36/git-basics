def time_zone(h, a, b): # функция обработки числа
 
    arthur_time = h + (b - a) # вычисляем время 
    return arthur_time % 24 # возвращаем результат остаток от деления на 24

print(time_zone(12, 3, 7))
print(time_zone(12, -4, 4))
print(time_zone(12, 0, 0))

















