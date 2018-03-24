#coding=utf-8

# 使用reversed生成反向可迭代对象


class FloatRange(object):
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t < self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t > self.start:
            yield t
            t -= self.step


for i in FloatRange(1.0, 5.0, 0.5):
    print i

print '*' * 20

for i in reversed(FloatRange(1.0, 5.0, 0.5)):
    print i
