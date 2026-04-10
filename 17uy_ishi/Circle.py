from math import pi

class Circle:
    def __init__(self, radius: float, color: str):
        self.radius = radius
        self.color = color

    def get_radius(self)->None:
        return self.radius
    
    def set_radius(self, newradius: float)->None:
        self.radius = newradius

    def get_color(self)->None:
        return self.color
    
    def set_color(self, newcolor: str)->None:
        self.color = newcolor

    def get_area(self)->float:
        return 3.14 * self.radius**2
    
    def get_circumference(self)->float:
        return 2 * 3.14 * self.radius
    
    def get_info(self)->str:
        return f"{self.radius}, {self.color}, {self.get_area()}, {self.get_circumference()}"
    


c = Circle(5,"qizil")

print("Radius:", c.get_radius())      
print("Rang:", c.get_color())         

print("Yuza:", c.get_area())          
print("Aylana uzunligi:", c.get_circumference())  

c.set_radius(10)
c.set_color("ko‘k")

print("Yangi radius:", c.get_radius())       
print("Yangi rang:", c.get_color())          
print("Yangi yuza:", c.get_area())      
print("Yangi aylana uzunligi:", c.get_circumference())  


print(c.get_info())