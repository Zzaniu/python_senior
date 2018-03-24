#coding=utf-8

from random import randint
from collections import Counter


# 随机序列
data = [randint(0, 20) for _ in xrange(30)]
print(data)

# 已序列中的值作为键，0作为初始键值
dict_c = dict.fromkeys(data, 0)
print(dict_c)
# 统计序列中每个元素出现的次数
for x in data:
    dict_c[x] += 1

print(dict_c)

# 找到序列中出现次数最高的三个元素，只需对统计出来的字典进行排序即可，reverse=True为降序，默认为升序
print(sorted(dict_c.iteritems(), key=lambda x:x[1], reverse=True))

# 转化为一个Counter字典
dict_c2 = Counter(data)
print(dict_c[10])
print(dict_c2[10])
print(dict_c2)
# 出现频度最高的4个元素
print(dict_c2.most_common(4))

# 统计单词出现次数最多的方案：
# txt = open("xxx.txt").read()
# list_txt = re.split('\W+'，txt)
# c = Counter(list_txt)
# c.most_common(4)