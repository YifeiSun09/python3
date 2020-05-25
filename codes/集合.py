#coding:utf8

from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p1 = Point(1,1)
p2 = Point(1,1)

print(p1 == p2)
print(p1.x,p1.y)