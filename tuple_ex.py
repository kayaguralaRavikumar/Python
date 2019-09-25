# tuple --> class
t1 = (10, 12.5, 'python', ['a', 'b'], (10, 20))
t2 = tuple([10, 20, 30])
print(t1)
print(t2)
print(t1[1:4])
i = t1.index(12.5)
c = t1.count(t1[2])
print(i, c)
# tuple to list
t3 = (10, 20, 30)
l2 = list(t3)
print(l2)
# list to tuple
l3 = [10, 20, 30]
t4 = tuple(l3)
print(t4)
# Tuple to dictionary
# 1 - way
e = enumerate(t4)
print(list(e))
print(dict(enumerate(t4)))
# 2 - ways
keys = ['a', 'b']
values = [10, 20, 30]
z = zip(keys, values)
print(list(z))
print(dict(zip(keys, values)))
