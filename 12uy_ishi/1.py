from random import randint


def tortburchak_yasa(n: int, m: int) -> None:                                      #1
    for i in range(n):
        print(" * " * m)

def raqamlar_yigindisi(royxat: list, n: int) -> int:                               #2
    return sum(royxat[:n])         

def raqamgacha_yigindi(son:int)-> int:                                             #3
    return sum(range(son+1))

def n_tasodifiy_son(n:int)->int:                                                   #4
    return randint(10**(n-1),10**n - 1)

def boluvchilari(n: int) -> list:                                                  #5
    faktorlar = []
    for i in range(1,n//2+1):
        if n % i == 0:
            faktorlar.append(i)
    return faktorlar        

def musbatlari(royaxat: list)->list:                                               #6
    musbat = []
    for i in royaxat:
        if i > -1:
            musbat.append(i)
    return musbat


def katHarf_value(n: dict) -> dict:                                                #7
    for i in n.keys():
        n[i] = n[i].upper()
    return n    

def dict_yasa(lst1:list, lst2:list) ->dict:                                        #8
    if len(lst1) != len(lst2): return None
    return dict(zip(lst1, lst2))    

def maxTop(lst: list) -> int:                                                      #9
    return max(lst)

def pANDs(a: int, b: int) -> tuple:                                                #10
    return tuple([(a+b)*2, a*b])


# print(tortburchak_yasa(3,5))
# print(raqamlar_yigindisi([1,2,3], 2))
# print(raqamgacha_yigindi(7))
# print(n_tasodifiy_son(3))
# print(boluvchilari(30))
# print(musbatlari([3,5,-4,2,-3,-3,4,-5]))
# print(katHarf_value({"Ism": "Ali", "Familya": "Kamolov", "Manzil": "Angren shahri"}))
# print(dict_yasa(["Jon", "Jeyms", "Piter", "Tony"], ["Vik", "Bond", "Parker", "Stark"]))
# print(maxTop([3, 6, 8, 1, 0]))
# print(pANDs(5,6))


#                                                                                           
################################################################################################

def raqamli_ildizi(n: int) -> int:                                                 #1
     
    while n > 10:
        y = 0 
        while n != 0:
            y += n%10
            n //= 10
        n = y
    return n

def satrlar_farqi(str1: str, str2: str) -> int:                                    #2
    a = len(str1)
    b = len(str2)
    n = b if b > a else a
    for i in range(1,n+1):
        if str1[:i] != str2[:i]:
            return i-1
    return -1    

def binom(n: int, k: int) -> int:                                                  #3
    y = 1 
    y1 = 1
    y2 = 1
    for i in range(1,n+1):
        y *= i
    for i in range(1,k+1):
        y1 *= i 
    for i in range(1,n-k+1):
        y2 *= i
    return y//(y1 * y2)            
    
def eng_yaqin_son(l: list, n: int) -> int:                                         #4
    lst = []
    for i in l:
        if i < n:
            lst.append(i)
    return max(lst)            

def birxil_harflar(str1: str, str2: str) -> int:                                   #5
    lst = list(str2)
    y = 0
    for i in lst:
        if i in str1:
            y += 1
    return y        

def top_hammasini(text: str, letter: str) -> int:                                  #6
    lst = []
    start = 0
    for i in range(len(text)):
        i = text.find(letter, start)
        if i == -1:
            break
        lst.append(i)
        start = i + 1
    
    return lst
         
def ortacha(*args) -> int:                                                         #10
    return sum(args)/len(args)

def dct(**qwargs) -> list:                                                         #11
    return qwargs.get("umumiy") - qwargs.get("chegirma") if qwargs.get("chegirma") is not None else qwargs.get("umumiy")

def birxil_joy_yigindi(set1: set, set2: set) -> int:                               #12
    lst = set1.intersection(set2)
    return sum(lst)




# print(raqamli_ildizi(45893))
# print(satrlar_farqi("1234567", "12345642"))
# print(binom(6, 4))
# print(eng_yaqin_son([1,6,3,5,7,99,11], n=10))
# print(birxil_harflar("python", ""))
# print(top_hammasini("men ,mohir dasturchiman", "m"))
# print(ortacha(3,4,5))
# print(dct(umumiy=550))
# print(birxil_joy_yigindi({1,2,3,4,5,6,7},{4,5,6,7,8,9}))

#                                                                                           
################################################################################################

def dct_qil(lst: list) -> dict:                                                    #1
    dct = {}
    for i in lst:
        dct[f"{i[0]}"] = [i[j] for j in range(1,len(i))]
    return dct    

def hmm(lst: list) -> list:                                                        #2
    lst = list(set(lst))
    if len([i for i in lst if i % 2 == 0]) != len([i for i in lst if i % 2 != 0]):
        return
    lst1 = []
    a = len(lst)
    if lst[0] % 2 == 0:
        for i in range(0,a,2):
            lst1.append(lst[a-2-i])
            lst1.append(lst[i+1])
    else:
        for i in range(0,a,2):
            lst1.append(lst[i])
            lst1.append(lst[a-1-i])       
    return lst1

def hmm1(lst: list):                                                               #3
    for i in lst: 
        if i["age"] > 18 and i["cars"] > 1:
            print(i)

def hmm2(lst: list) -> list:                                                       #4
    lst1 = []
    for i in lst:
        lst1.append(sum(i))
    return lst1

def input_list() -> list:                                                          #5
    lst = list(input("Sonlarni kiriting: ").split())
    lst1 = []
    for i in lst:
        if int(list(i)[0]) % 2 == 0:
            lst1.append(int(i))
    return lst1  

def hmm3(lst: list) -> int:                                                        #6
    lst.sort(key=lambda x: str(x)[0])
    lst.reverse()
    st = ""
    for i in lst:
        st += str(i)
    return int(st)

def hmm4(lst: list) -> int:                                                        #7
    st = set(lst)
    s = 0
    for i in st:
        if lst.count(i) == 1:
            s += 1
    if s == 0:
        return -1          
    return s

def isAnagram(st: str) -> bool:                                                    #8
    if st == st[::-1]:
        return True
    return False

def hmm5(n: int):                                                                  #9
    print(sum([n%1000//100, n//1000]))
    print(sum([n%100//10, n%10]))

def hmm6(lst: list) -> list:                                                       #10
    lst1 = []
    a = len(lst)
    for i in range(a):
        for j in range(i+1,a):
            for l in range(j+1,a):
                if lst[i] + lst[j] + lst[l] == 0:
                    lst1.append([lst[i], lst[j], lst[l]])

    return lst1

def hmm7(n: int) -> int:                                                           #11
    a = n**0.5
    if a == a//1:
        return a
    return -1

def hmm8(n: int) -> str:                                                           #12
    a = len(str(n))
    lst = []
    for i in range(a, 0, -1):
        b = n//10**(i-1) * 10**(i-1)
        if b != 0:
            lst.append(str(b))
        n -= b
    return "+".join(lst)  

def hmm9(dct: dict) -> dict:                                                       #13
    a = max(dct.keys())
    for i in range(2,a+1,2):
        dct[i],dct[i-1] = dct[i-1],dct[i]

    return dct


# lst = [
#     [1, "Jean Castro", "V"],
#     [2, "Lula Powell", "V"],
#     [3, "Brian Howell", "VI"],
#     [4, "Lynne Foster", "VI"],
#     [5, "Zachary Simon", "VII"],
# ]
# print(dct_qil(lst), sep="\n")
# print(hmm([2,3,4,5,6,7,8,9,10, 11]))
# lst = [
#     {"Name": "Asil", "age": 9, "cars": 3},
#     {"Name": "Laziz", "age": 19, "cars": 2},
#     {"Name": "Sardor", "age": 25, "cars": 7},
#     {"Name": "Og`abek", "age": 5, "cars": 5},
# ]
# hmm1(lst)
# print(hmm2([(1, 2), (2, 3), (3, 4)]))
# print(input_list())
# print(hmm3([5,42,934,42]))
# print(hmm4([1,2,3,1,1,5,4]))
# print(isAnagram("asas"))
# hmm5(1234)
# print(hmm6([-1,0,1,2,-1,-4]))
# print(hmm7(82))
# print(hmm8(85723070))
# dict1 = {1:"ABC", 2:"DEF", 3:"GHI", 4:"JKL", 5:"MNO"}
# print(hmm9(dict1))


#                                                                                           
################################################################################################

def yigindi(tpl: tuple) -> int:                                   #1
    if tpl == ():  
        return 0
    
    a = tpl[0]
    if a % 2 == 0:
        return a + yigindi(tpl[1:])
    else:
        return yigindi(tpl[1:])

def toq_chiqaz(n: int):                                           #2
    if n == 0:
        return 
    toq_chiqaz(n-1)
    if n % 2 != 0:
        print(n)    

def juft_chiqaz(n: int):                                          #3
    if n == 0:
        return 
    if n % 2 == 0:
        print(n)  
    juft_chiqaz(n-1)
      
def raqam_teskari(n: int):                                        #4
    if n == 0:
        return
    print(n%10)
    raqam_teskari(n//10)

def nechta_xona(n: int) -> int:                                   #5
    if n< 10:
        return 1
    return 1 + nechta_xona(n // 10)

def qoldiq(n: int, b: int) -> int:                                #6
    if n < b:
        return n

    return qoldiq(n-b, b)

def pow_qil(n: int, pow: int) -> int:                             #8
    if pow == 0:
        return 1
    if pow < 0:
        return None 
    pow-=1
    return n * pow_qil(n, pow)

def naoborot(st: str) -> str:                                     #9
    return st[::-1]

def kopaytir(n: int, b: int) -> int:                              #10
    if b == 0:
        return 0
    return n + kopaytir(n, b-1) 

def fibonachi(f0: int, f1: int, n: int) -> int:                   #11
    if n == 0:
        return f0
    elif n == 1:
        return f1
    return fibonachi(f0, f1, n-1) + fibonachi(f0, f1, n-2)

# print(yigindi((2,3,5,6,3,7,8,4,8,3)))
# toq_chiqaz(6)
# juft_chiqaz(6)
# raqam_teskari(1234)
# print(nechta_xona(1234756435))
# print(qoldiq(17, 6))
# print(pow_qil(5, 2))
# print(naoborot("buyya"))
# print(kopaytir(9,5))
# print(fibonachi(0,1,9))

#                                                                                           
################################################################################################

# a,b = 3,5                                                                                  #1
# print((lambda x, y: x if x > y else y)(a,b))                                                    

# tpl = (1,2,3,4,5,6)                                                                        #2
# print((lambda x: sum(tpl)/len(tpl))(tpl))

# lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]                                             #3
# lst.sort(key=lambda x: x[1])
# print(lst)

# n = 5                                                                                      #4
# print((lambda x: x*3)(n))

# n = 5                                                                                      #5
# print((lambda x: x*2)(n))

# n = 5                                                                                      #6
# print((lambda x: x**3)(n))

# print((lambda x, y: True if x[-1] == y[-1] else False)("caeri","cari"))                    #7

# st = "2020-01-15"                                                                          #8
# print((lambda x: {"year": int(st.split("-")[0]),"month": int(st.split("-")[1]),"day": int(st.split("-")[2])})(st))

# print((lambda x: True if type(x) == str or type(x) == int else False)("afgafsa"))          #9

# print((lambda x: len(x) == 6)("dastuur"))                                                  #10

# print((lambda x: x == int(str(x)[::-1]))(123213))                                          #11
