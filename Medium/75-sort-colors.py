# 75. Sort Colors
# Difficulty: Medium
# Link: https://leetcode.com/problems/sort-colors/
#
# Problem:
# Given an array nums with n objects colored red, white, or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
#
# Approach: Built-in In-place Sort
# - Use the built-in nums.sort() to sort the array in-place.
#
# Note:
# LeetCode accepts this, but interviewers usually expect the Dutch National Flag algorithm
# (3-way partitioning using three pointers) to sort in O(n) time and O(1) space in a single pass.
#
# Time Complexity:  O(n log n)  — built-in Timsort
# Space Complexity: O(1)        — in-place sorting (excluding Timsort stack space which is O(n))

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()
        """
        Do not return anything, modify nums in-place instead.
        """
