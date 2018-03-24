#coding=utf-8

# 生成器对象
# 用生成器创建一个可迭代的对象，每次yield返回一个素数


class generator(object):
    def __init__(self, start, end):
        if start > 0:
            self.start = start
        else:
            self.start = 1
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False
        # xrange生成2至k-1
        for i in xrange(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for i in xrange(self.start, self.end+1):
            if self.isPrimeNum(i):
                yield i


for i in generator(1, 100):
    print i