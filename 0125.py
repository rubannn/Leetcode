def isPalindrome(s: str) -> bool:
    st = [c.lower() for c in s if c.isalnum()]
    return st == st[::-1]
