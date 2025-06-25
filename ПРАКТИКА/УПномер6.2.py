def mid_num(a, b, c): # функция получения среднего по величине числа
    numbers = [a, b, c] # список чисел
    numbers.sort() # сортировка списка
    return numbers[1] # возвращаемое значение

print(mid_num(1, 2, 3))
print(mid_num(-2, -3, -1))
print(mid_num(7, 7, 7))



