def selfDividingNumbers(left: int,  right: int) -> list[int]:
    def check(n: int) -> bool:
        return sum(int(x) > 0 and (n % int(x) == 0) for x in str(n)) == len(str(n))
    return [i for i in range(left, right + 1) if check(i)]


left = 1
right = 22
m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
print(selfDividingNumbers(left,  right) == m)


left = 47
right = 85
m = [48, 55, 66, 77]
print(selfDividingNumbers(left,  right) == m)
