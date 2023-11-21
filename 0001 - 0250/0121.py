def maxProfit(prices: list[int]) -> int:
    low = 0
    profit = 0
    for i, p in enumerate(prices):
        if p < prices[low]:
            low = i
            continue
        profit = max(profit, p - prices[low])
    return profit


prices = [7, 1, 5, 3, 6, 4]
out = 5
print(maxProfit(prices) == out)

prices = [7,6,4,3,1]
out = 0
print(maxProfit(prices) == out)
