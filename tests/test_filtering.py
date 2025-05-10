from pytemplate.utils.filtering import filter_even_numbers


def test_filter_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4, 5]) == [2, 4]
    assert filter_even_numbers([10, 15, 20, 25]) == [10, 20]
    assert filter_even_numbers([0, -2, -3, -4]) == [0, -2, -4]
    assert filter_even_numbers([]) == []
    assert filter_even_numbers([1, 3, 5]) == []
