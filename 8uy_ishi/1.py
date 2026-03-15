# Palindrome Number

son = input("son: ")
print(son == son[::-1])


# FizzBuzz

son = int(input("son: "))
for i in range(1, son):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)        



# Reverse Integer

son = input()
son = int(son[::-1])
print(son)



# Add Digits

son = int(input())
n = 9.9
while n > 9:
    if n != 9.9:
        son = n
    n = 0
    while son:
        n += son % 10
        son //= 10
print(n)



# Happy Number

son = int(input())
while son != 1:
    n = 0   

    while son:
        n += (son % 10) * (son % 10)
        son //= 10 

    if son == 4:
        print("Unpappy Numaber")
        break

    son = n 

else:
    print("Happy Number")


# Count and Say

nechta = int(input())
son = 1
newS = 0
print(son)

for j in range(nechta-1):
    if j:
        son = newS
    newS = 0

    son = int(str(son)[::-1])

    while son:
        n = son % 10
        temp = n
        i = 0
        while son:
            n = son % 10
            if n != temp:
                break
            son = son // 10
            i += 1

    
        nextS = i * 10 + temp
        i = len(str(nextS))
        newS = newS * 10**i + int(nextS)


    print(newS)


# Climbing Stairs 

n = int(input())

a, b = 1, 1

for i in range(n-1):
    a, b = b, a + b

print(b)




