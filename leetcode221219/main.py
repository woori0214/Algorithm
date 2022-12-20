
# ** Case 1
# * Input: nums = [1,2,1]
# * Output: [1,2,1,1,2,1]

# ** Case 2
# * Input: nums = [1,3,2,1]
# * Output: [1,3,2,1,1,3,2,1]

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(2):
            for j in nums:
                result.append(j)
        return result

