# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
# You must implement a solution with O(n) time complexity.

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=list(set(nums))
        n.sort(reverse=True)
        return n[2] if len(n)>2 else n[0]
    
s= Solution()
l=[3,2,1]
print(s.thirdMax(l))
l=[1,2]
print(s.thirdMax(l))
l=[2,2,3,1]
print(s.thirdMax(l))