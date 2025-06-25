def binary_search(nums, target):
    left = 0 # начало поиска
    right = len(nums) - 1 # конец поиска
    while left <= right:  # поиск начинается с первого числа и заканчивается последним
        mid = (left + right) // 2 # вычисляем среднее арифметическое деление
        if nums[mid] == target:  # если число найдено, то возвращаем его
            return mid # возвращаем его
        elif nums[mid] < target: # если число меньше точки поиска, то поиск дальше влево
            left = mid + 1 # переходим влево
        else: # если число больше точки поиска, то поиск дальше вправо
            right = mid - 1 # переходим вправо
    return -1 # если число не найдено, то возвращаем -1

print(binary_search([10, 20, 30, 40, 50], 40))
print(binary_search([10, 20, 30, 40, 50], 60))
print(binary_search([1, 2, 3, 4, 5], 1))