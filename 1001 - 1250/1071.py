class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        t = gcd(len(str1), len(str2))
        if str1[:t] * (len(str2) // t) == str2 and str2[:t] * (len(str1) // t) == str1:
            return str1[:t]
        return ''
