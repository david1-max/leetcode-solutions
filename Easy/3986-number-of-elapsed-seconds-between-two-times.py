# 3986. Number of Elapsed Seconds Between Two Times
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/
#
# Problem:
# Given two strings startTime and endTime, both in the format "HH:MM:SS",
# return the number of seconds elapsed from startTime to endTime.
#
# Approach:
# - Split each time string by ":" to extract hours, minutes, and seconds.
# - Convert startTime to total seconds: hours * 3600 + minutes * 60 + seconds.
# - Convert endTime to total seconds the same way.
# - Return the difference (endTime seconds - startTime seconds).
#
# Time Complexity:  O(1)  — fixed-length string parsing, no loops over input size
# Space Complexity: O(1)

class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        lst = startTime.split(":")
        nlst = endTime.split(":")
        ttltimeofst = int(lst[0]) * 3600 + int(lst[1]) * 60 + int(lst[2])
        ttltimeofed = int(nlst[0]) * 3600 + int(nlst[1]) * 60 + int(nlst[2])
        return ttltimeofed - ttltimeofst
