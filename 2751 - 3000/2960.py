class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        devices = 0
        for b in batteryPercentages:
            b -= devices
            devices += b > 0
        return devices
