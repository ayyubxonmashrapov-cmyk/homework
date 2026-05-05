def count_passing_students(grades: list[int], passingGrade: int) -> int:
    count = 0
    for grade in grades:
        if grade >= passingGrade:
            count += 1

    return count            

grades = [45, 60, 75, 30, 90]
passingGrade = 60
print(count_passing_students(grades, passingGrade))
# Output: 3

grades = [45, 60, 75, 30, 90]
passingGrade = 60  
print(count_passing_students(grades, passingGrade))
# Output: 3

grades = [10, 20, 30, 40, 50]
passingGrade = 51  
print(count_passing_students(grades, passingGrade))
# Output: 0

grades = [100, 90, 80, 70, 60]
passingGrade = 70  
print(count_passing_students(grades, passingGrade))
# Output: 4

grades = [60, 60, 60, 60]
passingGrade = 60  
print(count_passing_students(grades, passingGrade))
# Output: 4

grades = []
passingGrade = 50  
print(count_passing_students(grades, passingGrade))
# Output: 0

grades = [49, 50, 51]
passingGrade = 50  
print(count_passing_students(grades, passingGrade))
# Output: 2
