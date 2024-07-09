class Solution:
    # variant 1
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink, rest = numBottles, 0
        while numBottles >= numExchange:
            numBottles, rest = divmod(numBottles, numExchange)
            drink += numBottles
            numBottles += rest
        return drink

    # variant 2
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)
