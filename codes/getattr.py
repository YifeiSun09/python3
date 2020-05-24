#coding:utf8

class Student:
    def __init__(self):
        self.name = 'Michael'
    
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        elif attr == 'age':
            return 25
        elif attr == 'height':
            return 176
        return None

student = Student()

print(student.score)