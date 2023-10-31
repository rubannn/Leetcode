class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        sm = arr[0]
        for i in range(1, len(pref)):
            arr.append(sm ^ pref[i])
            sm = sm ^ arr[-1]
        return arr
