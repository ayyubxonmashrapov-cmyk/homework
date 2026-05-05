def update_student_score(students: dict, student_name: str, score: int) -> dict:
    if student_name in students:
        students[student_name].append(score)
    else:
        students[student_name] = [score]

    return students

students = {"Ali": [80, 85], "Vali": [90]}
print(update_student_score(students, "Ali", 95))
# Output: {"Ali": [80, 85, 95], "Vali": [90]}

students = {"Ali": [80, 85]}
student_name = "Ali"
score = 90
print(update_student_score(students, student_name, score))
# {"Ali": [80, 85, 90]}

students = {"Vali": [88]}
student_name = "Hasan"
score = 92
print(update_student_score(students, student_name, score))
# {"Vali": [88], "Hasan": [92]}

students = {}
student_name = "Sardor"
score = 75
print(update_student_score(students, student_name, score))
# {"Sardor": [75]}

students = {"Dilshod": [100]}
student_name = "Dilshod"
score = 99
print(update_student_score(students, student_name, score))
# {"Dilshod": [100, 99]}

students = {"Laylo": [85]}
student_name = "Laylo"
score = 90
print(update_student_score(students, student_name, score))
# {"Laylo": [85, 90]}

students = {"Aziz": [60], "Laylo": [85]}
student_name = "Aziz"
score = 70
print(update_student_score(students, student_name, score))
# {"Aziz": [60, 70], "Laylo": [85]}

