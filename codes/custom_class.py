#coding:utf8

class Student:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

student = Student('Francis')
print(student)
