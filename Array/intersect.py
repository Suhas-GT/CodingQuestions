# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
        return res

s= Solution()
l1=[1,2,2,1]
l2=[2,2]
print(s.intersect(l1,l2))
l1=[4,9,5]
l2=[9,4,9,8,4]
print(s.intersect(l1,l2))
