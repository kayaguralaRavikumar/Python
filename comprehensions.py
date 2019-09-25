# Comprehensions
l1 = [i for i in range(10)]
print('l1=', l1)
l2 = [j * j for j in l1 if j % 2 == 0]
print('l2=', l2)
l3 = [j + j if j % 2 == 0 else j + 1 for j in l1]
print('l3=', l3)

t1 = (j + j if j % 2 == 0 else j + 1 for j in l1)  # creates  generator  object. need to convert to get output.
print('t1= ', tuple(t1))

keys = ['a', 'b']
values = [10, 20]
d = {k: v for k, v in zip(keys, values)}
print('d=', d)

l4 = [(lambda i: i * i)(a) for a in l1]
print('l4', l4)

d3 = {k: (lambda i: i + i)(v) for k, v in zip(keys, values)}
print('d3=', d3)
