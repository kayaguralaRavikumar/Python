a = 10
try:
    r = a / b
    print(r)
except:
    print('some error')
print('Remaining code')

a = 10
#
# for i in range(5):
#     print('*')
print('**************')

try:
    r = a / b
    print(r)
except ZeroDivisionError:
    print('ZDE')
except (NameError, IndexError):
    print('NE or IE')
except KeyError as k:
    print('msg=', k)
print('reamining code')

print('**************')

l = []
try:
    print(l[1])
except Exception as e:
    print('e=', e)
    print('type=', type(e))

print('**************')

try:
    r = a / b
except:
    print('some error')
else:
    r = a / a
    print('in else')

print('**************')
try:
    r = a / b
except:
    print('In except')
finally:
    print('In finally')

result = 'Test Case failed'
try:
    assert 'success' in result, 'some test failed'
    print('test Success')
except AssertionError as ae:
    print('ae=', ae)

x = 10
y = 0
try:
    if y == 0:
        raise ZeroDivisionError
    print('stmnt 100')
    r = x / y
except:
    print('from raise')


class Myerror(Exception):
    def __init__(self, m):
        self.msg = m

    def __str__(self):
        return 'more desc=' + self.msg

try:
    if y == 0:
        raise Myerror('y is o')
except Myerror as me:
    print('me=', me)
