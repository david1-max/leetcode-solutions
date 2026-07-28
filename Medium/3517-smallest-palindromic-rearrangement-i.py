# 3517. Smallest Palindromic Rearrangement I
# Difficulty: Medium
# Link: https://leetcode.com/problems/smallest-palindromic-rearrangement-i/
#
# Problem:
# Given a string s that is guaranteed to be a palindrome, return the
# lexicographically smallest palindromic permutation of that string.
#
# Approach: Half-String Sorting (Greedy)
# - Since s is already a palindrome:
#     1. The first half `s[:n // 2]` contains exactly one copy of every symmetric pair.
#     2. The middle character `s[n // 2]` (if length is odd) is the single odd-frequency character.
# - To make the palindrome lexicographically smallest:
#     - Count the frequencies of the characters in the first half.
#     - Construct the sorted first half in alphabetical order (`half`).
#     - Concatenate `half + mid + reversed(half)`.
#
# Time Complexity:  O(n)  — single pass to count the first half
# Space Complexity: O(k)  — where k is the size of alphabet (26)

from collections import Counter
from string import ascii_lowercase

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        freq = Counter(s[:n >> 1])
        
        half = "".join(c * freq[c] for c in ascii_lowercase)
        mid = s[n >> 1] if n & 1 else ""
        
        return half + mid + half[::-1]
