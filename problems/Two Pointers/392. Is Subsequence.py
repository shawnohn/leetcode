# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
# Difficulty: Easy
# Tag: Two Pointers

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub = 0
        n = len(s)
        if n == 0:
            return True
        for i in range(len(t)):
            if s[sub] == t[i]:
                sub += 1
                if sub == n:
                    return True
        return False


# Solution
# O(n) time | O(1) space. Iterate through the string t and check if the character is the same as the current character in s.
# If it is, increment the index of s. If the index of s is equal to the length of s which means we have found all the characters in s in t, return True.
# If we have iterated through the string t, it means s is not a subsequence of t, return False.
