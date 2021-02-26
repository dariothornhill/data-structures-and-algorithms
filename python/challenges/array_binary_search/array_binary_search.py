
def BinarySearch(sorted: list, value: int) -> int:
    def binary_search(start: int , end: int):
        if start >= end:
            return -1
        midpoint = len(sorted[start:end]) // 2
        if value == sorted[midpoint]:
            return midpoint
        if value > sorted[midpoint]:
            return binary_search(midpoint, -1)
        if value < sorted[midpoint]:
            return binary_search(0, midpoint)
        return False
    return binary_search(0, len(sorted))
