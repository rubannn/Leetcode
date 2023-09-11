def findLongestChain(self, pairs: list[list[int]]) -> int:
    pairs.sort(key=lambda x: x[0])
    chain = 0
    last = pairs[0][0] - 1
    for pair in pairs:
        if last < pair[0]:
            chain += 1
            last = pair[1]
        else:
            last = min(last, pair[1])
    return chain
