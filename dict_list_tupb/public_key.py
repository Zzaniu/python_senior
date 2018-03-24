#coding=utf-8


from random import randint, sample


# 'abcdef'中随机取样随机个
print(sample('abcdef', randint(3, 6)))

# 构建一个随机字典
dict_1 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}
print(dict_1)
dict_2 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}
print(dict_2)
dict_3 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}
print(dict_3)

# 找出三个字典中的公共键,s是类元组的对象(不是元组的子类)，支持元组交集操作，访问其中的元素需要转变为list
s = dict_1.viewkeys() & dict_2.viewkeys() & dict_3.viewkeys()
print s
print(isinstance(s, tuple))
s_list = list(s)
print s_list[0]


# map(function, iterable, ...)会根据提供的函数对指定序列做映射，function:函数 iterable:一个或多个序列
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
print(map(dict.viewkeys, [dict_1, dict_2, dict_3]))

# reduce(function, iterable[, initializer]) 函数会对参数序列中元素进行累积。
# function -- 函数，有两个参数 iterable -- 可迭代对象（如列表） initializer -- 可选，初始参数
print(reduce(lambda a, b: a & b, map(dict.viewkeys, [dict_1, dict_2, dict_3])))
