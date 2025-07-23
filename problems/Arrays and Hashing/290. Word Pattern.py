# https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150
# Difficulty: Easy
# Tag: String

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_to_w_map = {}
        w_to_p_map = {}
        list_s = s.split()
        if len(pattern) != len(list_s):
            return False

        for p_char, word in zip(pattern, list_s):
            if p_char in p_to_w_map and p_to_w_map[p_char] != word:
                return False
            if word in w_to_p_map and w_to_p_map[word] != p_char:
                return False

            p_to_w_map[p_char] = word
            w_to_p_map[word] = p_char

        return True


# Solution
# O(n) time | O(n) space. Iterate through the pattern and the string and use two maps to track character and word mappings.
# To make sure the mapping is one-to-one, we need to check mapping in both directions.
