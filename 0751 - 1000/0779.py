class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        st_len = 2 ** (n-1)
        polindrom = False
        while st_len > 1:
            if k > st_len // 2:
                k -= st_len // 2
                polindrom = not polindrom
            st_len //= 2
        return int(polindrom)
