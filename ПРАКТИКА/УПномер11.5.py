def count_numbers(n, k): # функция подсчета количества чисел меньше n и равных k
    count = 0 # счетчик чисел
    for i in range(1, n + 1): # проходим по всем числам
        digit_sum = sum(int(d) for d in str(i)) # получаем сумму цифр
        if i - digit_sum >= k: # если число больше k и равно ему сумме цифр
            count += 1 # увеличиваем счетчик
    return count # возвращаем результат

print(count_numbers(13, 2))
print(count_numbers(10, 5))
print(count_numbers(1, 0))


