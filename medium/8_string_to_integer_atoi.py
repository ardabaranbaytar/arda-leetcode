# LeetCode 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/
# Difficulty: Medium
# Tags: String
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Check sign
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        # Step 3: Convert digits
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # Step 4: Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
