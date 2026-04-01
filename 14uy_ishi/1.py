import random
import math
from datetime import datetime, timedelta


lst = [1,2,3,4,5,6]                                                              #1
print(random.sample(lst, 3))

n = 30                                                                           #2
print(math.sin(math.radians(n)))

now = datetime.now()                                                             #3
print(now.strftime("%Y-%m-%d %H:%M:%S"))

froM = 1                                                                         #4
to = 100
while True:
    n = random.randint(froM, to)
    print(n)
    b = int(input("1.meniki katta\n2.meniki kichik\n3.topdi\n : "))
    if b == 1:
        froM = n
    elif b == 2:
        to = n
    elif b == 3:
        break
    else:
        while 0 < b or b > 3:
            b = input("1.meniki katta\n2.meniki kichik\n3.topdi\n : ")


print(math.exp(1))                                                               #5

import cntr
print(cntr.usd_to_uzs(10))                                                       #6

import shapes                                                                    #7
print(shapes.circle_area(4))
print(shapes.rectangle_area(4,5))

