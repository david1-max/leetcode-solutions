# 1351. Count Negative Numbers in a Sorted Matrix
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
#
# Problem:
# Given a m x n matrix grid which is sorted in non-increasing order both
# row-wise and column-wise, return the number of negative numbers in grid.
#
# Approach: Staircase / Binary Search (O(m + n) Time)
# - Start from the bottom-left corner of the matrix: row = m-1, col = 0.
# - If the current element is negative, then all elements to its right in the same row
#   are also negative (since rows are sorted in non-increasing order).
#   We add the count of remaining elements in this row (clen - col) to our count, and move up (row -= 1).
# - If the current element is non-negative, then all elements above it in the same column
#   are also non-negative. We move right (col += 1).
#
# Time Complexity:  O(m + n)
# Space Complexity: O(1)

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        rlen = len(grid)
        clen = len(grid[0])

        i = rlen - 1
        j = 0
        c = 0
        while i >= 0 and j < clen:
            if grid[i][j] < 0:
                c += clen - j
                i -= 1
            else:
                j += 1
        return c
