# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# difficulty: normal
# tag: Array, Binary Search, Sliding Window, Prefix Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


import sys
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = sys.maxsize
        left = 0
        right = 0
        prefixSum = 0

        while right < len(nums):
            prefixSum += nums[right]
            while prefixSum >= target:
                minLength = min(minLength, right - left + 1)
                prefixSum -= nums[left]
                left += 1
            right += 1

        return 0 if minLength == sys.maxsize else minLength


# Solution
# O(n) time and O(1) space. Use two pointers to keep the sliding window of sum while iterate down nums.
# Once the sum greater then targe, try to reduce the size of sliding window until the sum is still greater or equal.

solution = Solution()

target = 10
nums = [1, 5, 5, 10, 20]

print(solution.minSubArrayLen(target, nums))
