class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted([(x, y) for x, y in Counter(nums).items()], key=lambda x: (-x[1]))
        return [x[0] for x in nums[:k]]
