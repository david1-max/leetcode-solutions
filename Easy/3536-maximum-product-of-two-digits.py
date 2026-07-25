# 3536. Maximum Product of Two Digits
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-product-of-two-digits/
#
# Problem:
# Given an integer n, find the maximum product of two digits in the number.
#
# Approach:
# - Convert the number n to string to get digits.
# - Find the maximum digit, remove it from the list of digits, and find the next maximum.
# - Return the product of these two maximum digits.
#
# Time Complexity:  O(D) — where D is the number of digits in n
# Space Complexity: O(D)

class Solution:
    def maxProduct(self, n: int) -> int:
        s = str(n)
        l = list(s)
        mx1 = max(l)
        l.remove(mx1)
        mx2 = max(l)
        return int(mx1) * int(mx2)
