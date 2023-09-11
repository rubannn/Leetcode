def maxProfit(prices: list[int]) -> int:
    # b = float('-inf')
    b = float('inf')
    s = 0
    for p in prices:
        # b = max(-p, b)
        # s = max(p + b, s)
        b = min(p, b)
        s = max(p - b, s)
        print(b, s)
    return s


prices = [7, 1, 5, 3, 6, 4]
out = 5
print(maxProfit(prices) == out)

# prices = [7,6,4,3,1]
# out = 0
# print(maxProfit(prices) == out)
