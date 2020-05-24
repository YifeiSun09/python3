#coding:utf8
class Student:
    __slots__ = ('name','age') # 设定允许的参数

    def __init__(self):
        pass

student = Student()
student.name = '1234'
student.age = 25
print(student)