# https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
# Difficulty: Easy
# Tag: Math, Two Pointers, Hash Table

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.

# Return true if n is a happy number, and false if not.


class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = {}
        processed = n
        while processed != 1:
            digits = str(processed)
            if digits in numbers:
                return False
            val = 0
            for digit in digits:
                val += pow(int(digit), 2)
            numbers[digits] = val
            processed = val

        return True


# Solution
# O(1) time and space. Loop until the number is 1 or we meet a cycle.
# Use a hash table to track the numbers so we can find a cycle in constant time.
