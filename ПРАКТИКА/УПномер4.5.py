def equation_of_line(values): # values - список значений коэффициентов и столбцов
    if len(values) != 5: # Проверяем число элементов в списке
        return None

    # Вычисляем k (угловой коэффициент)
    k = values[1] - values[0]
    # Проверяем, линейная ли функция
    for i in range(1, len(values)):
        if values[i] - values[i - 1] != k: # Если значение не равно коэффициенту k умноженному на столбец x и сложенному с столбцом y
            return None

    # b — это значение при x = 0
    b = values[0]

    # Формируем строку уравнения
    result = "y = "

    # Добавим часть с k
    if k == 0: # Если коэффициент k равен нулю
        if b == 0: # Если столбец y равен нулю
            return "y = 0" # Возвращаем уравнение y = 0
        return f"y = {b}" if b > 0 else f"y = -{abs(b)}" # В противном случае добавляем столбец y

    if k == 1: # Если коэффициент k равен 1
        result += "x" # Добавляем столбец x
    elif k == -1: # Если коэффициент k равен -1
        result += "-x" # Добавляем столбец x с знаком
    else: # Если коэффициент k равен некоторому числу
        result += f"{k}x" # Добавляем коэффициент k умноженном на столбец x

    # Добавим часть с b
    if b > 0:
        result += f" + {b}" # Добавляем столбец y
    elif b < 0: # Если столбец y меньше нуля
        result += f" - {abs(b)}" # Добавляем столбец y с знаком

    return result # Возвращаем результат


print(equation_of_line([0, 1, 2, 3, 4]))
print(equation_of_line([0, -1, -2, -3, -4]))
print(equation_of_line([0, -2, -4, -6, -8]))
print(equation_of_line([1, 3, 5, 7, 9]))
print(equation_of_line([6, 6, 6, 6, 6]))
print(equation_of_line([1, 1, 2, 2, 2])) 