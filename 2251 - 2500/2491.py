class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        s = skill[0] + skill[-1]
        sm = skill[0] * skill[-1]
        a, b = 1, len(skill) - 2
        while a < b:
            if skill[a] + skill[b] != s:
                return -1
            sm += skill[a] * skill[b]
            a += 1
            b -= 1
        return sm
