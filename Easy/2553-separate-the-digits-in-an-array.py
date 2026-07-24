# 2553. Separate the Digits in an Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/separate-the-digits-in-an-array/
#
# Problem:
# Given an array of positive integers nums, return an array ans that consists
# of the digits of each integer in nums after separating them in the same order
# they appear in nums.
#
# Approach:
# - Iterate through each number in the array.
# - Convert each number to its string representation to access its individual digits.
# - Convert each character digit back to an integer and append it to the result list.
#
# Time Complexity:  O(N * D) — where N is the number of elements and D is the average number of digits per element.
# Space Complexity: O(1)     — auxiliary space (excluding the output array).

from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            k = str(i)
            for j in k:
                ans.append(int(j))
        return ans
