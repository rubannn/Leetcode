class Solution:
    def rotatedDigits(self, n: int) -> int:
        dgts = {'0': '0', '1': '1', '2': '5', '3': '~', '4': '~',
                '5': '2', '6': '9', '7': '~', '8': '8', '9': '6'}
        k = 0
        for x in range(1, n+1):
            t = ''
            for c in str(x):
                t += dgts[c]
            if t.isnumeric() and int(t) != x:
                k += 1
        return k
