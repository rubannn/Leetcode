from typing import List
from collections import defaultdict


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = dict()
    for x in strs:
        v = "".join(sorted(x))
        if res.get(v, None) is None:
            res[v] = [x]
        else:
            res[v] += [x]
    return res.values()


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dc = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        dc[key].append(s)
    return dc.values()
