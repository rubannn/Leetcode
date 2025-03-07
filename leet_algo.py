def is_prime_quick(n):
    if n in (2, 3, 5):
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n < 0 or n == 1:
        return False
    p, q, h = 7, 11, n**0.5
    while q <= h and (n % p != 0) and (n % q != 0):
        p, q = p + 6, q + 6
    if q <= h or p <= h and n % p == 0:
        return False
    return True


def is_prime(n):
    if n in (2, 3, 5, 7):
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n < 0 or n == 1:
        return False
    d = 7
    while d <= n**0.5:
        if n % d == 0:
            return False
        d += 2
    return True


p = [x for x in range(2, 50000) if is_prime(x)]


def find_prime_factor(df, n):
    i = 2
    while n > 1:
        if n % i == 0 and df.get(i) is None:
            df[i] = 0
        while n % i == 0:
            df[i] += 1
            n //= i
        i += 1
    return df


def prime_factors(n):
    dict_of_factors = {}
    find_prime_factor(dict_of_factors, n)
    print(dict_of_factors)
    return []
