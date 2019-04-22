list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

for i in range(len(list1)):
    a = list1[i] + list2[i]
    print(a)

for a, b in zip(list1,list2):
    print(a+b)