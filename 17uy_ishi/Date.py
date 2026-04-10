class Date:
    def __init__(self, day: int, month: int, year:int):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self)->int:
        return self.day
    
    def get_month(self)->int:
        return self.month
    
    def get_year(self)->int:
        return self.year
    
    def set_day(self, new_day:int ):
        self.day = new_day

    def set_month(self, new_month: int):
        self.month = new_month

    def set_year(self, new_year: int):
        self.year = new_year

    def get_info(self)->str:
        return f"{self.day}/{self.month}/{self.year}"            

d = Date(7, 3, 2025)
print(d.get_info())  # 07/03/2025

d.set_day(1)
d.set_month(12)
d.set_year(2022)
print(d.get_info())  # 01/12/2022