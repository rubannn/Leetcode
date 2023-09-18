class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        symbols = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        st = ''.join([symbols[c] for c in digits])
        variants = [''.join(x) for x in permutations(st, len(digits))]
        res = []
        for item in variants:
            if all(c in symbols[digits[i]] for i, c in enumerate(item)) and item not in res:
                res.append(item)
        return res
