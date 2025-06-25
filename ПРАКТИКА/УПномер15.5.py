def k_swaps_to_sort(n, k):
    arr = list(range(1, n + 1)) # создаём список от 1 до n
    for i in range(n - 1, -1, -1): #   перебираем все элементы от n до 1
        move = min(k, n - 1 - i)  # сколько можем сдвинуть вправо
        if move > 0: # если можем сдвинуть вправо
            arr.insert(i + move, arr.pop(i))  # перемещаем элемент
            k -= move # уменьшаем количество сдвигов
        if k == 0: # если количество сдвигов равно нулю
            break # переходим вправо
    return arr # возвращаем список с отсортированными элементами


print(k_swaps_to_sort(5, 3))
print(k_swaps_to_sort(1, 0))
print(k_swaps_to_sort(5, 1))
