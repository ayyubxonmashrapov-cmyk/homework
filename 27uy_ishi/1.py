def majority_element(nums: list) -> int:
    return -1 if not nums else max(set(nums), key=lambda x: nums.count(x))


nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))
# Output: 2

print(majority_element([3, 3, 4]))
# Output: 3

print(majority_element([1, 1, 2, 2, 2, 3]))
# Output: 2

print(majority_element([5, 5, 5, 1, 2]))
# Output: 5

print(majority_element([7]))
# Output: 7

print(majority_element([]))
# Output: -1
