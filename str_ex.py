#str--> class name
#to store  all strings in different line use the  '

a  = 'person'
b  = "person's"
c  = '''person's height xyz" '''
e  = """person"""
f  = 'line11 \
        line2'
g  = '''line1
        line2 '''
h  = 'person\'s'
i  = 'c:\newfolder\test.py'
j  = 'c:\\newfolder\\test.py'
k  = r'c:\newfolder\test.py'
l  = 'wel come'

print (l)
print(len(l))
print(l[1])

#slicing
'''
: is used for slicing
variable[frm index : to index]
Start index is  inclusive
End index is  exclusive
'''
print(l[1:6])
print(l[1:]) #till end
print(l[:6]) #start  from  first index
print(l[:]) # entire string

j = l[:]
print(id(i) , id(j))

#Step
'''
Every occurance of the string 
'''
print(l[::-1])
print(l[1:6:2])
print(l[1:6:-2])
print(l[-1:-8:-1])

#negative indexes  will help to get end of the strings easily like logs  ,txt, pass,fail and all  
print(l[len(l)-4 :])
print(l[-4 :])

r1 = l.startswith('wel')
print(r1) #boolean object output
r2  = l.endswith('come')
print(r2)
r3 = l.isupper()
print(r3)
r4  = l.upper() # is lower and lower also are there
print(r4)
r5 = l.istitle()
print(r5)
r6 = l.title() #inticap  
print(r6)
r7 = l.capitalize()
print(r7)

s1 = 'hello'
s2 = 'world'
r8 = s1+s2
print(r8)
r9 = (s1 + '\n')  * 10
print(r9)
m='abc'
r11= m.isalpha()
n= '123'
r12= n.isdigit()
p = 'abc123'
r13 = p.isalnum() 
print(r11,r12,r13) 

#strip -- remove from end and begining like trim function 
q = '   wel  come  '
r15 = q.strip() 
r16 = q.lstrip() 
r17 = q.rstrip()
print(r15,r16,r17,sep  ='\n' ) 

s = '[wel[come][]'
r18 = s.strip(']w[e')
r19 = s.lstrip('w[')
r20 = s.rstrip('][e')
print(r18,r19,r20, sep='\n')

# split

k = 'wel come'
r21 = k.split()
print(r21[0])
r22 = k.split('e')
print(r22)

# index , find
r24 = k.find('a') #  it will give output  -1  when  not  found the  substring provided 
r23  = k.index('w') # index  will throw  error when not found the substring  provided
print(r23,r24) # index('e',3) , index('e',3,8)

r25 = k.count('e')
r26 = k.replace('e','E')

print(r25,r26) 

x =10
y =20
z = x+ y
r27 = 'add of x and y is Z'
r28 = 'add of {} and {} is {}'.format(x,y,z)
print(r28)
r29 = 'add of {1} and {0} is {2}'.format(x,y,z)
print(29)
#Py 3.5 onwards
r30  = f'add of {x} and {y} is {z}'
print(r30)
