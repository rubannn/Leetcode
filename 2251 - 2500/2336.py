from heapq import heapify, heappop, heappush

class SmallestInfiniteSet:

    def __init__(self):
        self.pq = list(range(1, 1001))
        heapify(self.pq)


    def popSmallest(self) -> int:
        return heappop(self.pq)

    def addBack(self, num: int) -> None:
        if not num in self.pq:
            heappush(self.pq, num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
