def bubble_sort(nums):
    n = len(nums) # длина списка
    for i in range(n): # первый проход: выносим все ненули в начало
        swapped = False  # были ли перестановки на этой итерации
        for j in range(0, n - 1 - i):  # каждый раз до конца-1-i
            if nums[j] < nums[j + 1]:  # меняем местами, если "не по убыванию"
                nums[j], nums[j + 1] = nums[j + 1], nums[j] # Обмениваем минимум на позицию i
                swapped = True # флаг: были ли перестановки на этой итерации
        if not swapped:  # если ничего не поменяли — значит, уже отсортировано
            break # переходим вправо


nums = [3, 4, 1, 2, 5]
bubble_sort(nums)
print(nums)

nums = [3, 2, 2, 1, 3, 3]
bubble_sort(nums)
print(nums)

nums = [1]
bubble_sort(nums)
print(nums)

