def make_palindrome(n): 
    def reverse_num(x): # функция получения обратного числа
        rev = 0 # счетчик обратного числа
        while x > 0: # проходим по всем цифрам
            rev = rev * 10 + x % 10 # умножаем на делитель
            x //= 10 # если x отрицательный, приводим его к положительному
        return rev # возвращаем результат

    def is_palindrome(x): # функция проверки на палиндром
        return x == reverse_num(x) # если x равен обратному числу, возвращаем True

    if is_palindrome(n): # если число палиндром
        return n # возвращаем число

    current = n # сохраняем число
    for _ in range(5): # проходим по всем цифрам
        current += reverse_num(current) # увеличиваем число на обратное
        if is_palindrome(current): # если число палиндром
            return current # возвращаем числo
    return -1 # возвращаем -1

print(make_palindrome(101))   
print(make_palindrome(23))    
print(make_palindrome(196))   