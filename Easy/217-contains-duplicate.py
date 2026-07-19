# 217. Contains Duplicate
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate/
#
# Problem:
# Given an integer array nums, return True if any value appears at least twice
# in the array, and return False if every element is distinct.
#
# Approach: Set Conversion
# - Convert the array to a set (which removes all duplicates).
# - If the length of the set is less than the length of the original array,
#   it means at least one duplicate existed.
# - Return True if lengths differ, False if they are equal.
#
# Time Complexity:  O(n)  — building a set from n elements
# Space Complexity: O(n)  — storing up to n elements in the set

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(s) != len(nums)
