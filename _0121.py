def maxProfit(prices: list[int]) -> int:
    res = [0]
    for i in range(len(prices) - 1):
        mx = max(prices[i+1:])
        if mx >= prices[i]:
            res.append(mx - prices[i])
    return max(res)


prices = [7,1,5,3,6,4]
out = 5
print(maxProfit(prices) == out)

prices = [7,6,4,3,1]
out = 0
print(maxProfit(prices) == out)
