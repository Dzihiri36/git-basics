def linear_coefficients(p1, p2): # p1 - первая точка, p2 - вторая точка
 
    x1, y1 = p1 # x1, y1 - координаты первой точки
    x2, y2 = p2 # x2, y2 - координаты второй точки

    if x1 == x2: # Если координаты первой и второй точки равны
        return None # возвращаем None

    k = (y2 - y1) / (x2 - x1) # Вычисляем коэффициент k
    b = y1 - k * x1 # Вычисляем сдвиг b
    return (k, b) # возвращаем коэффициент и сдвиг

print(linear_coefficients((1, 2), (2, 3)))   
print(linear_coefficients((0, 0), (1, 5)))
print(linear_coefficients((0, 2), (2, 2)))











