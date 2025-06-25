def equal(nums): # функция поиска элемента в списке
    for i, num in enumerate(nums): # проходим по списку и сравниваем каждый элемент с target
        if i == num: # если находим target, то возвращаем его индекс
            return num # возвращаем индекс элемента
    return -1 # если target не найден, то возвращаем -1

print(equal([10, 7, 2]))
print(equal([2, 1, 4, 3]))
print(equal([2, 9, 4, 8]))





















