class Student:
    def __init__(self, name: str, year: int):
        self.name = name 
        self.year = year
        self.grades = []

    def add_grade(self, grade: int):
        if 0 <= grade <= 5:
            self.grades.append(grade)

    def average_grade(self) -> int:
        return sum(self.grades)/len(self.grades)

    def __str__(self):
        return f"Talaba: {self.name}, Kurs: {self.year}, O‘rtacha baho: {self.average_grade()}"

    def __len__(self):
        return len(self.grades)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return None

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()
        return None
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return None
    
    