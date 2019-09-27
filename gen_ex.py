l = [1, 2, 3, 4]


def squares(M):
    res = []
    for i in M:
        res.append(i * i)
    return res


r1 = squares(l)
for a in r1:
    print('a=', a)


def gen_squares(m):
    for j in m:
        yield j * j
    for k in m:
        yield k + k


r2 = gen_squares(l)
for b in r2:
    print('b=', b)
print('type of  r2 =', type(r2))
print('r1,r2 =', r1, list(r2))
