MB = 150                                                                    #1
MBs = 3.125
print(MB / MBs)

son = int(input("son kiriting: "))                                          #2
y = 0
while son:
    n = son % 10
    son = son // 10
    y += n
print(y)


son = int(input("saqol oldizmi: "))                                         #3
tolov = 0
if son:
    tolov += 10000

son = int(input("Soch oldizmi: "))
if son:
    tolov += 25000

print(tolov)


username = input("username kiriting: ")                                     #4
print(username.lower())
print(f"@{username} \nBunday yuzer bor.")

son = 40000                                                                 #5
kishi = int(input("necha kishi: "))
print(f"jami {son*kishi}so'm\nkishi boshiga {son}so'm")

ismSharf = input("ism va familya kiriting: ")                               #6
print(f"birinchi harf: {ismSharf[0]}\noxirgi harf {ismSharf[-1]}")


ism = input("ism kiriting: ")                                               #7
print(f"{ism[0:2]}{ism[-2:]}" * 3)

matn = input()                                                              #8
print("\t",matn.title())


matn = input()                                                              #9
print(len(matn))

aski = ord(input("1ta harf: "))                                             #10
print(chr(aski+3))

soz = input()                                                               #11
print(soz[::-1])

parol = input("parol: ")                                                    #12
if len(parol) > 7:
    print("yaxshi parol")
else:
    print("Juda qisqa")    

nomer = input("nomer: ")                                                    #13
nomer = nomer.replace("+", "")
print(nomer.replace("-", ""))

matn = input()                                                              #14
print(matn.isalpha())
print(matn.isdigit())
print(matn.isalnum())
    

name = input()                                                              #15
summa = 0

for ch in name:
    code = ord(ch)  
    summa += code

print(summa)