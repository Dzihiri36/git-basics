def longest_substring_without_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'} # список волчебных символов
    max_length = 0 # максимальная длина подстроки
    current_length = 0 # текущая длина подстроки
    
    for char in s: # проходим по всем символам
        if char in vowels: # если символ волчебный
            if current_length > max_length: # если длина подстроки больше максимальной
                max_length = current_length # обновляем максимальную длину
            current_length = 0 # сбрасываем длину подстроки   
        else: # если символ не волчебный
            current_length += 1 # увеличиваем длину подстроки
             
    if current_length > max_length:  # если длина подстроки больше максимальной
        max_length = current_length # обновляем максимальную длину
        
    return max_length # возвращаем результат

print(longest_substring_without_vowels('abcdefg'))       
print(longest_substring_without_vowels('bcdgf'))         
print(longest_substring_without_vowels('aeiou'))         
