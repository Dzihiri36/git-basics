def linear_search(nums, target, reverse=False): # Поиск элемента в списке по индексу
    if not reverse: # Если не указано переворот списка, то просто ищем элемент в обычном порядке
        for i, num in enumerate(nums): # Проходим по списку и сравниваем каждый элемент с target
            if num == target: # Если находим target, то возвращаем его индекс
                return i # Возвращаем индекс элемента
        return -1 # Если target не найден, то возвращаем -1
    else: # Если указано переворот списка, то просто ищем элемент в обратном порядке
        for i in range(len(nums) - 1, -1, -1): # Проходим по списку и сравниваем каждый элемент с target
            if nums[i] == target: # Если находим target, то возвращаем его индекс
                return i # Возвращаем индекс элемента
        return -1 # Если target не найден, то возвращаем -1

print(linear_search([1, 5, 7], 5))
print(linear_search([2, 1, 7, 2], 2))
print(linear_search([12, 4, 1], 9))




