from itertools import permutations


def permuteUnique(self, nums: list[int]) -> list[list[int]]:
    return list(set(permutations(nums, len(nums))))
