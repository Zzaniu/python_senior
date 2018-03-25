#coding=utf-8

from itertools import chain
from random import randint

# 串行
e1 = [randint(60, 100) for _ in xrange(40)]
e2 = [randint(60, 100) for _ in xrange(41)]
e3 = [randint(60, 100) for _ in xrange(44)]
e4 = [randint(60, 100) for _ in xrange(39)]

count = 0

for s in chain(e1,e2,e3,e4):
    if s > 90:
        count += 1

print count

# 并行
chinese = ['a', 'b', 'c', 'd']
math = [1,2,3,4,5]

l = []
for i in zip(chinese, math):
    l.append(i)

print l
