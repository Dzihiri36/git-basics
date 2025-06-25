def hamming_distance(s1, s2): #
    count = 0 # счетчик отличий
    for i in range(len(s1)): # проходим по всем символам
        if s1[i] != s2[i]: # если символы не равны
            count += 1 # увеличиваем счетчик
            
    return count # возвращаем результат

print(hamming_distance('abbcace', 'abacacc'))  
print(hamming_distance('beegeek', 'beegeek'))  
print(hamming_distance('abcd', 'efgh'))