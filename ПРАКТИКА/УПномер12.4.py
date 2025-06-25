def golden_pairs(pairs): 
    counter = 0 # счетчик пар
    for pair in pairs: # проходим по всем парам
        if 1.6 <= (max(pair) / min(pair)) <= 1.7: # если соотношение между числами больше или равно 1.6 и меньше или равно 1.7
            counter += 1 # увеличиваем счетчик
    return counter # возвращаем результат

print(golden_pairs([(100, 165), (180, 100), (170, 100), (100, 160)]))
print(golden_pairs([(1, 10), (10, 1), (2, 5), (7, 4)]))
print(golden_pairs([(1, 1), (2, 2), (3, 3), (4, 4)]))
















