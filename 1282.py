def groupThePeople(groupSizes: list[int]) -> list[list[int]]:
    groups = dict()
    res = []
    for i, x in enumerate(groupSizes):
        if groups.get(x, -1) == -1:
            groups[x] = [i]
        else:
            cur = groups[x]
            if len(cur) == x:
                res.append(cur)
                groups[x] = [i]
            else:
                groups[x].append(i)
    for v in groups.values():
        res.append(v)
    return res


groupSizes = [3, 3, 3, 3, 3, 1, 3]
out = [[5], [0, 1, 2], [3, 4, 6]]
print(groupThePeople(groupSizes), out)

groupSizes = [2, 1, 3, 3, 3, 2]
out = [[1], [0, 5], [2, 3, 4]]
print(groupThePeople(groupSizes), out)
