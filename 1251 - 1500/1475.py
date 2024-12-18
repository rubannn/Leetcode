class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        for i in range(n - 1):
            j = i + 1
            while j + 1 < n and prices[j] > prices[i]:
                j += 1
            if prices[j] <= prices[i]:
                prices[i] -= prices[j]
        return prices
