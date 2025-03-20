# https://leetcode.com/problems/longest-consecutive-sequence/description/
# difficulty: normal
# tag: Array, Hash Table, Union Find

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hashSet = set(nums)
        longestSeq = 0

        for num in hashSet:
            if (num - 1) not in hashSet:
                curSeq = 1
                while (num + 1) in hashSet:
                    num += 1
                    curSeq += 1
                longestSeq = max(curSeq, longestSeq)

        return longestSeq


# Solution
# O(n) time and space when building a set from nums takes O(n) time and space.
# Iterate over the set and start searching consequence numbers only when the element is the start number of the sequence.
