class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_even = n // 2
        n_odd = n - n_even
        m_even = m // 2
        m_odd = m - m_even
        return n_even * m_odd + n_odd * m_even

    def flowerGame2(self, n: int, m: int) -> int:
        return n * m // 2
