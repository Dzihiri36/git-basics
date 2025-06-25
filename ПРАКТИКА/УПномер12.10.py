def min_product_of_two(nums): # функция для поиска минимального произведения двух чисел
    lst = [] # создаем список для хранения результата
    for ind1 in range(len(nums)): # проходим по всем числам
        for ind2 in range(ind1 + 1, len(nums)): # проходим по всем числам остальным
           lst.append(nums[ind1] * nums[ind2]) # сохраняем произведение двух чисел в список

    return min(lst) # возвращаем минимальное значение из списка


print(min_product_of_two([5, 2, 6, 1, 7]))
print(min_product_of_two([1, 1, 1, 1, 1]))
print(min_product_of_two([5, 4, 3, 2, 1]))











