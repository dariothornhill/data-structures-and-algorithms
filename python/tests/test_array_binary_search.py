from challenges.array_binary_search.array_binary_search import BinarySearch


def test_import():
    assert BinarySearch

def test_binary_search_array():
    arr = [1,3,4,5,6,7]
    key = 5
    expected = 3
    assert(expected == BinarySearch(arr, key))

def test_binary_search_array_not_found():
    arr = [1,3,4,5,6,7]
    key = 2
    expected = -1
    assert(expected == BinarySearch(arr, key))

