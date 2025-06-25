def is_function(pairs): # проверяет является ли пара функцией
    seen = {} # словарь для хранения всех элементов
    for x, y in pairs: # перебираем пары
        if x in seen: # если элемент уже в словаре
            if seen[x] != y: # и если значение не равно
                return False # возвращаем ложь
        else: # если элемент не в словаре
            seen[x] = y # добавляем в словарь
    return True # все прошло хорошо, возвращаем истину

print(is_function([(1, 3), (2, 5), (1, 7)]))
print(is_function([(1, 3)]))
print(is_function([(1, 3), (2, 5), (3, 7)]))