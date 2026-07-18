# 1979. Find Greatest Common Divisor of Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/
#
# Problem:
# Given an integer array nums, return the greatest common divisor of the smallest number
# and the largest number in nums.
#
# Approach:
# - Find the maximum value in the array.
# - Find the minimum value in the array.
# - Compute and return their Greatest Common Divisor (GCD) using math.gcd.
#
# Time Complexity:  O(n)
# Space Complexity: O(1)

import math
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)
        return math.gcd(mx, mn)
