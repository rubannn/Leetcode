class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mn = blocks.count("W")
        for i in range(len(blocks) - k + 1):
            substr = blocks[i : i + k]
            w_count = substr.count("W")
            print(substr, w_count)
            if mn > w_count:
                mn = w_count
        return mn


tests = [
    ("WBBWWBBWBW", 7, 3),
    ("WBWBBBW", 2, 0),
    ("BWWWBB", 6, 3),
    ("WWBBBWBBBBBWWBWWWB", 16, 6),
]

sol = Solution()
for block, k, ans in tests[:]:
    print(sol.minimumRecolors(block, k), ans)
