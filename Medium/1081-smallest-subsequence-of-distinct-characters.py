# 1081. Smallest Subsequence of Distinct Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
#
# Problem:
# Return the lexicographically smallest subsequence of the string s such that
# every distinct character appears exactly once.
#
# Approach: Monotonic Stack + Greedy
# - Use a frequency Counter to track remaining occurrences of each character.
# - Use a `seen` set to track which characters are already in the stack.
# - Iterate over each character:
#     1. Decrement its remaining frequency.
#     2. Skip if already in the result stack (seen).
#     3. While the stack's top character is GREATER than the current character
#        AND the top character still appears later (freq > 0), pop it from the
#        stack (we can add it later in a better position).
#     4. Push the current character onto the stack and mark as seen.
# - The result is the lexicographically smallest subsequence with all unique chars.
#
# Time Complexity:  O(n)  — each character is pushed and popped at most once
# Space Complexity: O(k)  — where k is the number of distinct characters (≤ 26)

from collections import Counter

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        seen = set()
        stack = []

        for c in s:
            freq[c] -= 1
            if c in seen:
                continue

            while stack and stack[-1] > c and freq[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)
