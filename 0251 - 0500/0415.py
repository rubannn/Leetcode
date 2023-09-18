class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1, num2 = num1[::-1], num2[::-1]
        res = ''
        r = 0
        for i in range(len(num1)):
            if i < len(num2):
                t = int(num1[i]) + int(num2[i]) + r
            else:
                t = int(num1[i]) + r
            r = t // 10
            res = f'{t % 10}' + res
        if r > 0:
            res = f'{r}' + res
        return res
