class Car:
    def __init__(self, speed: int, time: int):
        self.speed = speed
        self.time = time

    def get_info(self) -> int:
        return self.speed * self.time
    
matiz = Car(80, 3)
print(matiz.get_info())