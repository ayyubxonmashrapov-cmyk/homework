class Pesrson:
    def __init__(self, name: str, secondname: str, year: int):
        self.name = name
        self.secondname = secondname
        self.year = year

    def get_name(self) -> str:
        return self.name.title() + " " + self.secondname.title()
    
    def get_age(self) -> int:
        return 2026 - self.year
    
p1 = Pesrson("ali", "valiyev", 1995)
p2 = Pesrson("dilnoza", "xudoyberdiyeva", 2000)

print(f"Yosh: {p1.get_age()}")
print(f"Yosh: {p2.get_age()}")

print(f"To'liq ism: {p1.get_name()}")
print(f"To'liq ism: {p2.get_name()}")