class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        left, right = 0, n - 1
        while left < right:
            if s[left] == s[right]:

                while left + 1 < n and (s[left] == s[left + 1]):
                    left += 1
                while left < right and right - 1 >= 0 and (s[right] == s[right - 1]):
                    right -= 1

                left += 1
                right -= 1
            else:
                break
        return len(s[left : right + 1])


sol = Solution()
tests = [("ca", 2), ("cabaabac", 0), ("aabccabba", 3)]

for t, ans in tests[:]:
    print(sol.minimumLength(t), ans)
