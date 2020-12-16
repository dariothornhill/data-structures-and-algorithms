
def BinarySearch(sorted: list, key: int) -> int:
    midpoint = len(sorted) // 2
    if key == sorted[midpoint]:
        return midpoint
    if key > sorted[midpoint]:
        return BinarySearch(sorted[midpoint:-1], key)
    if key < sorted[midpoint]:
        return BinarySearch(sorted[0:midpoint], key)
    return False
