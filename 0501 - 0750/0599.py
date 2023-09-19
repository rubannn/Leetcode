class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mn = len(list1) + len(list2)
        res = []
        for i in range(len(list1)):
            if list1[i] in list2:
                t = i + list2.index(list1[i])
                if t < mn:
                    mn = t
                    res = [list1[i]]
                elif t == mn:
                    res.append(list1[i])
        return res
