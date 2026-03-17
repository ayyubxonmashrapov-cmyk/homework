# lst = [1, 2, 33, 5, 6, 7, 7]
# n = 8

# for i in range(len(lst)):
#     for j in range(i, len(lst)):
#         if lst[i] + lst[j] == n:
#             print(i, j)
#                                              1-misol      
######################################################

# lst = [1, 4, 6, 8]

# lst1 = [i*2 for i in lst]

# print(lst1)    

#                                              2-misol
######################################################


# lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# lst1 = [tuple(t[i] if i != len(t)-1 else 100 for i in range(len(t))) for t in lst]

# print(lst1)

#                                              3-misol
######################################################


# lst = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]

# lst = [i for i in lst if i != ()]

# print(lst)   

#                                              4-misol
######################################################


# lst = [
#     ('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'),
#     ('item4', '5.75'), ('item5', '18.30'), ('item6', '3.20'),
#     ('item7', '42.1'), ('item8', '0.99'), ('item9', '33.0'),
#     ('item10', '7.8'), ('item11', '21.45'), ('item12', '12.1')
# ]

# for j in range(len(lst)-1):
#     for i in range(len(lst)-2, j-1, -1):
#         if(float(lst[i][1]) < float(lst[i+1][1])):
#             temp = lst[i]
#             lst[i] = lst[i+1]
#             lst[i+1] = temp
           
# print(lst)       
        
#                                              5-misol
######################################################



# s = "python 3.0"

# t = tuple(i for i in s)

# print(t)

#                                              6-misol
######################################################


# lst = [1, 2, 3, 4]
# prefix = "emp"
# lst = [f"{prefix}{i}" for i in lst]

# print(lst)

#                                              7-misol
######################################################


# gap = "salom aziz qalaysan wed fewfegwgeg"

# gap = gap.split(" ")

# for i in range(len(gap)-1):
#     for j in range(0,len(gap)-1-i):
#         if len(gap[j]) > len(gap[j+1]):
#             temp = gap[j]
#             gap[j] = gap[j+1]
#             gap[j+1] = temp
# print(gap)            

#                                              8-misol
######################################################


# lst = [12, 'salom', 4.5, 'dunyo', True]
# lst1 = []
# for i in lst:
#     if type(i) == str:
#         lst1.append(i)

# print(lst1)

#                                              9-misol
######################################################


# t = (-3, 5, 0, 9, -1, 4)

# t = tuple(i for i in t if i > 0)

# print(t)

#                                             10-misol
######################################################


# lst = ['salom', 23, 'dunyo', 5, 100, 'python']
# strs = []
# nums = []
# tempS = ""
# tempN = 0
# for i in lst:
#     if type(i) == str:
#         if len(i) < len(tempS):
#             tempS = i
#             strs.insert(0,i)
#         else:
#             strs.append(i)
#     else:
#         if i >= tempN:
#             tempN = i
#             nums.insert(0,i)
#         else:
#             nums.append(i)    


# print(strs,nums, sep="\n")

#                                             11-misol
######################################################


# lst = [(5, 10), (1, 20), (12, 30), (3, 15), (8, 25), (2, 5)]

# for i in range(len(lst)-1):
#     for j in range(0,len(lst)-1-i):
#         if lst[j][0] > lst[j+1][0]:
#             temp = lst[j]
#             lst[j] = lst[j+1]
#             lst[j+1] = temp

# print(lst)
 
#                                             12-misol
######################################################


# lst = [1, 2, 3, 4]

# lst = [i * i for i in lst]

# print(lst)

#                                             13-misol
######################################################



# lst = ['salom', 'dunyo', 'python']

# lst = [i.title() for i in lst]

# print(lst)

#                                             14-misol
######################################################

# t = (1, 2, 3, 4, 5)

# y = 0 

# for i in t:
#     y+=i

# print(y)    

#                                             15-misol
######################################################




