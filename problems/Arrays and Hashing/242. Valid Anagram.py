# https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150
# Difficulty: Easy
# Tag: String

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1

        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        return s_map == t_map


# Solution
# O(n) time | O(n) space. Iterate through each string and map the frequency of each character.
# If the two maps are same, the strings are anagram.
