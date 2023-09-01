class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        i = ['type', 'color', 'name'].index(ruleKey)
        return len([item for item in items if item[i] == ruleValue])
