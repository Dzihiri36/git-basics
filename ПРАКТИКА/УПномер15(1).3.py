def binary_insertion_sort(nums): # функция для сортировки в отсортированном порядке
    def binary_search(arr, val, start, end): # функция для поиска места для вставки val в отсортированной части от start до end
   
        while start < end: # поиск начинается с первого элемента и заканчивается последним 
            mid = (start + end) // 2  # вычисляем среднее арифметическое деление
            mid = (start + end) // 2  # вычисляем среднее арифметическое деление
            if arr[mid] < val: # если элемент списка равен target, то возвращаем True
                start = mid + 1 # переходим влево
            else: # список по убыванию — больше значит "слева"
                end = mid # переходим вправо
        return start # возвращаем найденный минимальный элемент
 
    for i in range(1, len(nums)): # первый проход: выносим все ненули в начало
        key = nums[i] # получаем значение из списка
        pos = binary_search(nums, key, 0, i) # поиск места для вставки val в отсортированной части от start до end
      
        nums[pos + 1:i + 1] = nums[pos:i] # обмениваем минимум на позицию i
        nums[pos] = key 


nums = [3, 4, 1, 2, 5]
binary_insertion_sort(nums)
print(nums)

nums = [3, 2, 2, 1, 3, 3]
binary_insertion_sort(nums)
print(nums)

nums = [1]
binary_insertion_sort(nums)
print(nums)

