def nine_divisors(n): # функция подсчета количества чисел на которые делится на 9, меньше n
    lst_num_nine_divisors = [] # список чисел на которые делится на 9
    for num in range(1, n + 1): # проходим по всем числам
        counter = 0 # счетчик делителей
        for i in range(1, num + 1): # проходим по всем числам
            if num % i == 0: # если число делится на i
                counter += 1 # увеличиваем счетчик
        if counter == 9: # если счетчик равен 9
            lst_num_nine_divisors.append(num) # добавляем число в список

    return len(lst_num_nine_divisors) # возвращаем результат

print(nine_divisors(100))
print(nine_divisors(10))
print(nine_divisors(50))











