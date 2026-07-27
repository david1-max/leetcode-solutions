# 628. Maximum Product of Three Numbers
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
#
# Problem:
# Given an integer array nums, find three numbers whose product is maximum
# and return the maximum product.
#
# Approach: Sorting / Candidate Selection
# - Sort the array in ascending order.
# - The maximum product of three numbers can come from either:
#     1. The three largest positive numbers: nums[-1] * nums[-2] * nums[-3]
#     2. Two large negative numbers (which become positive when multiplied)
#        and the largest positive number: nums[-1] * nums[0] * nums[1]
# - Return the maximum of these two candidate products.
#
# Time Complexity:  O(n log n)  — sorting the array
# Space Complexity: O(1)        — sorted in-place (excluding sorting recursion stack)

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])
