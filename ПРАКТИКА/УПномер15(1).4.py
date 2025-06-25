def section_sort(nums):
    i = 0
    while i < len(nums):
        start = i
        while i < len(nums) and nums[i] != 0:
            i += 1
        end = i  # nums[start:end] — текущий блок без нуля
        nums[start:end] = sorted(nums[start:end])
        i += 1  # пропускаем 0


nums = [2, 1, 0, 3, 2, 1, 0]
section_sort(nums)
print(nums)

nums = [1, 1, 1, 0, 5, 3, 4, 0, 2, 5, 3, 0, 3, 2, 1, 0]
section_sort(nums)
print(nums)

nums = [1, 1, 1, 0, 2, 2, 2, 0]
section_sort(nums)
print(nums)

nums = [3, 2, 1, 0]
section_sort(nums)
print(nums)

nums = [1, 0]
section_sort(nums)
print(nums)

nums = [5, 4, 3, 0, 2, 1, 0]
section_sort(nums)
print(nums)