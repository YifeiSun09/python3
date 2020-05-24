#coding:utf8

class Student:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
    
student = Student('Francis')
student()