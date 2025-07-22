# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150
# Difficulty: Easy
# Tag: String

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Start from the end and skip trailing spaces
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        # Count the length of the last word
        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
