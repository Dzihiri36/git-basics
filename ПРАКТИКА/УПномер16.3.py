from collections import Counter

def least_frequent_number(nums):
    freq = Counter(nums)
    min_freq = min(freq.values())
    return min(num for num, count in freq.items() if count == min_freq)


print(least_frequent_number([4, 2, 4, 1, 3, 2, 1]))
print(least_frequent_number([3, 2, 1, 1, 3, 2, 1]))
print(least_frequent_number([1]))
print(least_frequent_number([1, 1, 1, 1, 1]))
print(least_frequent_number([1, 10, 100, 1000]))
print(least_frequent_number([1, 1, 10]))