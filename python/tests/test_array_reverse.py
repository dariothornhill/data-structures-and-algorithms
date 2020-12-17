from challenges.array_reverse.array_reverse import array_reverse


def test_import():
    assert array_reverse

def test_reverses_array():
    arr = [4,5,6,1,1,7,3]
    expected = [3,7,1,1,6,5,4]
    assert(expected == array_reverse(arr))
