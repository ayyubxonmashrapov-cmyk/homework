def calculate_painting_time(pattern: list) -> int: 
    seconds = 0
    for i in range(len(pattern)-1):
        if pattern[i] != pattern[i+1]:
            seconds +=1
    seconds += len(pattern) * 2
    return seconds


pattern = ["Red", "Blue", "Red", "Blue", "Red"]
print(calculate_painting_time(pattern)) 
# Output: 14

pattern = ["Green", "Green", "Green", "Green"]
print(calculate_painting_time(pattern)) 
Output: 8

pattern = ["Red", "Green", "Blue", "Yellow"]
print(calculate_painting_time(pattern)) 
Output: 11

pattern = []
print(calculate_painting_time(pattern)) 
Output: 0

pattern = ["Green"]
print(calculate_painting_time(pattern)) 
Output: 2