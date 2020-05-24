#coding:utf8
# 文档测试
def fact(n):
    '''
    测试阶乘

    >>> fact(1)
    1
    >>> fact(0)
    1
    >>> fact(4)
    24
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError
    '''
    if n < 0:
        raise ValueError()
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()