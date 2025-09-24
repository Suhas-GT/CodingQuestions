# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        s2 = set(nums2)
        s3=[]
        for i in s1:
            if i in s2:
                s3.append(i)
        return s3
    
s= Solution()
l1=[1,2,2,1]
l2=[2,2]
print(s.intersection(l1,l2))
l1=[4,9,5]
l2=[9,4,9,8,4]
print(s.intersection(l1,l2))