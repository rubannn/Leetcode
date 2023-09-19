class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 0
        line_count = 0
        for c in s:
            width = widths[ord(c) - ord('a')]
            if line + width <= 100:
                line += width
            else:
                line = width
                line_count += 1
        if line > 0:
            line_count += 1
        return [line_count, line]
