
# ** Case 1
# * Input: nums = [1,2,3,4]
# * Output: 3
# * Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

# ** Case 2
# * Input: nums = [1]
# * Output: 0

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        cnt = 1
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                result += cnt
                cnt += 1
            else:
                cnt = 1
        return result