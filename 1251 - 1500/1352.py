class ProductOfNumbers:

    def __init__(self):
        self.stream = []

    def add(self, num: int) -> None:
        if num == 0:
            self.stream = []
        self.stream.append(num)

    def getProduct(self, k: int) -> int:
        p = 1
        for x in self.stream[-k:]:
            p *= x
        return p
