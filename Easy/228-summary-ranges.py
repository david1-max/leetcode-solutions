# 228. Summary Ranges
# Difficulty: Easy
# Link: https://leetcode.com/problems/summary-ranges/
#
# Problem:
# Given a sorted unique integer array nums, return the smallest sorted list of
# ranges that cover all the numbers in the array exactly. A range [a, b] is
# represented as "a->b" if a != b, and "a" if a == b.
#
# Approach: Linear Scan with Range Tracking
# - Handle the empty array edge case upfront.
# - Track the start of the current range using `s` (as a string).
# - Iterate through adjacent pairs:
#     - If the gap between nums[i+1] and nums[i] is more than 1, the current
#       range ends at nums[i].
#       - If start == end (single element range), append just `s`.
#       - Otherwise, append "s->nums[i]".
#     - Reset `s` to the next element to start a new range.
# - After the loop, handle the final range using nums[-1].
#
# Time Complexity:  O(n)  — single pass through the array
# Space Complexity: O(1)  — excluding the output list

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        s = str(nums[0])
        l = []
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                if s == str(nums[i]):
                    l.append(s)
                else:
                    l.append(s + '->' + str(nums[i]))
                s = str(nums[i + 1])
        if s == str(nums[-1]):
            l.append(s)
        else:
            l.append(s + '->' + str(nums[-1]))
        return l
