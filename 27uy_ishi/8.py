def sort_products_by_name(products: list) -> list:
    products.sort(key=lambda x: x[1])
    return products

products = [("ID123", "Olma", 10), ("ID101", "Banan", 5), ("ID150", "Anor", 8)]
print(sort_products_by_name(products))
# Output: [('ID150', 'Anor', 8), ('ID101', 'Banan', 5), ('ID123', 'Olma', 10)]

products = [("ID123", "Olma", 10), ("ID101", "Banan", 5), ("ID150", "Anor", 8)]
print(sort_products_by_name(products))
# Output: [('ID150', 'Anor', 8), ('ID101', 'Banan', 5), ('ID123', 'Olma', 10)]

products = [("ID300", "Uzum", 20), ("ID100", "Olma", 15)]
print(sort_products_by_name(products))
# Output: [('ID100', 'Olma', 15), ('ID300', 'Uzum', 20)]

products = []
print(sort_products_by_name(products))
# Output: []

products = [("ID200", "Shaftoli", 12)]
print(sort_products_by_name(products))
# Output: [('ID200', 'Shaftoli', 12)]

products = [("ID400", "Olma", 8), ("ID401", "Olma", 9)]
print(sort_products_by_name(products))
# Output: [('ID400', 'Olma', 8), ('ID401', 'Olma', 9)]
