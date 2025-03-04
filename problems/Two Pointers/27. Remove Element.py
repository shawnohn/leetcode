# https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array
# Difficulty: Easy
# tag: Array, Two Pointers

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1
        return pointer


# Solution
# O(n) time and O(1) space. Two pointers for reading and writing.
# While iterating the array to find out the target value, use writing pointer to memo and override the non-equal value in the array
