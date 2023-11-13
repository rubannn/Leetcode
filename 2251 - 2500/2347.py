class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        mx = max(ranks.count(c) for c in ranks)
        if len(set(suits)) == 1:
            return "Flush"
        elif mx > 2:
            return "Three of a Kind"
        elif mx == 2:
            return "Pair"
        return "High Card"
