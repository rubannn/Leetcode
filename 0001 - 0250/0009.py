class Solution:
    # variant 1
    def isPalindrome(self, x: int) -> bool:
        return x >= 0 and x == int(str(x)[::-1])

    # variant 2
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            t = x
            n = 0
            while x > 0:
                n = n * 10 + x % 10
                x //= 10
            return n == t

    # variant 3
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x = str(x)
            i, n = 0, len(x)
            while i < n // 2 and x[i] == x[n - i - 1]:
                i += 1
            return x[i] == x[n - i - 1]
