# 35. Search Insert Position
# Difficulty: Easy
# Link: https://leetcode.com/problems/search-insert-position/
#
# Problem:
# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index
# where it would be if it were inserted in order.
#
# Approach: Linear Scan
# - If target is greater than the last element, return len(nums)
# - Otherwise scan through nums and return the first index
#   where nums[i] >= target
# Time Complexity:  O(n)
# Space Complexity: O(1)

class Solution(object):
    def searchInsert(self, nums, target):
        j = 0
        if target > nums[-1]:
            return len(nums)
        for i in nums:
            if i >= target:
                return j
            else:
                j += 1

# ----------------------------
# Test Cases
# ----------------------------
# Input: nums = [1,3,5,6], target = 5  → Output: 2
# Input: nums = [1,3,5,6], target = 2  → Output: 1
# Input: nums = [1,3,5,6], target = 7  → Output: 4
