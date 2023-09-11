def isHappy(self, n: int) -> bool:
    for _ in range(20):
        if n in (37, 58, 89, 145, 42, 20, 4, 16):
            return False
        n = sum(int(c)**2 for c in str(n))
    return True
