def add_product(products: dict, product_name: str, quantity: int) -> dict:
	if product_name in products:
		products[product_name] += quantity
	else:
		products[product_name] = quantity
	return products	
    

products = {"olma": 5, "banan": 3} 
print(add_product(products, "olma", 2))
# Output: {"olma": 7, "banan": 3}

products = {"non": 10}
product_name = "sut"
quantity = 5
print(add_product(products, product_name, quantity))
# Output: {"non": 10, "sut": 5}

products = {}
product_name = "shakar"
quantity = 4
print(add_product(products, product_name, quantity))
# Output: {"shakar": 4}

products = {"go‘sht": 6, "piyoz": 2}
product_name = "piyoz"
quantity = 3
print(add_product(products, product_name, quantity))
# Output: {"go‘sht": 6, "piyoz": 5}

products = {"tuz": 1}
product_name = "tuz"
quantity = 1
print(add_product(products, product_name, quantity))
# Output: {"tuz": 2}