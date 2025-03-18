# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
# difficulty: easy
# tag: Hash Table, String, Counting

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        char_counts = {}

        for char in magazine:
            char_counts[char] = char_counts.get(char, 0) + 1

        for char in ransomNote:
            if char not in char_counts or char_counts[char] == 0:
                return False
            char_counts[char] -= 1

        return True


# Solution
# O(m + n) time and O(k) where k is the number of unique characters. Build hash table to count the number of unique chars.
# Iterate over ransomNote and use the map to determine magazine has the enough number of chars.


if __name__ == "__main__":
    solution = Solution()

    ransomNote = "aa"
    magazine = "ab"
    # Test cases
    print("Test case 1:", solution.canConstruct(ransomNote, magazine))
