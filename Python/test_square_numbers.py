from square_numbers import square_num

def test_square_positive_numbers():
    assert square_num([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]

def test_square_negative_numbers():
    assert square_num([-1, -2, -3]) == [1, 4, 9]

def test_square_mixed_numbers():
    assert square_num([0, -1, 2, -3, 4]) == [0, 1, 4, 9, 16]