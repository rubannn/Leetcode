def romanToInt(self, s: str) -> int:
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dec = 0
    for i in range(len(s) - 1):
        dec += (-1) ** (rom[s[i]] < rom[s[i + 1]]) * rom[s[i]]
    return dec + rom[s[-1]]
