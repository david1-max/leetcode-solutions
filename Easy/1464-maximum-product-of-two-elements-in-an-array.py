# 1464. Maximum Product of Two Elements in an Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
#
# Problem:
# Given the array of integers nums, you will choose two different indices i and j
# of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
#
# Approach: Tracking Max/Min Candidates
# - If the length of the array is 2, return the product directly.
# - Find and remove the largest element to identify the second largest.
# - Find and remove the smallest element to identify the second smallest
#   (to account for potential negative values, though LeetCode constraints specify nums[i] >= 1).
# - Return the maximum of the two candidate products.
#
# Time Complexity:  O(n)  — multiple linear scans (max, min, remove)
# Space Complexity: O(1)  — modified in-place

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return ((nums[0] - 1) * (nums[1] - 1))
        
        mx = max(nums)
        nums.remove(mx)
        mx2 = max(nums)
        mn = min(nums)
        nums.remove(mn)
        mn2 = min(nums)
        return max((mx - 1) * (mx2 - 1), (mn - 1) * (mn2 - 1))
