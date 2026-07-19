# 350. Intersection of Two Arrays II
# Difficulty: Easy
# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
#
# Problem:
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays,
# and the result can be in any order.
#
# Approach: Frequency HashMap (Counter)
# - Build a frequency dictionary d1 for nums1, counting occurrences of each number.
# - Build a frequency dictionary d2 for nums2, counting occurrences of each number.
# - For each key in d1 that also exists in d2, take the minimum count from both
#   dictionaries and add that many copies of the number to the result list.
#
# Time Complexity:  O(m + n)  — one pass each through nums1 and nums2
# Space Complexity: O(m + n)  — storing frequency maps for both arrays

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        d1 = {}
        for i in nums1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1

        d2 = {}
        for i in nums2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1

        for i in d1:
            if i in d2:
                m = min(d1[i], d2[i])
                for j in range(m):
                    l.append(i)
        return l
