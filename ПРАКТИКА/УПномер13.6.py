def binarysearchrow(row, target):
    left, right = 0, len(row) - 1 # начало и конец поиска
    while left <= right:  # поиск начинается с первого числа и заканчивается последним
        mid = (left + right) // 2  # вычисляем среднее арифметическое деление
        if row[mid] == target:  # если число найдено, то возвращаем True
            return True  # возвращаем True
        elif row[mid] < target:  # список по убыванию — больше значит "слева"
            left = mid + 1  # переходим влево
        else:  # список по возрастанию — меньше значит "справа"
            right = mid - 1  # переходим вправо
    return False  # если число не найдено, то возвращаем False

def matrix_search(matrix, target): # функция для поиска числа в матрице
    for row in matrix: # перебираем все строки
        if binarysearchrow(row, target): # если число найдено, то возвращаем True
            return True # возвращаем True
    return False # если число не найдено, то возвращаем False

data = [[2, 4, 6],
        [1, 3, 5],
        [7, 8, 9]]
        
print(matrix_search(data, 5))


data = [[2, 4, 6],
        [1, 3, 5],
        [7, 8, 9]]
        
print(matrix_search(data, 0))
data = [[1]]

print(matrix_search(data, 1))


