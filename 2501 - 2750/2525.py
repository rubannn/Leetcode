class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = any(p >= 10**4 for p in [length, width, height, mass]) or length * width * height >= 10**9
        heavy = mass >= 100

        if bulky and heavy:
            return "Both"
        elif bulky and (not heavy):
            return "Bulky"
        elif (not bulky) and heavy:
            return "Heavy"
        elif not (bulky and heavy):
            return "Neither"
