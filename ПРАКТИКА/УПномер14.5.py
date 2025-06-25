def sort_like_nums(nums):
    def get_value(x): # функция для получения значения из списка
        return x[0] if isinstance(x, list) else x # если элемент списка равен target, то возвращаем True
 
    def is_greater(a, b): # функция для получения значения из списка
        val_a = get_value(a) # получаем значение из списка
        val_b = get_value(b) # получаем значение из списка

        if val_a != val_b: # если значения равны: число < список
            return val_a > val_b # возвращаем True
        else: # если значения равны: число < список
            
            return isinstance(a, list) and not isinstance(b, list) # возвращаем True

    n = len(nums) # длина списка
    for i in range(n): # первый проход: выносим все ненули в начало
        min_idx = i # начало индекса нашего списка
        for j in range(i + 1, n): # поиск максимального элемента
            if is_greater(nums[min_idx], nums[j]): # если элемент списка равен target, то возвращаем True
                min_idx = j # переходим влево
        nums[i], nums[min_idx] = nums[min_idx], nums[i] # Обмениваем минимум на позицию i


nums = [[4], 3, 2, [5], [1]]
sort_like_nums(nums)
print(nums)

nums = [2, 1, [2], 3, [3]]
sort_like_nums(nums)
print(nums)

nums = [[1]]
sort_like_nums(nums)
print(nums)

