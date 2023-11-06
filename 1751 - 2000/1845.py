# variant 1
from queue import PriorityQueue
class SeatManager:

    def __init__(self, n: int):
        self.stack = PriorityQueue(n)
        for i in range(1, n+1):
            self.stack.put(i)

    def reserve(self) -> int:
            return self.stack.get()

    def unreserve(self, seatNumber: int) -> None:
        self.stack.put(seatNumber)

# variant 2
class SeatManager:

    def __init__(self, n: int):
        self.heap = list(range(1, n + 1))

    def reserve(self) -> int:
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
