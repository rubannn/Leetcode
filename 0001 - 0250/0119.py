class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tr = [[1]]
        for _ in range(rowIndex):
            last = [1]
            for k in range(len(tr[-1])-1):
                last += [tr[-1][k] + tr[-1][k+1]]
            tr.append(last + [1])
        return tr[-1]
