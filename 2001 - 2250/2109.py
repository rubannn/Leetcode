class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        p = 0
        sn = ""
        for i, c in enumerate(s):
            if p < len(spaces) and spaces[p] == i:
                sn += " "
                p += 1
            sn += c
        return sn
