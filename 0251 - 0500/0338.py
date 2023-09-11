class Solution:
    def countBits(self, n: int) -> List[int]:
        return [f'{x:b}'.count('1') for x in range(n+1)]
