def isIsomorphic(self, s: str, t: str) -> bool:
    pairs = dict()
    for i in range(len(s)):
        if pairs.get(s[i]) is None and not (t[i] in pairs.values()):
            pairs[s[i]] = t[i]
        elif pairs.get(s[i]) != t[i]:
            return False
    return True
