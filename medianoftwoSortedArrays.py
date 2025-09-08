# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()
        n=len(nums3)
        mid = n//2
        if n % 2 != 0:
            return nums3[mid]
        else:
            return (nums3[mid-1]+nums3[mid])/2.0

s=Solution()
print(s.findMedianSortedArrays([1,3],[2]))
print(s.findMedianSortedArrays([1,2],[3,4]))