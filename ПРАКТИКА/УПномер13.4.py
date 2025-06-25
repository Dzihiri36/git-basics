def bounded_binary_search(nums, target, left=None, right=None): # функция для поиска числа в отведенном интервале
    if left is None:  # если не указан левый границы
        left = 0  # по умолчанию он равен 0
    if right is None:  # если не указан правый границы
        right = len(nums) - 1  # по умолчанию он равен длине списка

    while left <= right:  # поиск начинается с первого числа и заканчивается последним
        mid = (left + right) // 2  # вычисляем среднее арифметическое деление
        if nums[mid] == target:  # если число найдено, то возвращаем его
            return mid  # возвращаем его
        elif nums[mid] < target:  # список по убыванию — больше значит "слева"
            left = mid + 1  # переходим влево
        else:  # список по возрастанию — меньше значит "справа"
            right = mid - 1  # переходим вправо
    return -1  # если число не найдено, то возвращаем -14

print(bounded_binary_search([10, 20, 30, 40, 50], 60, left=0, right=4))
print(bounded_binary_search([1, 3, 5, 7, 9], 5, 1, 3))
print(bounded_binary_search([1, 3, 5, 7, 9], 5, 0, 1))
print(bounded_binary_search([10, 20, 30, 40, 50], 40))

















