def can_nest(nums1, nums2):
    if (min(nums1) > min(nums2) or min(nums1) < min(nums2)) and (max(nums1) > max(nums2) or max(nums1) < max(nums2)): 
        # если минимальный или максимальный элемент в первом списке больше или меньше второго, то можно соединить их
        return True # возвращаем True
    return False # возвращаем False


print(can_nest([1, 2, 3, 4], [0, 6]))
print(can_nest([4, 0], [3, 1]))
print(can_nest([1, 2, 3, 4], [2, 3]))










