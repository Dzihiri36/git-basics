def search_insert_position(nums, target): # поиск элемента в списке по индексу
    for index, num in enumerate(nums): # проходим по списку и сравниваем каждый элемент с target
        if num == target: # если находим target, то возвращаем его индекс
            return index # возвращаем индекс элемента

    nums.append(target) # добавляем target в конец списка
    nums = sorted(nums) # сортируем список
 
    return nums.index(target) # возвращаем индекс элемента

print(search_insert_position([1, 2, 3, 4, 5], 5))
print(search_insert_position([1, 2, 3, 4, 5], 6))
print(search_insert_position([1, 2, 4, 5], 3))












