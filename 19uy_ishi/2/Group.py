from Teacher import Teacher
from Student import Student
import json

class Group:
    def __init__(self, science: str, teacher: Teacher):
        self.science = science
        self.teacher = teacher

    def __load(self):
        try:
            with open("data.json", "r") as f:
                return json.load(f)
        except:
            return []
    
    def __save(self, student: Student):                                          #adashmasam har guruhga alohida json ochiladi (minus)
        data = self.__load()
        data.append({
            "name": student.name,
            "year": student.year,
            "grades": student.grades
        })

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    def __str__(self):
        data = self.__load()
        students = [student["name"] for student in data]                        
        return f"Guruh: {self.science}, O‘qituvchi: {self.teacher.name}\nGuruh talabalar: {students}"

    def add_student_togroup(self, student: Student):
        if isinstance(student, Student):
            self.__save(student)
            return True
        return False

    def show_group_students(self)-> list:
        data = self.__load()
        for student in data:
            print(student)

    def __len__(self):
        data = self.__load()
        return len(data)



