#Trainer 
'''
Prabhu - 9986169696

'''
#Python   
'''
case sentitive langague
'''
#comments
'''
Triple quote  - Multi comment 
Double triple quote - Multi comment 
# -single comment
Triple and Double quote -- create the a object in the memory . So try to avoid it.

Block Description :-
Always use the Triple quote. 

It will help in showing the content of the function with help command 
'''
#core_datatypes
#Number
#strings
'''
List -- collections  of elements (Array). List can be modified.
Tuple --Can't change. For master data.
Dictionary -- Key value pairs 
Set  -- Store all unique
Set operations -- union , intersect , minus.
'''
#doubts
''' 
what is use of Tuple compare to list and other collections
What exactly the concept of mutable and immutable designed .what are the benefits of it.
Compiled and interperted execution. which one is best.   
'''
#Points  
'''
arguments for print function
Sep  - separator
end  - 
file -
flush -  
'''
#memory
'''
Stack, heap
All objects will store in heap
All referencewill be store in Stack 
Refernce <---- objects
a <----------- 10 
'''
# Immutables,Mutable
'''
Immutables - Can't change the object once created
 Number ,strings ,Tuple 
Mutable- Can change the  object  once created
 List , Dictionary , Set 

All immutable objects create new objectand reference to its variable name

Reference Counter  

        object   Refernce Count
a ----> 100  -----  0  
a ----> 200  -----  1
b ----> 300  -----  1

ReferenceCount is used for garbage collections
'''
# Executions
'''
Machine code

Source code + M.c info 
                                                    adding Machine info 
Test.py(Source Code) ------> intermediate code(Byte Code)-------> Machine code

PVM - Python virtual machine

'''
# Deployment
'''
1.Sc
2.Executables (pyinstaller, py2exe utilites . This will combine both byte code and PVM) 
3.tar,Zip,whl 
'''
#Number
a = 10
b = 12.5
c = 0b1010
d = 0x12
e = 0O12
f = int(10)
print(a,b,c,d,e,sep = ';',end = '.') 
print('test')
print(id(a))
a =100
print(id(a))
print(type(a)) #
print(type(a).__name__)
