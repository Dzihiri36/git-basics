def max_guests(n, m): # n — общее количество этажей в гостинице
   
    if not (1 <= n <= 1000 and 1 <= m <= 1000): # Проверка на вхождение в диапазон
        return 0 # Если нет, то возвращаем 0

    return (n - 1) * m * 3 # расчет результата

print(max_guests(5, 10))
print(max_guests(10, 10))
print(max_guests(2, 5))












