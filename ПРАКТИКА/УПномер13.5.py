def binary_search(nums, target):
    left, right = 0, len(nums) - 1 #    
    ascending = nums[0] < nums[-1]  # определяем порядок сортировки
    while left <= right:  # поиск начинается с первого числа и заканчивается последним
        mid = (left + right) // 2  # вычисляем среднее арифметическое деление
        if nums[mid] == target:  # если число найдено, то возвращаем его
            return mid  # возвращаем его
        if ascending:  # если порядок сортировки возрастание, то поиск дальше влево
            if nums[mid] < target:  # если число меньше точки поиска, то поиск дальше влево
                left = mid + 1  # переходим влево
            else:  # если число больше точки поиска, то поиск дальше вправо
                right = mid - 1  # переходим вправо
        else:  # если порядок сортировки убывание, то поиск дальше вправо
            if nums[mid] > target:  # если число больше точки поиска, то поиск дальше вправо
                left = mid + 1  # переходим вправо
            else:  # если число меньше точки поиска, то поиск дальше влево
                rght = mid - 1  # переходим влево
    return -1  # если число не найдено, то возвращаем -1

print(binary_search([10, 20, 30, 40, 50], 20))
print(binary_search([50, 40, 30, 20, 10], 20))
print(binary_search([10, 20, 30, 40, 50], 25))










