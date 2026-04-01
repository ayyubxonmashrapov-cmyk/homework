# sonlar = [1,2,3]                                                    #1
# yangi = list(map(lambda x: x * 3, sonlar))
# print(yangi)

# lst1 = [1, 2, 3]                                                    #2
# lst2 = [4, 5, 6]
# yangi = list(map(lambda x, y: x + y, lst1 , lst2))
# print(yangi)

# lst = ["olma", "uzum", "banan", "shaftoli"]                         #3
# print(list((map(lambda x: len(x), lst))))

# lst = [1,2,3]                                                       #4
# lst1 = [4,5,6] 
# lst2 = [7,8,9]
# print(list(map(lambda x,y,z: x*y*z, lst,lst1,lst2)))

# lst = ["molas", "lug", "apmal", "hsoyuq"]                           #5
# print(list(map(lambda x: x[::-1], lst)))

# lst = [1,4,2,3,5]                                                   #6
# print(list(map(lambda x: x**2, lst)))

# lst = ["olma", "uzum", "banan", "shaftoli"]                         #7
# print(list(filter(lambda x: len(x) == 5, lst)))

# lst = [3,7,9,14,7]                                                  #8
# print(list(filter(lambda x: x % 7 == 0, lst)))

# lst = [121, 34, 565, 78]                                            #9
# print(list(filter(lambda x: x == int(str(x)[::-1]), lst)))

lst = ["abc", "cba", "jkl"]
print(list(filter(lambda x: sorted(x) == sorted("bca"), lst)))