# functions ----- Implementaion
from builtins import print


def add():
    a = 10
    b = 20
    c = a + b
    print(c)


add()


def add2():
    a = 10
    b = 20
    c = a + b
    # return c
    # return
    # return [a,b,c]
    # return a, b, c
    # return dict(zip([a, b, c]))
    return (a + b) / (a - b)


r1 = add2()
print(r1)


# positional args
def add3(a, b):
    return a + b


r2 = add3(10, 20)
print(r2)

r3 = add3('py', 'py')
print(r3)


# default values

def add4(a, b=10):
    return a + b


r5 = add4(10)
print(r5)
r6 = add4(10, 20)
print(r6)


# variable arguments

def add5(a, b=10, *c):
    print('extra arg passed :', c)
    r = a + b
    for i in c:
        r = r + i
    return r


r7 = add5(10)
print(r7)
r8 = add5(10, 20, 30, 40, 50)
print(r8)

l = [10, 20, 30, 40, 50]
r9 = add5(*l)  # unpacking
print(r9)


# * - uses  for packing and unpacking variables
# keyword only arguments
def add6(a, b=10, *c, d, e):
    r = a + b + d + e
    for i in c:
        r += i
    return r


r10 = add6(10, 20, 30, 40, 50, e=60, d=70)
print(r10)


# variable keyword argument

def add7(a, b=10, *c, d, e, **f):
    print('remaining keyword only args', f)
    r = a + b + d + e
    for i in c:
        r = r + i
    for j in f.values():
        r = r + j
    return r


r11 = add7(10, 20, 30, 40, 50, d=60, e=70, x=80, y=90)
print(r11)

# function  without  args
# function  with  args
# function  default values (always keep defalut last)
# function  with positional  args
# function  with  key word  args
# function  with  variable keyword  args


# add()
# add(a,b)
# add(a,b=10)
# add(b=10,a) error
# add(*a)
# add(**a)
# add(*a,**b)
# add(*,a,b)
