from challenges.array_shift.array_shift import insert_shift_array


def test_import():
    assert insert_shift_array

def test_shifts_array():
    arr = [1,3,4,5,6,7]
    value = 2
    expected = [1,2,3,4,5,6,7]
    assert(expected == insert_shift_array(arr, value))
