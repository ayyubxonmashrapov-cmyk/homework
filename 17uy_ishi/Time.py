class Time:
    def __init__(self, minuts: int , seconds: int):
        self.minuts = minuts
        self.seconds = seconds

    def get_minutes(self) -> int:
        return self.minuts + self.seconds//60
    def get_seconds(self) -> int:
        return self.seconds + self.minuts * 60
    
time = Time(5, 130) 
print(time.get_minutes()) 
print(time.get_seconds())