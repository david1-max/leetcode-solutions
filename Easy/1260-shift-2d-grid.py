# 1260. Shift 2D Grid
# Difficulty: Easy
# Link: https://leetcode.com/problems/shift-2d-grid/
#
# Problem:
# Given a 2D grid and an integer k, shift the grid k times.
# In one shift: every element moves one step to the right,
# the last element of each row moves to the first position of the next row,
# and the last element of the grid wraps to the first position of the grid.
# Return the modified grid after k shifts.
#
# Approach: Flatten + Reverse Rotation Algorithm
# - Flatten the 2D grid into a 1D array `temp`.
# - Reduce k using modulo to avoid redundant full rotations: k %= size.
# - Apply the classic 3-step reverse rotation to right-shift by k:
#     1. Reverse the entire array.
#     2. Reverse the first k elements.
#     3. Reverse the remaining elements.
#   This achieves a right rotation of k positions in O(n) time.
# - Reconstruct the 2D grid from the rotated 1D array row by row.
#
# Time Complexity:  O(n * m)  — flattening + reversals + reconstruction
# Space Complexity: O(n * m)  — storing the flattened temp array

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        temp = []

        # Flatten the grid
        for i in range(n):
            for j in range(m):
                temp.append(grid[i][j])

        size = len(temp)
        k %= size

        # 3-step reverse rotation (right shift by k)
        temp1 = temp[::-1]
        t1 = temp1[:k]
        t2 = temp1[k:]
        t1 = t1[::-1]
        t2 = t2[::-1]
        t = t1 + t2

        # Reconstruct the 2D grid
        ans = []
        x = 0
        for i in range(n):
            c = []
            for j in range(m):
                c.append(t[x])
                x += 1
            ans.append(c)
        return ans
