
def swap_digits(n): # функция обработки числа
    first_digit = n // 100 # получаем первую цифру
    midd_ledigit = (n // 10) % 10 # получаем среднюю цифру
    lastdigit = n % 10 # получаем последнюю цифру
    return lastdigit * 100 + midd_ledigit * 10 + first_digit # возвращаем результат

print(swap_digits(123))
print(swap_digits(321))
print(swap_digits(555))









