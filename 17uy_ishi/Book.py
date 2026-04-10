class Book:
    def __init__(self, id: int, title: str, author: str, price: int, quantity: int):
        self.quantity = quantity
        self.price = price
        self.author = author
        self.title = title
        self.id = id

    def getID(self) -> int:
        return self.id
    
    def getTitle(self) -> str:
        return self.title
    
    def getAuthor(self) -> str:
        return self.author
    
    def getPrice(self) -> int:
        return self.price
    
    def setPrice(self, new_price: int):
        self.price = new_price

    def toString(self)-> str:
        return f"Book [id={self.id}, title={self.title}, author={self.author} price={self.price}, quantity={self.quantity}]"
    
b = Book(42, "afgvg", "sfa", 2424, 4)    
print(b.toString())