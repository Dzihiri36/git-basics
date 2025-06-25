def sort_binary_list(binary_list):
    count_zeros = binary_list.count(0)
    count_ones = len(binary_list) - count_zeros

    # Обновляем список на месте
    binary_list[:count_zeros] = [0] * count_zeros
    binary_list[count_zeros:] = [1] * count_ones


binary_list = [0, 1, 1, 0, 1]
sort_binary_list(binary_list)
print(binary_list)


binary_list = [0, 0, 0, 0, 0]
sort_binary_list(binary_list)
print(binary_list)

binary_list = [1, 1, 1, 1, 1]
sort_binary_list(binary_list)
print(binary_list)

binary_list = [1]
sort_binary_list(binary_list)
print(binary_list)

binary_list = [0, 1]
sort_binary_list(binary_list)
print(binary_list)

binary_list = [0, 1, 0, 1]
sort_binary_list(binary_list)
print(binary_list)