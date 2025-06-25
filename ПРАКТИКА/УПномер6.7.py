def drop_one_and_five(n): # функция обработки числа
    result = 0 # результат обработки
    multiplier = 1 # счетчик длины результата
    while n > 0: # пока не станет равен 0
        digit = n % 10 # получаем последнюю цифру
        n //= 10 # уменьшаем число на 10
        if digit != 1 and digit != 5: # если цифра не равна 1 и 5
            result += digit * multiplier # вычисляем сумму с последней цифрой
            multiplier *= 10 # умножаем на 10
    return result # возвращаем результат

print(drop_one_and_five(527012))
print(drop_one_and_five(2468))
print(drop_one_and_five(0))









