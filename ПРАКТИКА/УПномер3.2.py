def get_quadrant(p): # функция
    x, y = p # переменные
    if x > 0 and y > 0: # если x > 0 и y > 0
        return 1 # возвращаем 1
    elif x < 0 and y > 0: # если x < 0 и y > 0
        return 2 # возвращаем 2
    elif x < 0 and y < 0: # если x < 0 и y < 0
        return 3 # возвращаем 3
    elif x > 0 and y < 0: # если x > 0 и y < 0
        return 4 # возвращаем 4
    else: # если ни одно из условий не выполняется
        return None # возвращаем None


print(get_quadrant((3, 4)))
print(get_quadrant((-1, 2)))
print(get_quadrant((-3, -5)))
print(get_quadrant((5, 0)))




























