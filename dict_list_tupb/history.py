#coding=utf-8

# 猜数字程序，保存猜数字的历史记录（猜过哪些数字）


from random import randint
from collections import deque
import pickle


number = randint(0,100)
# 创建一个双端队列
q = deque([], 5)

def guess(value):
    if value == number:
        print 'right!'
        return True

    if value > number:
        print '%s is greater-than number'%value
    else:
        print '%s is less-than number' % value

    return False

try:
    q = pickle.load(open('history'))
except:
    pass


while True:
    str = raw_input('please input a number : ')
    if str.isdigit():
        value = int(str)
        q.append(value)
        if guess(value):
            break
    else:
        if "history" == str or "h?" == str:
            print(list(q))


print(q)
pickle.dump(q, open('history', 'w'))
print "*" * 20
q2 = pickle.load(open('history'))
print(q2)
