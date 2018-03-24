#coding=utf-8

#randint 返回参数指定范围内的随机的整数
from random import randint
from timeit import timeit, repeat
from collections import OrderedDict


# list

list_a = [1,2,3,4,5]
# 是列表中的元素反序，改变了原来的列表
list_a.reverse()
print list_a


# 统计列表中某元素的数量，使用list.count(元素)
data = [randint(-10,10) for _ in xrange(10)] #python3使用range
print(data)

data_gt_0 = filter(lambda x:x>=0, data)
print(data_gt_0)

data_gt_1 = [x for x in data if x >= 0]
print(data_gt_1)

print(timeit('filter(lambda x:x>=0, data)', 'from __main__ import data', number=10))
print(timeit('[x for x in data if x >= 0]', 'from __main__ import data', number=10))
print(repeat('filter(lambda x:x>=0, data)', 'from __main__ import data', number=10))
print(repeat('[x for x in data if x >= 0]', 'from __main__ import data', number=10))
# end_list

# dict
dict_1 = {x:randint(60, 100) for x in xrange(1,21)}
print "dict_1.items() = ", dict_1.items()
print "dict_1 = ", dict_1
# iteritems生成一个生成器（迭代器），items生成一个完整的列表(列表里面的元素为元组，元组包含键和值)
dict_filter = {k : v for k, v in dict_1.iteritems() if v > 90}
print "dict_filter = ", dict_filter
# 字典排序，x[0]按键排序，x[1]按值排序,reverse=True为降序，默认为False升序
dict_sort_to_tpub = sorted(dict_1.iteritems(), key=lambda x:x[1], reverse=True)
print "dict_sort_to_tpub = ", dict_sort_to_tpub
dict_sort = {k:v for k, v in dict_sort_to_tpub}
print "dict_sort = ", dict_sort


# 字典生成的时候是一个乱序的，用OrderedDict()构造的字典不是乱序的
d = OrderedDict()
for x in dict_sort_to_tpub:
    d[x[0]] = x[1]
print("d = ", d)
print("d[1] = ", d[1])
for k in d:print k,
print #换行
# end_dict

# set
s = set(data)
s_filter = {x for x in s if x % 3 == 0}
print "s_filter = ", s_filter
# end_set