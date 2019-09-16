Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("aman")
aman
>>> int(input("enter the value:"))
enter the value:20
20
>>> b=int(input("enter the value:"))
enter the value:30
>>> a=int(input("enter the value:"))
enter the value:20
>>> c=a+b
>>> c
50
>>> a=[1,2,4,8,-1,2.0,2.2,'b']
>>> a
[1, 2, 4, 8, -1, 2.0, 2.2, 'b']
>>> a.append(5)
>>> a
[1, 2, 4, 8, -1, 2.0, 2.2, 'b', 5]
>>> a.append('s')
>>> a
[1, 2, 4, 8, -1, 2.0, 2.2, 'b', 5, 's']
>>> b=[4,5,8,7]
>>> a.extend(['a','b','c'])
>>> a
[1, 2, 4, 8, -1, 2.0, 2.2, 'b', 5, 's', 'a', 'b', 'c']
>>> a.extend(b)
>>> a
[1, 2, 4, 8, -1, 2.0, 2.2, 'b', 5, 's', 'a', 'b', 'c', 4, 5, 8, 7]
>>> a=['1',2,3]
>>> b=[4,5,6]
>>> a+b
['1', 2, 3, 4, 5, 6]
>>> 
a.index(-1)
Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    a.index(-1)
ValueError: -1 is not in list
>>> a.index(5)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.index(5)
ValueError: 5 is not in list
>>> a
['1', 2, 3]
>>> a.index(3)
2
>>> c=a+b
>>> c
['1', 2, 3, 4, 5, 6]
>>> c.index(5)
4
>>> a=["cmr","good","college"]
>>> a
['cmr', 'good', 'college']
>>> a.insert(1,is)
SyntaxError: invalid syntax
>>> a.insert(1,"is")
>>> a
['cmr', 'is', 'good', 'college']
>>> 
a.replace("college","university")
Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    a.replace("college","university")
AttributeError: 'list' object has no attribute 'replace'
>>> a.replace["college","university"]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.replace["college","university"]
AttributeError: 'list' object has no attribute 'replace'
>>> a.replace[3,"university"]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.replace[3,"university"]
AttributeError: 'list' object has no attribute 'replace'
>>> a.replace(3,"university")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.replace(3,"university")
AttributeError: 'list' object has no attribute 'replace'
>>> 
a.remove(3)
Traceback (most recent call last):
  File "<pyshell#36>", line 2, in <module>
    a.remove(3)
ValueError: list.remove(x): x not in list
>>> a.remove("college")
>>> a.insert(3,"university")
>>> a
['cmr', 'is', 'good', 'university']
>>> 
a.pop(1)
'is'
>>> a
['cmr', 'good', 'university']
>>> a.reverse
<built-in method reverse of list object at 0x7fac61a65e48>
>>> a
['cmr', 'good', 'university']
>>> a
['cmr', 'good', 'university']
>>> 
