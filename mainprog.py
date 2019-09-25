'''
Collect modules are package
Two way to access  modules in different  folder
'''

import mymodule
import sys

# print(sys.path)
# sys.path.append(r'c:\training\lib')
print(mymodule.msg)
print(mymodule.sub(10, 20))

import mymodule as m  # alias

print(m.msg)
print(m.sub(10, 20))

from mymodule import msg, sub  # import specific function only

print(msg)
print(sub(10, 20))

from mymodule import msg as m, sub as s  # import specific function only

print(m)
print(s(10, 20))

'''
from  package import
'''

import Project.net.mymodule
import sys

# print(sys.path)
# sys.path.append(r'c:\training\lib')
print(Project.net.mymodule.msg)
print(Project.net.mymodule.sub(10, 20))

import Project.net.mymodule as m  # alias

print(m.msg)
print(m.sub(10, 20))

from Project.net.mymodule import msg, sub  # import specific function only

print(msg)
print(sub(10, 20))

from Project.net.mymodule import msg as m, sub as s  # import specific function only

print(m)
print(s(10, 20))
