def max_to_min(nums): # функция для поиска максимального из четырех чисел
    max_num = max(nums) # получаем максимальное число
    while max_num == max(nums):  # проходим по всем числам и сравниваем каждый число с максимальным
        if max(nums) == min(nums): # если максимальное число равно минимальному, то возвращаем результат
            break # выходим из цикла
        nums[nums.index(max_num)] = min(nums) # меняем максимальное число на минимальное


data = [1, 3, 3, 3, 4]
max_to_min(data)
print(data)

data = [5, 4, 2, -2, 4, 2, 2, 5]
max_to_min(data)
print(data)

data = [1]
max_to_min(data)
print(data)

data = [1, 2, 1, 2, 1, 2]
max_to_min(data)
print(data)

data = [1, 1, 1, -1, 1, 1, 0]
max_to_min(data)
print(data)

data = [1, 1]
max_to_min(data)
print(data)










