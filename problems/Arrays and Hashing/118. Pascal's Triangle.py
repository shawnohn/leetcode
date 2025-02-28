from typing import List

# https://leetcode.com/problems/pascals-triangle/description/
# Difficulty: Easy

# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(numRows):
            if i == 0:
                continue

            newRow = []
            prevRow = result[i - 1]
            for j in range(i + 1):
                if j == 0 or j == i:
                    newRow.append(1)
                else:
                    newRow.append(prevRow[j - 1] + prevRow[j])
            result.append(newRow)

        return result


# Solution
# O(n^2) time and O(1) aux space. We have to iterate the prev row and create the new row over n rows of length n.
