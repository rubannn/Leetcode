class Solution:
    # variant 1
    def getRow(self, rowIndex: int) -> List[int]:
        tr = [[1]]
        for _ in range(rowIndex):
            last = [1]
            for k in range(len(tr[-1])-1):
                last += [tr[-1][k] + tr[-1][k+1]]
            tr.append(last + [1])
        return tr[-1]

    # variant 2
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            last = [1]
            for k in range(len(row)-1):
                last += [row[k] + row[k+1]]
            row = last + [1]
        return row
