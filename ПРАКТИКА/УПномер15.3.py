def number_of_swaps(nums):
    count = 0 # счётчик подстановок
    temp = nums[:]  # создаём копию, чтобы не портить оригинал
    n = len(temp) # длина списка

    for i in range(n): # первый проход: выносим все ненули в начало
        for j in range(0, n - 1 - i): # каждый раз до конца-1-i
            if temp[j] > temp[j + 1]: # меняем местами, если "не по убыванию"
                temp[j], temp[j + 1] = temp[j + 1], temp[j] # Обмениваем минимум на позицию i
                count += 1 # увеличиваем счётчик подстановок
    return count # возвращаем счётчик подстановок

print(number_of_swaps([1, 2, 4, 3, 5]))
print(number_of_swaps([2, 1, 4, 3, 5]))
print(number_of_swaps([1, 2, 3, 4, 5]))
