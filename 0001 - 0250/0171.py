class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        sol = 0
        for i in range(len(columnTitle)):
            sol += (26 ** i)*(ord(columnTitle[i]) - ord('A') + 1)
        return sol
