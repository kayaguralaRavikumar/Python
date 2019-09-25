a = 20
if a == 10:
    print('a eq 10')
if a > 10:
    print('a gt 10')
if a < 10:
    print('a lt 10')

a = 5
if a == 10:
    print('a eq 10')
elif a > 10:
    print('a gt 10')
elif a < 10:
    print('a lt 10')

a = -1
if a == 10:
    print('a eq 10')
elif a > 10:
    print('a gt 10')
elif a < 10:
    print('a lt 10')
else:
    print('not found')

s = 'python'
if s != 'java':
    print('not java')
if not s.startswith('s'):
    print('start')
if 'th' in s:
    print('substr th found ')

l1 = [10, 20, 30]
l2 = l1
l3 = l1.copy()
if l1 == l3:
    print('contents ae same')
if l1 is l2:
    print('id are same or refers same object')
if 30 in l1:
    print('30 found')

d = {'a': 10, 'b': 20}

if 'b' in d:
    print('key-b found')
if 20 in d.values():
    print('20 found')
if ('b', 20) in d.items():
    print('item found')

l = [['h', 'i']]
if ['h', 'i'] in l:
    print('found')

# --------------------- loop -----------------------------
s = 'python'
for a in s:
    print('a=', a)

b = 'java'
l = [10, 20, 30]
for b in l:
    print('b=', b)
print(b)

d = {'a': 10, 'b': 20}
for k in d:
    print(k, d[k])
for v in d.values():
    print(v)
for i in d.items():
    print(i, i[0], i[1])
for i, j in d.items():
    print(i, j)
hosts = ['h1', 'h2']
ips = ['ip1', 'ip2']
for h, i in zip(hosts, ips):
    print(h, i)

# for(i=2,i<10,i+2)
r1 = range(10)
r2 = range(1, 10)
r3 = range(1, 10, 2)
print(list(r1), list(r2), list(r3), sep='\n')
r4 = range(10, 1, -1)
for i in range(2, 10, 2):
    print(i)
s = 'python'
print(list(range(len(s))))

for i in range(len(s)):
    print(s[i], end='')

comp = ['IBM', 'syni', 'sap', 'syn2']
for c in comp:
    if c.startswith('syn'):
        print('found')
        break
else:  # block  will after the for loop  completeds  . It will always executed  if we dont  provide break
    print('nf')

for d in comp:
    if d.startswith('syn'):
        print('some logic here')
    print('last stmt of for')

for d in comp:
    if not d.startswith('syn'):
        continue
    if d.startswith('syn'):
        print('some logic here')
    print('last stmt of for')

# ------------------ while loop --------------------------------
a = 0
while a < 10:
    print('a=', a)
    a = a + 1  # a+=1
s = 'python'
b = 0
while b < len(s):
    print(s[b])
    b = b + 1

l = [10, 20, 30]

while l:
    x = l.pop()
    print('processed:', x)

# helpanddir
l=[]
print(dir(l))
print(help(l.append))