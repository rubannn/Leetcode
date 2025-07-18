class NumArray:

    def __init__(self, nums: List[int]):
        self.data = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.data[left : right + 1])
