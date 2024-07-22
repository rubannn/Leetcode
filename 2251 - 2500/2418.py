class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names, heights = zip(*sorted(zip(names, heights), key=lambda a: -a[1]))
        return names
