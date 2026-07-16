# 20. Valid Parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-parentheses/
#
# Problem:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
#
# Approach: Stack Data Structure
# - Use a stack to store opening brackets.
# - For each character in the string, if it's an opening bracket, push it onto the stack.
# - If it's a closing bracket, verify that the stack is not empty and matches the
#   corresponding opening bracket at the top of the stack. If so, pop it.
# - Otherwise, the string is invalid.
# - At the end, the stack should be empty for a valid string.
#
# Time Complexity:  O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0
