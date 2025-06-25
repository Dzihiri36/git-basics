def check_letters(s: str): # функция проверки на буквы
    simbols = ['0' for x in range(26)] # список символов
    for letter in s: # проходим по всем символам
        if 97 <= ord(letter.lower()) <= 122: # если символ в диапазоне a-z
            index_letter = ord(letter.lower()) - 97 # вычисляем индекс символа
            simbols[index_letter] = '1' # заполняем список на все буквы с значением 1
 
    return ''.join(simbols) # возвращаем результат

print(check_letters('ABcd'))
print(check_letters('A-Z'))
print(check_letters('b*e*e*g*e*e*k'))
