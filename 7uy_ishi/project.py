from faker import Faker
import random

faker = Faker("uz_UZ")

print("================================================")
print("| №  |       Ism Familiya        | Yosh | Kurs |")
print("================================================")

for i in range(1, 10):
    name = faker.name()
    age = random.randint(18, 28)
    year = random.randint(1, 4)

    print(f"| {i:<3}| {name:<26}| {age:<5}|  {year:<4}|")

print("================================================")
