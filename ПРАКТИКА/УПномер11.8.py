def find_peaks(nums): # функция поиска пиков
    counter = 0 # счетчик пиков
    for i in range(1, len(nums)  - 1): # проходим по всем элементам
        if nums[i] > nums[i-1] and nums[i] > nums [i+1]: # если три элемента больше друг друга
            counter += 1 # увеличиваем счетчик

    return counter # возвращаем результат

print(find_peaks([16, 7, 18, 12, 13, 11, 19, 9, 10, 6]))
print(find_peaks([1, -1, 1, -2, 2, -2, -3, 3, -3]))
print(find_peaks([3, 1, 3]))









