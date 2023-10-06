from math import prod

def integerBreak(n: int) -> int:
    k = 2
    res = 0
    while k <= n:
        elems = [n // k] * k
        elems[-1] += n % k
        res = max(prod(elems), res)

        elems = [(n + n % k) // k] * k
        elems[-1] = n - sum(elems[:-1])
        res = max(prod(elems), res)
        k += 1
    return res


n = 2; res = 1
print(integerBreak(n) == res)

n = 10; res = 36
print(integerBreak(n) == res)

n = 8; res = 18
print(integerBreak(n) == res)
