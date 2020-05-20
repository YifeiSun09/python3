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
S.sort(reverse = True) # 逆序排列
def sumto(S,total):
    for idx,val in enumerate(S):
        if val == total:
            return True
        return sumto(S[idx+1:],total) or sumto(S[idx+1:],total - val)
    return False

print(S,24)