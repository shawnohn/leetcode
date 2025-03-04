# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=problem-list-v2&envId=array
# Difficulty: Medium
# tag: Array, Binary Search

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left if left < len(nums) and nums[left] == target else -1

        def findLast(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right if right >= 0 and nums[right] == target else -1

        return [findFirst(nums, target), findLast(nums, target)]


# Solution
# O(log n) time complexity
# Key insight: Modify binary search to find extreme positions by:
# 1. For first position: When nums[mid] >= target, keep searching left half
#    This ensures we find the leftmost occurrence by including target in left search
# 2. For last position: When nums[mid] <= target, keep searching right half
#    This ensures we find the rightmost occurrence by including target in right search

nums = [5, 6, 7, 8, 9, 10]
target = 6

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange(nums, target))
