# set Class
# Collection of elements
# unordered Collections
# NO Index
# No Key
# mutable
# hold only immutable objects
# unique values

s1 = {10, 10, 'py', 'py'}
s1.add(20)
s1.add(20)
print(s1)

r1 = s1.remove(20)
r2 = s1.pop()
print(r1, r2, s1)

l1 = [10, 10, 20, 20]
s2 = set(l1)
s3 = {10, 20, 30, 30}
l2 = list(s3)
print(s2, s3)

s4 = {10, 20, 30, 40}
s5 = {30, 40, 50, 60}
s6 = s4.union(s5)
s7 = s4.intersection(s5)
s8 = s4.difference(s5)
print(s6, s7, s8)
