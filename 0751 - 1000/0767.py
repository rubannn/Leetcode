def reorganizeString(self, s: str) -> str:
    symbols = dict()
    for c in s:
        symbols[c] = symbols.get(c, 0) + 1
    h = [(-cnt, sm) for sm, cnt in symbols.items()]
    heapq.heapify(h)

    res = []
    while h:
        count, letter = heapq.heappop(h)
        if not res or res[-1] != letter:
            count += 1
            res.append(letter)
            if count != 0:
                heapq.heappush(h, (count, letter))
            continue

        if not h:
            return ''

        count2, letter2 = heapq.heappop(h)
        count2 += 1
        res.append(letter2)
        if count2 != 0:
            heapq.heappush(h, (count2, letter2))
        heapq.heappush(h, (count, letter))
    return ''.join(res)
