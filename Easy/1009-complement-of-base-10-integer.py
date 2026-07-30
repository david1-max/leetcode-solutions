# 1009. Complement of Base 10 Integer
# Difficulty: Easy
# Link: https://leetcode.com/problems/complement-of-base-10-integer/
#
# Problem:
# The complement of an integer is the integer you get when you flip all the 0's to 1's
# and all the 1's to 0's in its binary representation. Given an integer n, return its complement.
#
# Approach: Binary String Parsing
# - Convert n to its binary string representation using bin(n) and strip the '0b' prefix.
# - Iterate through the binary string, flipping '0' to '1' and '1' to '0'.
# - Reverse the flipped binary string.
# - Convert the reversed string back to decimal by accumulating powers of 2.
#
# Time Complexity:  O(log n)  — binary representation length is log2(n)
# Space Complexity: O(log n)  — storing string representations of binary length

from typing import List

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)
        b = b[2:]
        s = ''
        for i in b:
            if i == '0':
                s += str(1)
            else:
                s += str(0)
        s = s[::-1]
        r = 0
        for i in range(len(s)):
            r += (2 ** (i)) * int(s[i])
        return r
