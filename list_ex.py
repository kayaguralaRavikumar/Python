#list ---> class
'''
List can have any object
list will have indexby default 
mutable  - we can add,delete, modify the data
'''
l1 = list([10,20,30])
l2 =[10,12.5,'python', ['a','b']]
print(l1)
print(l2[0])
print(l2[0:3])

#list value in a list - list 
print(l2[2][1])

#update
l2[1] = 'java'
print(l2)

#concept Referencing
l= [10,20]
''' 
l ---> [ref1 , ref2]

ref 1  ----> 10
ref 2  ----> 20
ref 3  ----> 'java'

after update

l ---> [ref1,ref3]
'''

#add
l2.append(200)
print(l2) #add element at the end
l2.insert(2,300)
print(l2)
l3 = [10,20]
l4 = ['a','b']
l5 = l3 + l4
l6 = l3 * 10
print (l5,l6,sep='\n')
l3.extend(l4)
print(l3)

# remove
r1= l1.pop()
print(r1,l1)
r2 = l1.pop(1)
print(r2,l1)
r3 = l2.remove('python') # remove function will return none(null)
print(r3,l2)

#some other functions
l7 = [30,10,40]
l7.sort()
print(l7)
l8=['z','a','b']
l8.sort(reverse =True)
print('desc', l8)
l9 = [10,'a',20,'b']
l9.reverse()
print(l9)
i = l9.index('a')
c = l9.count('a')
print(i,c)
l9.clear() #make list empty 
print(l9)

l = [10,['a','b']]
m = l # reference copy (if you change any to L and M it will impact both)
N = l.copy() # shallow copy (No impact of N as change of L)

# deep copy - it is not built method of list class. required  libary - import copy
import copy
p = copy.deepcopy(N)
print(p)


