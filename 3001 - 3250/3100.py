class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange - 1
            numExchange += 1
            drunk += 1
        return drunk
