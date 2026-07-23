# 196. Delete Duplicate Emails
# Difficulty: Easy
# Link: https://leetcode.com/problems/delete-duplicate-emails/
#
# Problem:
# Write a SQL query to delete all duplicate email entries in a table named Person,
# keeping only unique emails based on its smallest Id.
#
# Approach:
# - Self-join the Person table on the email column.
# - Delete rows from the first table instance (p1) where the ID is greater than
#   the ID in the second table instance (p2) for the same email.
# - This keeps only the row with the minimum ID for each duplicate email.
#
# Time Complexity:  O(n^2) - due to self-join comparison of all pairs of rows
# Space Complexity: O(n)

# Write your MySQL query statement below
DELETE p1 FROM Person p1, Person p2
WHERE p1.email = p2.email AND p1.id > p2.id;
