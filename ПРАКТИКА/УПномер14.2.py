def selection_sort(nums): 
    n = len(nums) # длина списка
    for i in range(n): # первый проход: выносим все ненули в начало
        max_idx = i # начало индекса нашего списка
        for j in range(i + 1, n): # поиск максимального элемента
            if nums[j] > nums[max_idx]: # если элемент списка равен target, то возвращаем True
                max_idx = j # переходим влево
        nums[i], nums[max_idx] = nums[max_idx], nums[i] # Обмениваем минимум на позицию i


nums = [3, 4, 1, 2, 5]
selection_sort(nums)
print(nums)

nums = [3, 2, 2, 1, 3, 3]
selection_sort(nums)
print(nums)

nums = [1]
selection_sort(nums)
print(nums)

