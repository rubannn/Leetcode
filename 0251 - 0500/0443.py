class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return len(chars)
        pred = ''
        k = p = 1
        while p < len(chars):
            if chars[p] == chars[p-1]:
                k += 1
                chars.pop(p)
            else:
                if k > 1:
                    for c in list(str(k)):
                        chars.insert(p, c)
                        p += 1
                k = 1
                p += 1
        if k > 1:
            for c in list(str(k)):
                chars.insert(p, c)
                p += 1
        return len(chars)
