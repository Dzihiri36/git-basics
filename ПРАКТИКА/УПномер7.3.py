def mystery(n: int) -> int: # функция получения количества четных чисел меньше n
    count = 0 # счетчик
    for i in range(1, n+1): # если i может делить n
        if n % i == 0: # если n делится на i и равно 0
            count += 1 # увеличиваем счетчик
    return count * 2 # возвращаем результат умноженный на 2

print(mystery(1))
print(mystery(2))
print(mystery(3))










