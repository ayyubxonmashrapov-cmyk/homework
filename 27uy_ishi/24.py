def calculate_class_averages(scores: dict) -> dict: 
    dct = {}
    for i in scores:
        if scores[i]:
            n = sum(scores[i]) / len(scores[i]) 
            if n%1 > 0.50:
                n += (1 - n%1)
            else:
                n -= n%1

            dct[i] = int(n)
        else:
            dct[i] = 0
    return dct

scores = {"Class B": [96, 76, 98], "Class C": [60, 90]}
print(calculate_class_averages(scores))
# Output: {'Class B': 90, 'Class C': 75}


scores = { "Class A": [70, 80, 90], "Class B": [50, 60] }
print(calculate_class_averages(scores))
	# Output: {'Class A': 80, 'Class B': 55}

scores = { "Class A": [85, 90, 95], "Class B": [60, 70], "Class C": [50], "Class D": [100, 80, 60, 40] }
print(calculate_class_averages(scores))
	# Output: {'Class A': 90, 'Class B': 65, 'Class C': 50, 'Class D': 70}
	
scores = { "Class A": [90, 80], "Class B": [], "Class C": [70], "Class D": [100, 95, 90, 85], "Class E": [] }
print(calculate_class_averages(scores))
	# Output: {'Class A': 85, 'Class B': 0, 'Class C': 70, 'Class D': 92, 'Class E': 0}

scores = { "Class A": [90.5, 0, 70.8], "Class B": [100, 50.6, 75.2], "Class C": [45, 67.5], "Class D": [89.9, 90.1, 91.0] }
print(calculate_class_averages(scores))
	# Output: {'Class A': 54, 'Class B': 75, 'Class C': 56, 'Class D': 90}