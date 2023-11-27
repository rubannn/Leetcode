class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        have_stock = -prices[0]
        no_stock = 0
        for i in range(1, n):
            no_stock = max(no_stock, have_stock + prices[i] - fee)
            have_stock = max(have_stock, no_stock - prices[i])
        return no_stock
