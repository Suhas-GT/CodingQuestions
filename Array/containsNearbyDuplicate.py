# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Example 1:    
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen={}
        for i,num in enumerate(nums):
            if num in seen and i-seen[num] <= k:
                return True
            seen[num]=i
        return False

s= Solution()
print(s.containsNearbyDuplicate([1,2,3,1],3))
print(s.containsNearbyDuplicate([1,0,1,1],1))
print(s.containsNearbyDuplicate([1,2,3,1,2,3],2))