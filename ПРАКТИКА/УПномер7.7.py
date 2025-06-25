def even_odd(nums): # функция проверяет четность натуральных чисел
    if not nums: # если список пуст
        return True # возвращаем True
    
    first_parity = nums[0] % 2 # получаем первое число с нечётностью
    for num in nums: # проходим по всем числам
        if num % 2 != first_parity: # если число не имеет то же нечётность
            return False # возвращаем False
        
    return True # все числа имеют одинаковую нечётность, возвращаем True

print(even_odd([-2, 4, -6, 8]))    
print(even_odd([1, 3, 4]))         
print(even_odd([0, 0, 0]))  









