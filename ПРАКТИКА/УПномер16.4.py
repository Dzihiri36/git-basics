from collections import Counter

def count_beautiful_pairs(nums):
    freq = Counter(nums)
    return sum(count // 2 for count in freq.values())


print(count_beautiful_pairs([1, 4, 5, 4, 1, 1, 0]))
print(count_beautiful_pairs([4, 4, 4, 4, 4, 4, 4]))
print(count_beautiful_pairs([1, 2, 3, 4, 5, 6, 7]))
print(count_beautiful_pairs([0, 0])) 
print(count_beautiful_pairs([1, 1, 1]))    
print(count_beautiful_pairs([0, 9, 9, 0]))  