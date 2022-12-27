# ** Case 1
# * Input: nums = 2
# * Output: 2
# * Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# ** Case 2
# * Input: nums = 3
# * Output: 3
# * Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        prevPrev = 1
        prev = 2
        current = 0

        for step in range(3, n + 1):
            current = prevPrev + prev
            prevPrev = prev
            prev = current
        return current