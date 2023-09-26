class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            last = (digits[i] + 1)//10
            digits[i] = (digits[i] + 1) % 10
            if last == 0: return digits
        return digits if last == 0 else [last] + digits
