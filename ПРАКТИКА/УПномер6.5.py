def training_time(n, m, s, b): # функция обработки числа

    total_seconds = n * (m * 60 + s) + (n - 1) * b # пересчитываем время
    total_minutes = total_seconds // 60 # целочисленное деление на 60
    remaining_seconds = total_seconds % 60 # остаток от деления на 60
    return (total_minutes, remaining_seconds) # возвращаем результат

print(training_time(3, 2, 10, 90))
print(training_time(1, 1, 0, 0))
print(training_time(1, 0, 1, 0))












