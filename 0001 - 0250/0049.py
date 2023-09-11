def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    res = dict()
    for x in strs:
        v = ''.join(sorted(x))
        if res.get(v, None) is None:
            res[v] = [x]
        else:
            res[v] += [x]
    return res.values()
