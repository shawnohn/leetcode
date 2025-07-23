# https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
# Difficulty: Easy
# Tag: String

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t_map = {}
        t_to_s_map = {}

        for s_char, t_char in zip(s, t):
            if s_char in s_to_t_map and s_to_t_map[s_char] != t_char:
                return False
            if t_char in t_to_s_map and t_to_s_map[t_char] != s_char:
                return False

            s_to_t_map[s_char] = t_char
            t_to_s_map[t_char] = s_char

        return True


# Solution
# O(n) time | O(n) space. Iterate through the strings and use two maps to track character mappings.
# To make sure the mapping is one-to-one, we need to use another map to track the reverse mapping.
