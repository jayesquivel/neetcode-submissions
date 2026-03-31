class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxVal = 0
        for val in nums:
            if val == 0:
                maxVal = max(maxVal, count)
                count = 0
            else:
                count += 1
        
        return max(count, maxVal)
        