# Worst case time O(n)
# Worst case space O(n)
def insert_shift_array(arr: list, value: int) -> list:
    for i in range(len(arr)):
        if arr[i] > value:
            newArray = arr[:i] + [value] + arr[i::]
            return newArray
