class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        for i, s in enumerate(seats):
            res += abs(students[i] - s)
        return res
