class Solution:
    def isNumber(self, s: str) -> bool:
        def check(x):
            try:
                float(x)
                return True
            except ValueError:
                return False
        s = s.split('e')
        if len(s) == 1:
            return check(s[0]) and 'inf' not in s[0].lower()
        elif len(s) == 2:
            return check(s[0]) and check(s[1]) and not ('.' in s[1])
        else:
            return False
