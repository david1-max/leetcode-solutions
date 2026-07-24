# 3754. Concatenate Non-Zero Digits and Multiply by Sum I
# Difficulty: Easy
# Link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
#
# Problem:
# Given an integer n, concatenate all its non-zero digits to form a new integer,
# and multiply this new integer by the sum of its non-zero digits.
#
# Approach:
# - Convert n to string to iterate over digits.
# - Accumulate sum of non-zero digits and build concatenated string of non-zero digits.
# - Return the product of the concatenated integer and the sum.
#
# Time Complexity:  O(D) — where D is the number of digits in n
# Space Complexity: O(D)

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        st = str(n)
        ns = ''
        s = 0
        if n == 0:
            return 0
        for i in st:
            if i == '0':
                s += 0
                continue
            else:
                ns += i
                s += int(i)
        return int(ns) * s
