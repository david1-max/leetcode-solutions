# 3867. Sum of GCD of Formed Pairs
# Difficulty: Medium
# Link: https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/
#
# Problem:
# Given a list of integers nums, calculate the prefix GCDs (using the running maximum
# of the prefix and each element), sort them, and return the sum of the GCDs of pairs
# formed by matching the smallest and largest remaining elements.
#
# Approach:
# 1. Maintain a running maximum (`mx`) of the array.
# 2. Compute prefix GCDs as `GCD(mx, nums[i])` and store them in a list.
# 3. Sort the prefix GCD list.
# 4. Form pairs using a two-pointer approach (pairing element at index `i` with `l-i-1`).
# 5. Compute the GCD of each pair and return the accumulated sum.
#
# Time Complexity:  O(n log n + n log(max_val))
# Space Complexity: O(n)

import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixgcd = []
        mx = nums[0]
        for i in range(len(nums)):
            if mx < nums[i]:
                mx = nums[i]
            prefixgcd.append(math.gcd(mx, nums[i]))
        prefixgcd.sort()

        s = 0
        l = len(prefixgcd)
        for i in range(l // 2):
            s += math.gcd(prefixgcd[i], prefixgcd[l - i - 1])
        return s
