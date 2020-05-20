#coding=utf8
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.
#
# Integers can appear more than once in the list. You may assume all numbers in the list are positive.
#
# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

S = [12,1,61,5,9,2]

def sumto(S,target):
    # 遍历列表
    for idx,val in enumerate(S):
        if val == target: # 判断当前值是否等于目标值,如果相同,返回当前值
            return [val]
        res = sumto(S[idx+1:],target) # 不包含当前元素的右侧子列表结果
        res2 = sumto(S[idx+1:],target - val) # 包含当前元素的的右侧子列表结果
        if not res2 is None: # 当当前元素被使用且有效时记录当前的元素,返回到上一级
            res = res2+[val]
        return res
    return None

print(sumto(S,24))