# Map
l = [100, 200, 300, 400]


def func(i):
    return i - 10


r1 = map(func, l)
r2 = map(func, list(r1))
print('r1=', list(r1))
print(list(r2))


# generator is concept of python. which create object at the time of call at once .It create on the call based one by one
# it can be used once only.

# Filter
def filt(j):
    return j > 100


r3 = filter(filt, l)
print('r3', list(r3))

# Reduce -- take 2 values do operation and  same operations  with output and  third  element

from functools import reduce


def red(p, q):
    return p + q


r4 = reduce(red, l)
print('r4=', r4)

# Lamda functions
'''
Lamda function is a function which dont have name 
Lamda function are one liner's  
Lamda function is aynonmus function  
'''
r5 = map(lambda i: i - 10, l)
print('r5=', list(r5))
r6 = filter(lambda j: j > 100, l)
print('r6=', list(r6))
r7 = reduce(lambda p, q: p + q, l)
print('r7=', r7)

a = lambda x, y: x + y
r8 = a(10, 20)
print('r8=', r8)
