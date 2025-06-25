def is_point_in_rectangle(p, rect): # функция
    x, y = p # переменные
    (x1, y1), (x2, y2) = rect # разбивка пары на две переменные
    # Проверяем, что точка внутри по x и по y строго между границами прямоугольника
    if x1 < x < x2 and y1 < y < y2: # если точка внутри по x и по y строго между границами прямоугольника
        return True # возвращаем True
    else: # если точка не внутри по x и по y строго между границами прямоугольника
        return False # возвращаем False


print(is_point_in_rectangle((1, 0), [(1, 1), (3, 4)]))
print(is_point_in_rectangle((2, 2), [(1, 1), (3, 4)]))
print(is_point_in_rectangle((2, 1), [(1, 1), (3, 4)]))
print(is_point_in_rectangle((0, 0), [(-1, -1), (3, 3)]))





























