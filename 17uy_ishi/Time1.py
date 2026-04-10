class Time:
    def __init__(self, hour:int, minuts: int , seconds: int):
        self.minuts = minuts
        self.seconds = seconds
        self.hour = hour

    def get_hour(self) -> int:
        return self.hour
    def get_minutes(self) -> int:
        return self.minuts
    def get_seconds(self) -> int:
        return self.seconds
    def set_hour(self, new_hour: int):
        self.hour = new_hour
    def set_minutes(self, new_minute:int):
        self.minuts = new_minute
    def set_seconds(self, new_second: int):
        self.seconds = new_second

    def set_time(self, new_hour:int, new_minuts: int , new_seconds: int):
        self.minuts = new_minuts
        self.seconds = new_seconds
        self.hour = new_hour

    def __str__(self):
        return "%02d:%02d:%02d" % (self.hour, self.minuts, self.seconds)
    
    def next_second(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minuts += 1
        if self.minuts == 60:
            self.minuts = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0

    def before_second(self):
        self.seconds -= 1
        if self.seconds == -1:
            self.seconds = 59
            self.minuts -=1
        if self.minuts == -1:
            self.minuts = 59
            self.hour -= 1
        if self.hour == -1:
            self.hour = 23                       
    
t = Time(23, 59, 59)
print(t)  # 23:59:59

t.next_second()
print(t)  # 00:00:00

# 1 soniyaga kamaytirish
t.before_second()
print(t)  # 23:59:59

# Elementlarni o‘zgartirish va olish
t.set_time(12, 5, 9)
print(t.get_hour())   # 12
print(t.get_minutes()) # 5
print(t.get_seconds()) # 9
print(t)             # 12:05:09

    