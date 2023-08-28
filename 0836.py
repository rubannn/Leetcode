def isRectangleOverlap(rec1: list, rec2: list) -> bool:
    w = max(0, min(rec1[2], rec2[2]) - max(rec1[0], rec2[0]))
    h = max(0, min(rec1[3], rec2[3]) - max(rec1[1], rec2[1]))
    return w * h != 0
