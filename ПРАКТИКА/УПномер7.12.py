def divisible(n): 
    count = 0 # счетчик делителей
    x = abs(n) # если n отрицательный, приводим его к положительному
    
    while x > 0: # проходим по всем цифрам
        digit = x % 10 # получаем текущую цифру
        if digit != 0 and n % digit == 0: # если цифра не равна 0, и n делится на неё
            count += 1 # увеличиваем счетчик делителей
        x //= 10 # умножаем на делитель
    
    return count # возвращаем результат

print(divisible(22))   
print(divisible(500))   
print(divisible(1))    