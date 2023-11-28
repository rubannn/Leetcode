class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0 and len(path) == k:
                result.append(path[:])
                return
            for i in range(start, 10):
                if i > target:
                    break
                path.append(i)
                backtrack(i + 1, target - i, path)
                path.pop()

        result = []
        backtrack(1, n, [])
        return result
