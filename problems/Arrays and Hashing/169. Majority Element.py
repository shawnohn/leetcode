# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
# Difficulty: Easy
# Tag: Array, Hash Table, Divide and Conquer, Sorting, Counting

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        n = n // 2
        for key, value in m.items():
            if value > n:
                return key

        return 0
