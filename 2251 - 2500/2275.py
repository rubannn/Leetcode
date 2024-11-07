class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        n = 24
        bits = [0] * n
        for el in candidates:
            b = list(map(int, f"{el:0{n}b}"))
            for i in range(n):
                bits[i] += b[i]
        mx = 0
        for i in range(n):
            if bits[mx] < bits[i]:
                mx = i
        return bits[mx]
