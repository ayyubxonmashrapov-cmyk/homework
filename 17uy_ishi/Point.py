class Point:
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y

    def get_quarter(self)-> int | None:
        if self.x == 0 or self.y == 0:
            return None
        elif self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        else:
            return 4
        
p1 = Point(0,0)
print(p1.get_quarter())
