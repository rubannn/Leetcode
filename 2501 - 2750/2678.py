class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(p[-4:-2]) > 60 for p in details)
