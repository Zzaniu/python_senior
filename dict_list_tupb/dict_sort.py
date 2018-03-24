#coding=utf-8

# 模拟用字典记录选手答题排名和时间，字典按顺序记录下来
# 因为字典保存的时候是hash，无序的，所以调用OrderedDict模块用来生成一个有序的字典

from time import time
from random import  randint
from collections import OrderedDict


players = list("ABCDEFGH")
d = OrderedDict()
start_time = time()

print "开始答题..."
for i in xrange(8):
    raw_input()
    p = players.pop(randint(0, 7-i))
    end_time = time()
    print i + 1, p, end_time - start_time,
    d[p] = (i + 1, end_time - start_time)

print
print "-" * 20

for k in d:
    print k, d[k]