# 3658. GCD of Odd and Even Sums
# Difficulty: Easy
# Link: https://leetcode.com/problems/gcd-of-odd-and-even-sums/
#
# Problem:
# Given an integer n, calculate the sum of the first n odd numbers
# and the sum of the first n even numbers, then return their greatest common divisor (GCD).
#
# Mathematical Insight:
# - Sum of first n odd numbers = n^2
# - Sum of first n even numbers = n * (n + 1)
# - GCD(n^2, n(n+1)) = n * GCD(n, n+1) = n * 1 = n
# (Since consecutive integers are coprime, GCD(n, n+1) is always 1)
#
# Time Complexity:  O(log(min(odsm, evnsm))) due to Euclidean algorithm for GCD
# Space Complexity: O(1)

import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odsm = n * n
        evnsm = n * (n + 1)
        return math.gcd(odsm, evnsm)
