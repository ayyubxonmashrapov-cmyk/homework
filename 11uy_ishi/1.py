lst = {"Ali": 85, "Vali": 90, "Hasan": 78, "Husan": 88}

search_name = "Vali"

print(lst[f"{search_name}"])

#                                                   misol-1
##############################################################

products = {"olma": 15000, "banan": 18000, "uzum": 22000}
search_product = "banan"
print(products[f"{search_product}"])

#                                                   misol-2
##############################################################

contacts = {"Ali": "+998901234567", "Vali": "+998911112233"}
search_name = "Ali"

print(f"{search_name} telfon raqami: {contacts[f"{search_name}"]}")

#                                                   misol-3
##############################################################

cars = {"Malibu": 2020, "Captiva": 2018, "Nexia": 2015}
search_car = "Captiva"
print(f"{search_car} {cars[search_car]}-yilda ishlab chiqazilgan")

#                                                   misol-4
##############################################################

currency_rates = {"USD": 11650, "EUR": 12500, "RUB": 150}
search_currency = "USD"
print(f"1 {search_currency} = {currency_rates[search_currency]} so'm")

#                                                   misol-5
##############################################################

employees = {"Anvar": "Dasturchi", "Madina": "HR", "Rustam": "Menejer"}
search_employee = "Madina"
print(f"{search_employee} lavozimi - {employees[search_employee]}")

#                                                   misol-6
##############################################################

books = {"Harry Potter": "J.K. Rowling", "1984": "George Orwell", "Dunyo ishlari": "O'tkir Hoshimov"}
search_book = "1984"
print(f"{search_book} muallifi: {books[search_book]}")

#                                                   misol-7
##############################################################

weather = {"1-fevral": -2, "2-fevral": 0, "3-fevral": 3}
search_date = "2-fevral"
print(weather[search_date])

#                                                   misol-8
##############################################################

courses = {"Python": 250000, "C++": 300000, "Java": 280000}
search_course = "Python"
print(courses[search_course])

#                                                   misol-9
##############################################################

teams = {"Brazil": 1, "Argentina": 2, "France": 3}
search_team = "Argentina"
print(teams[search_team])

#                                                   misol-10
##############################################################

students = {"Ali": 85, "Vali": 90, "Hasan": 78, "Husan": 88, "Anvar": 92, "Madina": 95}

lst = list(students.items())  

for i in range(-1,len(lst)):
    for j in range(len(lst)-2, i, -1):
        if lst[j][1] < lst[j+1][1]:
            lst[j],lst[j+1] = lst[j+1], lst[j]

for i in range(3):
    print(f"{i+1}. {lst[i][0]} - {lst[i][1]}")

#                                                    misol-1
##############################################################    


products = {"olma": 15000, "banan": 18000, "uzum": 22000, "nok": 17000}
cart = {"olma": 2, "banan": 1, "nok": 3}

y=0
for i in cart.keys():
    for j in products.keys():
        if i == j:
            y += products[j] * cart[i]

print(y) 

#                                                    misol-2
##############################################################  

salaries = {"Ali": 5000000, "Vali": 5500000, "Hasan": 6200000, "Madina": 4900000, "Rustam": 5800000}

y = 0
c = 0
for i in salaries.values():
    y += i
    c += 1

print(y/c)   

#                                                     misol-3
###############################################################

students = {"Ali": 7, "Vali": 5, "Hasan": 12, "Madina": 9, "Husan": 6}

print(max(students.values()))

#                                                     misol-4
###############################################################

teams = {
    "Real Madrid": "Vinicius Jr.",
    "Barcelona": "Pedri",
    "Manchester City": "Erling Haaland",
    "Bayern Munich": "Harry Kane"
}
search_team = "Manchester City"

print(teams[search_team])

#                                                     misol-5
###############################################################

salaries = {"Dasturchi": 7000000, "Menejer": 8500000, "HR": 6000000}

for i in salaries.values():
    print(i*0.1)

#                                                     misol-6
###############################################################

stock = {"olma": 10, "banan": 0, "uzum": 5, "nok": 0, "shaftoli": 3}
lst = []
for i in stock.keys():
    if stock[i] == 0:
        lst.append(i)

print(*lst)        

#                                                     misol-7
###############################################################

movies = {"Titanic": 195, "Avatar": 162, "Interstellar": 169, "The Irishman": 209}
n = max(movies.values())
for k, v in movies.items():
    if v == n:
        print(k, v)

#                                                     misol-8
###############################################################

grades = {
    "Ali": {"Matematika": 85, "Fizika": 90, "Ingliz tili": 78},
    "Vali": {"Matematika": 88, "Fizika": 85, "Ingliz tili": 82},
    "Hasan": {"Matematika": 92, "Fizika": 80, "Ingliz tili": 85}
}

lst = [k for k in grades]


for k in grades[lst[0]]:
    y = 0
    ism = ""
    for kGr in grades:
        if grades[kGr][k]>y:
            y = grades[kGr][k]
            ism = kGr
    print(f"{k} boycha eng yuqorisi {ism}: {y}")        

#                                                     misol-9
###############################################################

resignations = [2020, 2021, 2020, 2019, 2021, 2021, 2020, 2019, 2020, 2021, 2019]

st = set(resignations)

y = 0
yr = 0
for i in st:
    if resignations.count(i) >= y:
        y = resignations.count(i)
        yr = i
print(f"Eng kop xodim ketgan yil: {yr} ({y} ta)")        

#                                                     misol-10
###############################################################