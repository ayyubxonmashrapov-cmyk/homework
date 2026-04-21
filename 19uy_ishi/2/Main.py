from Teacher import Teacher
from Student import Student
from Group import Group

teacher = Teacher("Abdurahmonov", "Python")
group = Group("Bootcamp Foundation", teacher)

student1 = Student("Ali", 1)
student1.add_grade(5)
student1.add_grade(4)

group.add_student_togroup(student1)

group.show_group_students()