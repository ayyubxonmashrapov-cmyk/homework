class Pharmacy():
    def __init__(self,pharmacy_name: str, pharmacy_address: str):
        self.medicines = []
        self.cash_balance = 0.0
        self.pharmacy_address = pharmacy_address
        self.pharmacy_name = pharmacy_name
        
    def get_medicines_info(self):
        for medicine in self.medicines:
            print(medicine["medicine"], medicine["price"], medicine["quantity"])

    def add_medicine(self, medicine: str, price: float, quantity: int):
        if price > 0 and quantity > 0:
            self.medicines.append({
                "medicine" : medicine,
                "price" : price,
                "quantity" : quantity 
            })

    def remove_medicine(self, medicine: str):
        for i in range(len(self.medicines)):
            if self.medicines[i]["medicine"] == medicine:
                self.medicines.pop(i)

    def add_money(self, amount: float):
        if amount > 0:
            self.cash_balance += amount

    def sell_medicine(self, medicine: str, quantity: int) ->None:
        for i in range(len(self.medicines)):
            if self.medicines[i]["medicine"] == medicine:
                if self.medicines[i]["quantity"] >= quantity:
                    self.medicines[i]["quantity"] -= quantity
                    self.cash_balance += quantity * self.medicines[i]["price"]

                    if self.medicines[i]["quantity"] == 0:
                        self.medicines.pop(i)
                    return True
                return False       
                
    def update_medicine_price(self, medicine: str, new_price: float):
        for i in self.medicines:
            if i["medicine"] == medicine:
                i["price"] = new_price
                return

    def check_medicine_stock(self, medicine: str):
        for i in self.medicines:
            if i["medicine"] == medicine:
                return i["quantity"] 
            
    def total_medicines_value(self) -> float:
        total = 0.0
        for i in self.medicines:
            total += i["price"]
        return total


ph = Pharmacy("Apteka 1", "Tashkent")

ph.add_medicine("Paracetamol", 5000, 10)
ph.add_medicine("Ibuprofen", 8000, 5)

print("=== Все лекарства ===")
ph.get_medicines_info()

print("\nParacetamol stock:", ph.check_medicine_stock("Paracetamol"))

print("\nПродажа 3 Paracetamol:")
result = ph.sell_medicine("Paracetamol", 3)
print("Успешно?", result)

print("\n=== После продажи ===")
ph.get_medicines_info()

print("\nБаланс:", ph.cash_balance)

ph.update_medicine_price("Ibuprofen", 9000)

print("\n=== После изменения цены ===")
ph.get_medicines_info()

print("\nОбщая стоимость:", ph.total_medicines_value())

ph.remove_medicine("Ibuprofen")

print("\n=== После удаления ===")
ph.get_medicines_info()