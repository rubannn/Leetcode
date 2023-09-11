def intToRoman(self, num: int) -> str:
    dec = 'IVXLCDM'
    rom, p = '', 0
    while num > 0:
        k = num % 10
        num //= 10
        if k in (4, 9):
            rom = (dec[p] + dec[p+1 + int(k == 9)]) + rom
        elif k > 0:
            rom = ((dec[p+1] if k >= 5 else '') + dec[p] * (k - 5 * int(k >= 5))) + rom
        p += 2
    return rom
