# file = open("file.txt","r")                                              # 1
# for i in file.read().split():
#     if int(i) % 2 == 0:
#         print(i)
# file.close()

# file = open("file.txt","r")                                              # 2
# print(max([int(i) for i in file.read().split()]))
# file.close()

# file = open("file.txt", "r")                                             # 3       
# lst = file.read().split()
# print(list[0] * 2) 
# file.close()


# from functools import reduce                                             # 4        
# file = open("file.txt", "r")
# lst = file.read().split()
# print(sum([len(i) for i in lst])/len(lst)) 
# file.close()

# file = open("file.txt", "r")                                             # 5
# lst = file.read().split(". ")
# mx = 0
# mxG = ""
# for i in lst:
#     if len(i) > mx:
#         mx = len(i)
#         mxG = i
# print(mxG)
# file.close()

# n = int(input("son: "))                                                  # 1        
# file = open("file.txt", "w")
# for i in range(1,n+1):
#     file.write(f"{i}\n")
# file.close()


# array = [-3, 5, -1, 7, -6]                                               # 2
# fplus = open("plus.txt", "w")
# fminus = open("minus.txt", "w")

# for i in array:                                                          
#     if i > -1:
#         fplus.write(f"{i}\n")
#     else:
#         fminus.write(f"{i}\n")    
# fplus.close()
# fminus.close()

# n = int(input("son: "))                                                  # 3                                        
# file = open("file.txt", "w")
# for i in range(1,n+1):
#     file.write(f"{i**2}\n")
# file.close()

# lst = ["Otabek", "Anvar", "Ulug‘bek", "Sherzod", "Bekzod"]               # 4
# file = open("file.txt", "w")
# for i in lst:
#     file.write(f"{i}\n")
# file.close()

# soz = input("soz: ")                                                     # 5      
# file = open("file.txt", "w")
# for i in soz:
#     file.write(f"{i}\n")
# file.close()


    