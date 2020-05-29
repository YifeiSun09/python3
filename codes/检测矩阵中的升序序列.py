#coding:utf8
# 有一个n*m的矩阵,计算从上到下有序的列数

class Solution:
    '''
    测试

    >>> s = Solution()
    >>> s.solve(['abcd','bcde','dcba'])
    3
    >>> s.solve(['afcd','gdsa','csac'])
    0
    '''
    def solve(self,matrix):
        if matrix == []:
            return 0
        n = len(matrix) # n行
        m = len(matrix[0]) #m列
        cols = 0
        for i in range(n):
            last_inc = 0
            inc = 0
            for j in range(1,m):
                inc = -1 if matrix[i][j] > matrix[i][j-1] else 1
                if last_inc == 0:
                    last_inc = inc
                if last_inc != inc:
                    break
            if last_inc == inc:
                cols += 1
        return cols

if __name__ == '__main__':
    import doctest
    res = doctest.testmod()
    if res[0] == 0:
        print('测试成功')