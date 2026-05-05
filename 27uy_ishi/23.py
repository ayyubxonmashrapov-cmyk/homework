def apply_discount_and_sort(prices: list) -> list:
    result = [i*0.85 for i in prices if i > 0]
    result.sort(reverse=True)
    return result
    
prices = [100, 250, 75, 150, 300]
print(apply_discount_and_sort(prices))
# Output: [255.0, 212.5, 127.5, 85.0, 63.75]

prices = []
print(apply_discount_and_sort(prices))
# Output: []

prices = [150.5, 200, 99.9, 50.25]
print(apply_discount_and_sort(prices))
# Output: [170.0, 127.925, 84.915, 42.7125]

prices = [0, 300, -200, 150, 50]
print(apply_discount_and_sort(prices))
# Output: [255.0, 127.5, 42.5]


