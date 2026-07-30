# 1009. Complement of Base 10 Integer
# Difficulty: Easy
# Link: https://leetcode.com/problems/complement-of-base-10-integer/
#
# Problem:
# The complement of an integer is the integer you get when you flip all the 0's to 1's
# and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer n, return its complement.
#
# Approach: Bitwise XOR with a Mask
# - If n is 0, its complement is 1.
# - Otherwise, find the bit length of n.
# - Create a mask of 1s of the same bit length: mask = (1 << n.bit_length()) - 1.
# - The complement is n XOR mask (n ^ mask).
#
# Time Complexity:  O(1)
# Space Complexity: O(1)

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        mask = (1 << n.bit_length()) - 1
        return n ^ mask
