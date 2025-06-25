def sort_by_digit_and_value(nums):
    n = len(nums) # длина списка
    for i in range(n):  # Первый проход: выносим все ненули в начало
        max_idx = i  # начало индекса нашего списка
        for j in range(i + 1, n):  # Поиск максимального элемента
            
            last_i = abs(nums[max_idx]) % 10 # получаем последний цифры из максимального элемента
            last_j = abs(nums[j]) % 10 # получаем последний цифры из элемента
            if last_j > last_i: # если элемент списка равен target, то возвращаем True
                max_idx = j # переходим влево
            elif last_j == last_i and nums[j] < nums[max_idx]: # если элемент списка равен target, то возвращаем True
                max_idx = j # переходим влево
        nums[i], nums[max_idx] = nums[max_idx], nums[i]  # Меняем местами


nums = [5, 11, 183, 19, 274]
sort_by_digit_and_value(nums)
print(nums)

nums = [5, 11, 185, 19, 271]
sort_by_digit_and_value(nums)
print(nums)

nums = [1]
sort_by_digit_and_value(nums)
print(nums)

