msg = 'Module Demo'


def sub(a, b):
    return a - b


if __name__ == '__main__':
    print(__name__)
    print(__file__)
    print('test=', msg)
    print('test=', sub(10, 20))
