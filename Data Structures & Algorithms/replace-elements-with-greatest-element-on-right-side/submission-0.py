class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxR = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(maxR, arr[i])
            arr[i] = maxR
            maxR = newMax
        return arr