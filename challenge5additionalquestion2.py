list1=[i for i in range(1,30,2) ]#1
print(list1)
newList=[i for i in list1 if i%3==0]
print (newList)

list1=[10,20,30,40,50,60,70,80] #2
print(list1[2:7])

tuple=(1,2,3)#3
#tuples are immutable so append and insertion is not possible
list2 = list(tuple)
list2.append(4)
print(list2)
list2.insert(2,55)
print(list2)
print(list2[-2])