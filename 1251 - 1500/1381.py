class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.deep = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.deep:
            self.stack.append(x)

    def pop(self) -> int:
        x = self.stack[-1] if self.stack else -1
        self.stack = self.stack[:-1]
        return x

    def increment(self, k: int, val: int) -> None:
        cur_deep = len(self.stack)
        for i in range(min(k, cur_deep, self.deep)):
            self.stack[i] += val
