from pytemplate.utils.sorting import sort_list


def test_sort_list():
    assert sort_list([3, 1, 2]) == [1, 2, 3]
    assert sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sort_list([-1, -3, 0, 2]) == [-3, -1, 0, 2]
    assert sort_list([]) == []
    assert sort_list([1]) == [1]
