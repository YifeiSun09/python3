#coding:utf8

class Student:
    __slots__ = ('name','age','_idx')
    def __init__(self):
        self.name = 'Francis'
        self.age = 25
        self._idx = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self._idx += 1
        if self._idx > 2:
            raise StopIteration()
        elif self._idx == 1:
            return self.name
        elif self._idx == 2:
            return self.age
        return '0'
    
student = Student()
for i in student:
    print(i)