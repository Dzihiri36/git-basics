def binary_search(nums, target):
    left = 0  # начало поиска
    right = len(nums) - 1  # конец поиска
    while left <= right:  # поиск начинается с первого числа и заканчивается последним
        mid = (left + right) // 2  # вычисляем среднее арифметическое деление
        if nums[mid] == target:  # если число найдено, то возвращаем его
            return mid  # возвращаем его
        elif nums[mid] > target:  # список по убыванию — больше значит "слева"
            left = mid + 1  # переходим влево
        else:  # список по возрастанию — меньше значит "справа"
            right = mid - 1  # переходим вправо
    return -1  # если число не найдено, то возвращаем -1

print(binary_search([50, 40, 30, 20, 10], 30))
print(binary_search([50, 40, 30, 20, 10], 0))
print(binary_search([5, 4, 3, 2, 1], 5))











