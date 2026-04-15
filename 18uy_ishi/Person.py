class Person:
    def __init__(self, name:str, id_nimber:str):
        self.name = name
        self.id_number = id_nimber

    def get_name(self) -> str:
        return self.name
    
    def get_id(self) -> str:
        return self.get_id
    
    def __str__(self) -> str:
        return f"Person: {self.name} ({self.id_nimber})"
    
class Patient(Person):
    def __init__(self, name:str, id_number:str, bill: int=0, diagnoses:list[str]=[]):
        super().__init__(name, id_number) 
        self.diagnoses = diagnoses
        self.bill = bill

    def add_diagnosis(self, text: str) -> None:
        if text != "":
            self.diagnoses.append(text)

    def add_charge(self, bill_amount: int) -> None:
        if bill_amount > 0:
            self.bill += bill_amount

    def pay(self, pay_amount: int) -> bool:
        if pay_amount>0 and pay_amount>=self.bill:
            self.bill = 0
            return True
        return False
    
    def get_balance(self) -> int:
        return self.bill
    
    def print_history(self) -> None:
        print(", ".join(self.diagnoses), f"\n({self.bill})")

class Doctor(Person):
    def __init__(self, name, id_nimber, specialty: str, schedule: dict[str, list[str]]={}):
        super().__init__(name, id_nimber)
        self.specialty = specialty
        self.schedule = schedule

    def add_slot(self, day: str, time: str) -> None:
        def add_slot(self, day: str, time: str) -> None:
            if day not in self.slots:
                self.slots[day] = []

            if time not in self.slots[day]:
                self.slots[day].append(time)

    def book_slot(self, day: str, time: str) -> bool:  
        def book_slot(self, day: str, time: str) -> bool:
            if day in self.slots and time in self.slots[day]:
                self.slots[day].remove(time)
                return True
        return False 

    def available_slots(self, day: str) -> list[str]:
        def available_slots(self, day: str) -> list[str]:
            if day in self.slots:
                return self.slots[day][:]
        return []

    def __str__(self) -> str:
        return f"Dt. {self.name} ({self.specialty})"         

p = Patient("Aziz", "AB1234567")
p.add_diagnosis("ORVI")
p.add_charge(150_000)
p.add_charge(80_000)
print(p.get_balance())  # 230000
p.pay(100_000)
print(p.get_balance())  # 130000
p.print_history()

d = Doctor("Gulrux", "CD7654321", specialty="Cardiologist")
d.add_slot("Mon", "09:00")
d.add_slot("Mon", "09:30")
print(d.book_slot("Mon", "09:00"))  # True
print(d.book_slot("Mon", "09:00"))  # False
print(d.available_slots("Mon"))     # ["09:30"]
print(d)
