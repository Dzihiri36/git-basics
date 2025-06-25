def avg_values(nums):
    result = [] # список результатов
    total = 0 # сумма всех чисел

    for i, num in enumerate(nums, start=1): # проходим по всем числам
        total += num  # увеличиваем сумму на текущее число
        result.append(total / i) # добавляем результат в список

    return result # возвращаем результат

print(avg_values([10, 20, 30, 40, 50]))  
print(avg_values([1, 1, 1, 1, 1]))       
print(avg_values([-2, -3, 5, 5]))   