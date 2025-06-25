def sum_of_seven_smallest(nums):
    n = len(nums) # длина списка
    for i in range(7):  # Только первые 7 шагов сортировки
        min_idx = i # начало индекса нашего списка
        for j in range(i + 1, n): # поиск максимального элемента
            if nums[j] < nums[min_idx]: # если элемент списка равен target, то возвращаем True
                min_idx = j # переходим влево
        nums[i], nums[min_idx] = nums[min_idx], nums[i]  # Обмениваем минимум на позицию i

    return sum(nums[:7]) # возвращаем сумму первых 7 элементов


print(sum_of_seven_smallest([2, 7, 3, 6, 10, 4, 1, 9, 5, 8])) 
print(sum_of_seven_smallest([2, 2, 4, 1, 3, 3, 5, 4, 4]))
print(sum_of_seven_smallest([1, 1, 1, 1, 1, 1, 1, 1]))
