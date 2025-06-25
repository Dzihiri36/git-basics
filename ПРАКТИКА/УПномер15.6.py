def cocktail_sort(nums):
    n = len(nums) # длина списка
    left = 0  # указывает на следующий максимум
    right = n - 1 # указывает на следующий минимум
    swapped = True # флаг: были ли перестановки на этой итерации

    while swapped: # поиск начинается с первого элемента и заканчивается последним
        swapped = False  # были ли перестановки на этой итерации

        for i in range(left, right):    # каждый раз до конца-1-i
            if nums[i] > nums[i + 1]:  # меняем местами, если "не по убыванию"
                nums[i], nums[i + 1] = nums[i + 1], nums[i] # Обмениваем минимум на позицию i
                swapped = True # флаг: были ли перестановки на этой итерации
        right -= 1 # уменьшаем индекс двойкой
 
        if not swapped: # если ничего не поменяли — значит, уже отсортировано
            break # переходим вправо

        swapped = False  # были ли перестановки на этой итерации
 
        for i in range(right, left, -1):  # каждый раз до конца-1-i
            if nums[i] < nums[i - 1]: # меняем местами, если "не по убыванию"
                nums[i], nums[i - 1] = nums[i - 1], nums[i] # Обмениваем минимум на позицию i
                swapped = True # флаг: были ли перестановки на этой итерации
        left += 1 # увеличиваем индекс двойкой


data = [8, 9, 6, 5, 7, 4, 1, 2, 3]
cocktail_sort(data)
print(data)

data = [5, 4, 3, -2, 1]
cocktail_sort(data)
print(data)

data = [3]
cocktail_sort(data)
print(data)

