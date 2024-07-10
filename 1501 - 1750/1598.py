class Solution:
    # variant 1
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for log in logs:
            if log == "../":
                level -= 1 if level > 0 else 0
            elif log == "./":
                continue
            else:
                level += 1
        return level

    # variant 2
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for x in logs:
            if x == "../":
                level += (-1) * (level > 0)
            elif x == "./":
                continue
            else:
                level += 1
        return level
