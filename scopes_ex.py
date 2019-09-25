x = 10  # global scope


def f1():
    global x  # to ref  global scope
    x = 20  # enclosed scope

    def f2():
        # nonlocal x  # to ref  enclose scope
        x = 30  # local  scope
        print('f2', x)

    f2()
    print('f1', x)


f1()
print('global', x)
print(dir(__builtins__))

# if use global variable but variable is  not create before  then  will create one for us ;
# local , enclosed , global , built in order it will check

count = 0


def ca():
    global count
    count += 1


def da():
    global count
    count -= 1

ca()
ca()
count = 100
da()
print('total accounts', count)
