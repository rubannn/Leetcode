class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = list(map(int, s))
        n = len(arr)
        for a in range(1, n - 1):
            for b in range(1, n - a + 1):
                arr[b - 1] = (arr[b - 1] + arr[b]) % 10
        return arr[0] == arr[1]
