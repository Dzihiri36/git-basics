def move_zeros(nums):
    pos = 0  # позиция, куда будем ставить ненули

    for i in range(len(nums)): #  выносим все ненули в начало
        if nums[i] != 0: # если элемент списка равен target, то возвращаем True
            nums[pos] = nums[i] # перемещаем элемент в нужное место
            pos += 1 # увеличиваем индекс двойкой

    for i in range(pos, len(nums)): # добиваем хвост нулями
        nums[i] = 0 # перемещаем элемент в нужное место


nums = [0, 1, 2]
move_zeros(nums)
print(nums)

nums = [0, 2, 1]
move_zeros(nums)
print(nums)

nums = [1, 2, 3]
move_zeros(nums)
print(nums)

