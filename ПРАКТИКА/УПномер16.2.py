from collections import Counter

def count_triplet_numbers(nums):
    """
    Считает количество чисел, встречающихся ровно 3 раза.
    """
    counter = Counter(nums)
    return sum(1 for count in counter.values() if count == 3)


print(count_triplet_numbers([4, 5, 6, 4, 5, 4, 5, 6]))
print(count_triplet_numbers([5, 4, 5, 5, 4, 5, 7, 4]))
print(count_triplet_numbers([4, 5, 4, 6, 5, 7, 5, 5]))
print(count_triplet_numbers([5]))
print(count_triplet_numbers([1, 1, 1, 1]))
print(count_triplet_numbers([7, 7, 7]))