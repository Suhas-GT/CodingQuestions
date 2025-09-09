# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxi = 0 
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            maxi = max(maxi, h * w)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxi



s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))  
print(s.maxArea([1,1]))                
