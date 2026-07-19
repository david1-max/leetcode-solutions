# 349. Intersection of Two Arrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/intersection-of-two-arrays/
#
# Problem:
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique, and the result can be in any order.
#
# Note: This differs from #350 (Intersection of Two Arrays II) where duplicates
# are counted. Here, each element appears at most once in the result.
#
# Approach: Set Intersection
# - Convert both arrays to sets (automatically removes duplicates).
# - Use the & operator to find the common elements between both sets.
# - Return the result as a list.
#
# Time Complexity:  O(m + n)  — building two sets and computing intersection
# Space Complexity: O(m + n)  — storing both sets

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        l = s1 & s2
        return list(l)
