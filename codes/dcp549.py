# coding:utf8
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

# Do this in O(N) time and O(1) space.
# 在一个列表中,除了一个数字出现一次外,其他数字都出现过3次,请找出这个出现一次的数字.  

class Solution:
    def __init__(self,arr):
        self.arr = arr
    
    def result(self):
        if not isinstance(self.arr,list): # 传入的必须数列表
            return None
        res = [0] * 32 # 结果
        for i in self.arr:
            for j in range(32):
                res[j] += (1 if (i & (1<<j)) > 0 else 0) # 遍历数字中的所有位数
        
        ans = 0
        for idx,val in enumerate(res):
            ans |= (val % 3) << idx
        return ans

print(Solution([13, 19, 13, 13]).result())