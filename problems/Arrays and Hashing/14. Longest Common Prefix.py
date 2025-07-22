# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150
# Difficulty: Easy
# Tag: String

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for i in range(len(prefix)):
            for word in strs[1:]:
                if i == len(word) or word[i] != prefix[i]:
                    return prefix[0:i]

        return prefix


# Solution
# O(n) time | O(1) space. Based on the first string, iterate through the rest of the string.
# Check the string has the same character at the same index of the first string.
