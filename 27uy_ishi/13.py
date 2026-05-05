def move_numbers(nums: list) -> list:
    zeros = []
    positives = []
    negatives = []
    for i in nums:
        if i == 0:
            zeros.append(0)
        elif i > 0:
            positives.append(i)
        else:
            negatives.append(i)

    zeros.extend(positives)
    zeros.extend(negatives)
    return zeros

nums = [0, -1, 2, -3, 4, -5]
print(move_numbers(nums))
# Output: [0, 2, 4, -1, -3, -5]

print(move_numbers([0, -1, 4, -3, 2, -5]))
print(move_numbers([2, 3, 1, 4, 5]))
print(move_numbers([-1, -2, -3]))
print(move_numbers([8, -8, 0, 5, -2, 6, -3, 7]))
print(move_numbers([0, -8, -2, 3, 9, -3, 5]))
print(move_numbers([9, 8, -7, -6, 5, 4, 0]))
print(move_numbers([0, 0, -1, 0, 1]))
print(move_numbers([0]))
print(move_numbers([-1]))
print(move_numbers([]))


# [0, 4, 2, -1, -3, -5]
# [2, 3, 1, 4, 5]
# [-1, -2, -3]
# [0, 8, 5, 6, 7, -8, -2, -3]
# [0, 3, 9, 5, -8, -2, -3]
# [0, 9, 8, 5, 4, -7, -6]
# [0, 0, 0, 1, -1]
# []
# [0]
# [-1]











