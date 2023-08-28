def numberToWords(num: int) -> str:
    digits = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
        7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven',
        12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
        16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
        20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
        60: 'Sixty',  70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
    }
    handreds = {1: 'Hundred', 2: 'Thousand', 3: 'Million', 4: 'Billion'}

    if not num:
        return "Zero"
    txt = []
    k = 1
    while num > 0:
        subnum = []
        hundred = num % 1000 // 100
        less_hundred = num % 100

        if hundred > 0:
            subnum.append(digits.get(hundred % 10, ''))
            subnum.append(handreds[1])

        if less_hundred < 21:
            subnum.append(digits.get(less_hundred, ''))
        else:
            subnum.append(digits.get(less_hundred // 10 * 10, ''))
            subnum.append(digits.get(less_hundred % 10, ''))

        if k > 1 and (hundred > 0 or less_hundred > 0):
            subnum.append(handreds.get(k, ''))

        txt = subnum + txt
        num //= 1000
        k += 1
    return ' '.join(w for w in txt if w)


n = 123
res = "One Hundred Twenty Three"
print(numberToWords(n) == res)

n = 12345
res = "Twelve Thousand Three Hundred Forty Five"
print(numberToWords(n) == res)

n = 1234567
res = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
print(numberToWords(n) == res)

n = 1_234_567_891
res = "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
print(numberToWords(n) == res)

n = 30
res = "Thirty"
print(numberToWords(n) == res)

n = 1000
res = "One Thousand"
print(numberToWords(n) == res)

n = 1000000
res = "One Million"
print(numberToWords(n) == res)
