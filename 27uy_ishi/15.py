def assign_employee_ids(employee_ids: list, prefix: str) -> list:
    for i in range(len(employee_ids)):
        employee_ids[i] = prefix + str(employee_ids[i])

    return employee_ids

employee_ids = [101, 102, 103, 104]
prefix = "EMP"
print(assign_employee_ids(employee_ids, prefix))
# Output: ['EMP101', 'EMP102', 'EMP103', 'EMP104']

employee_ids = [1, 2, 3, 4]
prefix = "EMP"
print(assign_employee_ids(employee_ids, prefix))
employee_ids = [101, 102]
prefix = "ID"
print(assign_employee_ids(employee_ids, prefix))
employee_ids = []
prefix = "EMP"
print(assign_employee_ids(employee_ids, prefix))
employee_ids = [9, 10, 11]
prefix = "STAFF"
print(assign_employee_ids(employee_ids, prefix))
employee_ids = [1001]
prefix = "USR"
print(assign_employee_ids(employee_ids, prefix))

# ['EMP1', 'EMP2', 'EMP3', 'EMP4']
# ['ID101', 'ID102']
# []
# ['STAFF9', 'STAFF10', 'STAFF11']
# ['USR1001']

