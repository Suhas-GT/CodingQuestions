# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/   

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if (len(nums) > len(set(nums))) else False
    
s=Solution()
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))