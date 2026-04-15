class User:
    def __init__(self, name:str, email:str, addres:str):
        self.name = name 
        self.email = email
        self.addres = addres

    def get_name(self)->str:
        return self.name
    
    def get_email(self)->str:
        return self.email
    
    def get_addres(self)->str:
        return self.addres
    
    def set_address(self, new_address: str) -> None:
        self.addres = new_address

    def __str__(self) -> str:
        return f"User {self.name} <{self.email}>"
    


class Customer(User):
    def __init__(self, name:str, email:str, addres:str, balance:int, cart:list[tuple[str,int,int]]=[]):
        super().__init__(name, email, addres)
        self.cart = cart
        self.balance = balance

    def add_to_cart(self, product:str, qty:int, price:int) -> None:
        if qty > 0 and price > 0:
            self.cart.append((product, qty, price))
    
    def clear_cart(self) -> None:
        self.cart.clear()

    def get_cart_total(self)-> int:
        return sum([qty * price for name, qty, price in self.cart])
    
    def checkout(self) -> bool:
        if self.get_cart_total() > self.balance:
            return False
        self.balance -= self.get_cart_total()
        return  True
    
    def __str__(self) -> str:
        return f"Customer: {self.name} (balance: {self.balance} so'm)"
    
class Seller(User):
    def __init__(self, name:str, email:str, addres:str, rating:float, produsts:dict[str,int]={}):
        super().__init__(name, email, addres)
        self.produsts = produsts
        self.rating = rating

    def add_product(self, name, qty) -> None:
        if name in self.produsts.keys():
            self.produsts[name] += qty
        else:
            self.produsts[name] = qty

    def remove_product(self, name) -> bool:
        if name in self.add_product:
            self.produsts.pop(name)
            return True
        return False

    def update_stock(self, name, delta_qty) -> bool:
        if name in self.produsts and self.produsts[name] - delta_qty > -1:
            self.produsts[name] += delta_qty
            return True
        return False
    
    def get_stock(self) -> dict[str,int]:
        return self.produsts
    
    def __str__(self) -> str:
        return f"Seller {self.name} (rating: {self.rating}, items: {sum(self.produsts.values())})"
            

            


c = Customer("Ali", "ali@mail.com", "Toshkent", balance=2_000_000)
c.add_to_cart("Keyboard", 1, 300_000)
c.add_to_cart("Mouse", 2, 150_000)
print(c.get_cart_total())     # 600000
print(c.checkout())           # True
print(c)                      # Customer: Ali (balance: 1400000 so‘m)

s = Seller("Gulbahor", "g@mail.com", "Samarqand", rating=4.8)
s.add_product("Keyboard", 10)
s.update_stock("Keyboard", -3)
print(s.get_stock())          # {'Keyboard': 7}
print(s)                      # Seller: Gulbahor (rating: 4.8, items: 7)
