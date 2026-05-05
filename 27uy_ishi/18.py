def move_zeroes(nums: list) -> list:
    zeros = []
    while 0 in nums:
        nums.remove(0)
        zeros.append(0)
    
    nums.extend(zeros)
    return nums

nums = [0, 1, 0, 3, 12]
print(move_zeroes(nums))
# Output: [1, 3, 12, 0, 0]



nums = [0, 1, 0, 3, 12]
print(move_zeroes(nums))
# Output: [1, 3, 12, 0, 0]

nums = [1, 2, 3, 4, 5]
print(move_zeroes(nums))
# Output: [1, 2, 3, 4, 5]

nums = [0, 0, 0, 0, 0]
print(move_zeroes(nums))
# Output: [0, 0, 0, 0, 0]

nums = [4, 0, 5, 0, 6, 0, 7]
print(move_zeroes(nums))
# Output: [4, 5, 6, 7, 0, 0, 0]

nums = [0, 1, 2, 0, 3, 4, 0, 5]
print(move_zeroes(nums))
# Output: [1, 2, 3, 4, 5, 0, 0, 0]

nums = [9, 8, 0, 0, 7, 6, 0, 5, 4]
print(move_zeroes(nums))
# Output: [9, 8, 7, 6, 5, 4, 0, 0, 0]

nums = [0, 0, 1]
# Output: [1, 0, 0]

nums = [1, 0, 2, 0, 3, 0, 4, 0]
print(move_zeroes(nums))
# Output: [1, 2, 3, 4, 0, 0, 0, 0]

nums = []
print(move_zeroes(nums))
# Output: []

nums = [0]
print(move_zeroes(nums))
# Output: [0]