def remove_duplicates(nums: list) -> list:
    result = []
    for num in nums:
        if num not in result:
            result.append(num)

    return result 

# Test
nums = [5, 2, 2, 3, 1, 4, 3, 5]
print(remove_duplicates(nums))
# Output: [5, 2, 3, 1, 4]

print(remove_duplicates([1, 2, 2, 3, 1, 4, 3, 5]))
# Output: [1, 2, 3, 4, 5]

print(remove_duplicates([7, 7, 7, 7, 7]))
# Output: [7]

print(remove_duplicates([1, 2, 3, 4, 5]))
# Output: [1, 2, 3, 4, 5]

print(remove_duplicates([]))
# Output: []

print(remove_duplicates([9, 8, 7, 9, 8, 6, 5, 4, 4, 3]))
# Output: [9, 8, 7, 6, 5, 4, 3]
