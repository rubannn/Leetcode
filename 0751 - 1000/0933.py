from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        if not self.queue or t - self.queue[0] <= 3000:
            self.queue.append(t)
            return len(self.queue)
        else:
            margin = t - 3000
            while self.queue and self.queue[0] < margin:
                self.queue.popleft()
            self.queue.append(t)
            return len(self.queue)
