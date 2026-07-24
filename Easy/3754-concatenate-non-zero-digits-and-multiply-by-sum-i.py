# 3754. Concatenate Non-Zero Digits and Multiply by Sum I
# Difficulty: Easy
# Link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
#
# Problem:
# Given an integer n, concatenate all its non-zero digits to form a new integer,
# and multiply this new integer by the sum of its non-zero digits.
#
# Approach:
# - Extract digits of n mathematically using modulo and division.
# - Accumulate the sum of non-zero digits and build a reversed integer of non-zero digits.
# - Reverse the digit integer back to the original order.
# - Return the product of the concatenated integer and the sum.
#
# Time Complexity:  O(D) — where D is the number of digits in n
# Space Complexity: O(1) — constant auxiliary space

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = 0
        rr = 0
        while n > 0:
            if n % 10 == 0:
                s += 0
            else:
                s += n % 10
                rr = rr * 10 + n % 10
            n //= 10
        nrr = 0
        while rr > 0:
            nrr = nrr * 10 + rr % 10
            rr = rr // 10
        return nrr * s
