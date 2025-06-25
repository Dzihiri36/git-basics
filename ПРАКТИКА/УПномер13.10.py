def is_value(values, target): 
    if values[0] == target: # если первый элемент списка равен target, то возвращаем True
        return True # возвращаем True
    i = 1 # начало индекса нашего списка
    while i < len(values) and values[i] > target: # поиск начинается с первого элемента и заканчивается последним
        i *= 2 # увеличиваем индекс двойкой


    left = i // 2 # начало предыдущей степени двойки
    right = min(i, len(values) - 1) # конец предыдущей степени двойки

    while left <= right: # поиск начинается с первого элемента и заканчивается последним
        mid = (left + right) // 2  # вычисляем среднее арифметическое деление
        if values[mid] == target: # если элемент списка равен target, то возвращаем True
            return True # возвращаем True
        elif values[mid] > target: # список по убыванию — больше значит "слева"
            left = mid + 1 # переходим влево
        else: # список по возрастанию — меньше значит "справа"
            right = mid - 1 # переходим вправо

    return False   # если элемент не найден, то возвращаем False


values1 = [4, -3, -10, -17, -24, -31, -38, -45]
values2 = [1, 0, -3, -8, -15, -24, -35, -48, -63, -80, -99, -120, -143, -168]

print(is_value(values1, -17))      
print(is_value(values1, 100))       
print(is_value(values1, 4))         
