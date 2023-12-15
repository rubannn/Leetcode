class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city = dict()
        for a, b in paths:
            city["from"] = city.get("from", set()) | {a}
            city["to"] = city.get("to", set()) | {b}
        return (city["to"] - city["from"]).pop()
