set1={1,2,3,4,5,6}	
set2={4,5,6,7,8,9}
y=0
y1=0
for i in set1.difference(set2):
    y+=i

for i in set1.intersection(set2):
    y1+=i

print(y - y1 if y > y1 else y1 - y)

#                                          misol 1
##################################################

set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}

a = set1.intersection(set2)#.difference(set3)
print(a)

#                                          misol 2
##################################################

set1={4,5,6,7,8,9}	
set2={5,6,7,10,11}

y=0
y1=0
for i in set1.symmetric_difference(set2):
    y+=i

for i in set1.intersection(set2):
    y1+=i

print(y - y1)

#                                          misol 3
##################################################

set1={"Artel","Alif","Yandex", "Google", "Meta"}
set2={"Google", "Apple", "Amazon", "Meta"}
set3={"Alibaba", "Uzum", "Meta", "Google", "Amazon"}


a = set1.intersection(set2).intersection(set3)

b = set1.symmetric_difference(a)
print(a)

print(b)

#                                          misol 4
##################################################


set1={2,3,4,5,6}
set2={4,5,6,7,8,9}

y = 0
for i in set1.symmetric_difference(set2):
    y+=i
print(y)    

#                                          misol 5
##################################################

set1={100, 20, 45, 80, 70, 50}
set2={30, 55, 70, 60, 32, 100}

a = set1.intersection(set2)
y=0
l=0
for i in a:
    y+=i
    l+=1
print(y/l)    

#                                          misol 6
##################################################


nums1 = [1,2,2,1]
nums2 = [2,2]

a = list(set(nums2).intersection(set(nums1)))

print(a)

#                                          misol 7
##################################################

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

a = list(set(nums1).difference(set(nums2)))
b = list(set(nums2).difference(set(nums1)))
print([a,b])

#                                          misol 8
##################################################
