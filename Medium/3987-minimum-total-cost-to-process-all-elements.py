# 3987. Minimum Total Cost to Process All Elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/
#
# Problem:
# Given an integer array nums and an integer k, process all elements greedily.
# You start with a remaining budget `rsr = k`. For each element:
#   - If nums[i] <= rsr, subtract it from rsr at zero extra cost.
#   - Otherwise, you must buy additional capacity in increments of k.
#     The cost to buy c units of extra capacity is a triangular number:
#     cost = (c * (c + 1)) // 2 + c * (previous total operations)
# Return the total cost modulo 10^9 + 7.
#
# Approach: Greedy + Triangular Number Cost Formula
# - Track remaining budget `rsr` across the array.
# - For each element that exceeds `rsr`, calculate the minimum number of
#   k-capacity blocks `c` needed to cover the deficit.
# - Apply the triangular cost formula: (c*(c+1))//2 + c * op
#   where `op` is the cumulative number of capacity purchases so far.
# - Accumulate total cost and update `op` and `rsr` accordingly.
# - Return total cost mod (10^9 + 7).
#
# Time Complexity:  O(n)
# Space Complexity: O(1)

class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        ttlcst = 0
        c = 0
        cc = 0
        op = 0
        rsr = k
        for i in range(len(nums)):
            if nums[i] <= rsr:
                rsr -= nums[i]
            else:
                rrsr = (nums[i] - rsr)
                if rrsr % k == 0:
                    c = rrsr // k
                    cc = (c * (c + 1)) // 2 + c * op
                    rsr = rsr + k * c - nums[i]
                else:
                    c = rrsr // k + 1
                    cc = (c * (c + 1)) // 2 + c * op
                    rsr = rsr + k * c - nums[i]
                op += c
                ttlcst += cc
        return ttlcst % (10 ** 9 + 7)
