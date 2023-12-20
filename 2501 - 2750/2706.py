class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        sm = prices[0] + prices[1]
        return (money - sm) if sm <= money else money
