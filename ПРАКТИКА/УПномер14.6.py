def alter_sort(nums):
 
    n = len(nums) # длина списка
    for i in range(n): # первый проход: выносим все ненули в начало
        max_idx = i # начало индекса нашего списка
        for j in range(i + 1, n): # поиск максимального элемента
            if nums[j] > nums[max_idx]: # если элемент списка равен target, то возвращаем True
                max_idx = j # переходим влево
        nums[i], nums[max_idx] = nums[max_idx], nums[i] # Обмениваем минимум на позицию i

    #собираем попеременно максимум и минимум
    result = [] # создаем пустой список
    left = 0  # указывает на следующий максимум
    right = n - 1 # указывает на следующий минимум

    while left <= right: # поиск начинается с первого элемента и заканчивается последним
        result.append(nums[left]) # добавляем максимум в начало
        left += 1 # увеличиваем индекс двойкой
        if left <= right: # если максимум не стоит в конце, то добавляем его
            result.append(nums[right]) # добавляем минимум в конец
            right -= 1 # уменьшаем индекс двойкой

    nums[:] = result # меняем содержимое nums на result


nums = [1, 2, 3, 4, 5]
alter_sort(nums)
print(nums)

nums = [5, 4, 3, 2, 1]
alter_sort(nums)
print(nums)

nums = [1, 1, 1]
alter_sort(nums)
print(nums)

