
def calculate(vars, values, exp): # Создаем словарь соответствия переменных их значениям
    mapping = {var: val for var, val in zip(vars, values)} # Заменяем переменные на их значения в выражении
    expr = ''
    for ch in exp:
        if ch in mapping:
            expr += str(mapping[ch]) # Вычисляем значение выражения и возвращаем результат
        else:
            expr += ch # Вычисляем значение выражения и возвращаем результат
    return eval(expr)

print(calculate('xyz', [1, 2, 3], 'x-y+z'))             # 1 - 2 + 3 = 2
print(calculate('dbcw', [3, 0, -2, -3], '-d-c-b+w'))    # -3 - (-2) - 0 - 3 = -4
print(calculate('abcd', [0, 0, 0, 0], 'a+b+c+d'))       # 0 + 0 + 0 + 0 = 0
print(calculate('a', [4], 'a'))                         # 4 = 4