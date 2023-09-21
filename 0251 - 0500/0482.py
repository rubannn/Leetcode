class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        s = ' '*(k - len(s) % k) + s
        s = '-'.join(s[i:i+k] for i in range(0, len(s), k))
        return s.strip(' -')
