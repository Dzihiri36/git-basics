def find_triple(nums):
    nums.sort()
    s = nums[3]  # a + b + c
    x, y, z = nums[0], nums[1], nums[2]  # суммы по парам

    a = s - z
    b = s - y
    c = s - x

    return sorted([a, b, c])


print(find_triple([8, 5, 7, 4]))
print(find_triple([2, 2, 3, 2]))
print(find_triple([5, 3, 6, 4]))
print(find_triple([600000000, 600000000, 600000000, 900000000]))
print(find_triple([3, 5, 3, 4]))