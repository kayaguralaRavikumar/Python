# def add1(a, b):
#     print('result is :')
#     print(a + b + a)
#     print('end  of res')
#
#
# def sub1(a, b):
#     print('result is :')
#     print(a - b - a)
#     print('end  of res')
#
#
# add1(10, 20)
# sub1(10, 20)


def mydec(fucn):
    def decorated_funct(x, y):
        print('result is :')
        fucn(x, y)
        print('End of res')

    return decorated_funct


@mydec
def add2(a, b):
    print(a + a + a)


add2(100, 200)


def add3(a, b):
    print(a + b)


f = mydec(add3)
f(10, 30)

# my(add3,10,20)
