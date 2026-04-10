class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    def get_a(self) -> float:
        return self.a

    def set_a(self, new_a: float)-> None:  
        self.a = new_a

    def get_b(self) -> float:
        return self.b
    
    def set_b(self, new_b: float)->None:
        self.b = new_b

    def get_area(self)->float:
        return self.a * self.b
    
    def get_perimetr(self)->float:
        return 2*(self.a + self.b)
    
    def get_info(self)->str:
        return f"{self.a}, {self.b}, {self.get_area()}, {self.get_perimetr()}"
    

r = Rectangle(3, 4)

print("a:", r.get_a())          # 3
print("b:", r.get_b())          # 4

print("area:", r.get_area())    # 12
print("perimeter:", r.get_perimetr())  # 14

r.set_a(5)
r.set_b(6)

print("new a:", r.get_a())      # 5
print("new b:", r.get_b())      # 6

print("new area:", r.get_area())        # 30
print("new perimeter:", r.get_perimetr())  # 22

print("info:", r.get_info())
    

