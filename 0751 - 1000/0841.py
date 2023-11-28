from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        locks = [0 for _ in range(len(rooms))]
        locks[0] = 1
        newkeys = set(rooms[0])
        while newkeys:
            cur_key = newkeys.pop()
            if locks[cur_key] == 0:
                locks[cur_key] = 1
                newkeys = {k for k in (newkeys | set(rooms[cur_key])) if locks[k] == 0}
        return all(k == 1 for k in locks)


sol = Solution()
rm = [[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]]
ans = True
print(sol.canVisitAllRooms(rm) == ans)
