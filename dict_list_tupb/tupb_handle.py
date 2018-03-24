#coding=utf-8


from collections import namedtuple


# 学生姓名、年龄、性别
student = ('jim', 16, 'male', '123465@126.com')

NAME, AGE, SEX, EMAIL = xrange(4)

print student[NAME]
print student[SEX]
print student[SEX]
print student[EMAIL]


student = namedtuple('student', ['name', 'age', 'sex', 'email'])

s = student('jim', 16, 'male', '123465@126.com')
print s
print s.age
s2 = student(name='tom', age=18, sex='male', email='123654@126.com')
print s2
print s2.age

# 是不是元组的一个子类
print isinstance(s, tuple)