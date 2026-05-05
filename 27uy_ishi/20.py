def find_top_three_numbers_sorted(data: list) -> list:
    result = []
    for i in data:
        i = list(i)
        i.sort(reverse=True)
        result.append(tuple(i[:3]))
    
    return result

data = [(10, 20, 30, 11), (5, 15), (40,), (7, 8, 50, 3)]
print(find_top_three_numbers_sorted(data))
# Output: [(30, 20, 11), (15, 5), (40,), (50, 8, 7)]


data = [ ]
print(find_top_three_numbers_sorted(data))
# Output: [ ]

data = [(5,), (12, 3), (0, -1)]
print(find_top_three_numbers_sorted(data))
# Output: [(5,), (12, 3), (0, -1)]
 
data = [(4, 4, 4, 4), (2, 2, 2), (10, 10, 10, 10)]
print(find_top_three_numbers_sorted(data))
# Output: [(4, 4, 4), (2, 2, 2), (10, 10, 10)]

data = [(-10, -5, -20, -1), (-3, -2, -1), (-50, -100)]
print(find_top_three_numbers_sorted(data))
# Output: [(-1, -5, -10), (-1, -2, -3), (-50, -100)]