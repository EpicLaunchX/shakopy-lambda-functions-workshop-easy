from pytemplate.utils.mapping import map_square

def test_map_square():
    assert map_square([1, 2, 3]) == [1, 4, 9]
    assert map_square([0, -1, -2]) == [0, 1, 4]
    assert map_square([]) == []
    assert map_square([5]) == [25]
    assert map_square([2, 3, 4]) == [4, 9, 16]