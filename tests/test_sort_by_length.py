from pytemplate.utils.sort_by_length import sort_by_length


def test_sort_by_length():
    assert sort_by_length(["apple", "banana", "pear"]) == ["pear", "apple", "banana"]
    assert sort_by_length(["a", "bb", "ccc", "dddd"]) == ["a", "bb", "ccc", "dddd"]
    assert sort_by_length(["longest", "short", "tiny"]) == ["tiny", "short", "longest"]
    assert sort_by_length([]) == []
    assert sort_by_length(["same", "size"]) == ["same", "size"]
