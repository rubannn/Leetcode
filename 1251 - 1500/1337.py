def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
    res = [(i, sum(row)) for i, row in enumerate(mat)]
    res.sort(key=lambda x: x[1])
    return [x for x, _ in res][:k]
