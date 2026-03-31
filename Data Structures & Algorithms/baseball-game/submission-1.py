class Solution:
    def calPoints(self, operations: List[str]) -> int:
        newRecord = []
        for i in operations:
            if i == "+":
                newRecord.append(newRecord[-1] + newRecord[-2])
            elif i == "D":
                newRecord.append(2 * newRecord[-1])
            elif i == "C":
                newRecord.pop()
            else:
                newRecord.append(int(i))
        return sum(newRecord)
                
        