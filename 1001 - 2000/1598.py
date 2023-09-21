class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for log in logs:
            if log == '../':
                level -= 1 if level > 0 else 0
            elif log == './':
                continue
            else:
                level += 1
        return level
