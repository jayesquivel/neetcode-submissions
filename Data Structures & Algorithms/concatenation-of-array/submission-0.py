class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Make empty array
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans