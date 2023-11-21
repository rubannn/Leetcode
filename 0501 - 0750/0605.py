class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed[:2] == [0, 0] or flowerbed == [0]:
            flowerbed[0] = 1
            n -= 1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        if flowerbed[-2:] == [0, 0]:
            n -= 1
        return n <= 0
