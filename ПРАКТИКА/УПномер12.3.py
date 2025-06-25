def max_of_two(a, b): # функция для поиска максимального из двух чисел
    if a < b: # если первое число меньше второго, то возвращаем первое число
        return b # возвращаем первое число
    return a # возвращаем второе число

def max_of_four(a, b, c, d): # функция для поиска максимального из четырех чисел
    if all(x < d for x in [a, b, c]): # если все числа меньше чем d, то возвращаем d
        return d # возвращаем d
    elif all(x < c for x in [a, b, d]): # если все числа меньше чем c, то возвращаем c
        return c # возвращаем c
    elif all(x < b for x in [a, c, d]): # если все числа меньше чем b, то возвращаем b
        return b  # возвращаем b
    return a # возвращаем a


print(max_of_four(4, 9, 10, 5))
print(max_of_four(5, 5, 5, 5))
print(max_of_four(0, -1, -1, 0))








