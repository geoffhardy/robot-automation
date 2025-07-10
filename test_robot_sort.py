from robot_sort import sort

def test_sort_standard():
    assert sort(10, 10, 10, 10) == "STANDARD"
    assert sort(149, 10, 10, 10) == "STANDARD"
    assert sort(10, 149, 10, 10) == "STANDARD"
    assert sort(10, 10, 149, 10) == "STANDARD"
    assert sort(10, 10, 10, 19) == "STANDARD"
    assert sort(100, 100, 99, 10) == "STANDARD"
    assert sort(99, 100, 100, 10) == "STANDARD"
    assert sort(100, 99, 100, 10) == "STANDARD"

    # volume < 1,000,000 and mass < 20
    assert sort(149, 149, 45, 19) == "STANDARD"
    

def test_sort_special():
    # bulky volume > 1,000,000
    assert sort(100, 100, 100, 10) == "SPECIAL"
    assert sort(10, 1000, 100, 10) == "SPECIAL"

    # any edge >= 150
    assert sort(150, 10, 10, 10) == "SPECIAL"
    assert sort(10, 150, 10, 10) == "SPECIAL"
    assert sort(10, 10, 150, 10) == "SPECIAL"
    assert sort(200, 10, 10, 10) == "SPECIAL"
    assert sort(10, 200, 10, 10) == "SPECIAL"
    assert sort(10, 10, 200, 10) == "SPECIAL"
    # mass >= 20
    assert sort(10, 10, 10, 20) == "SPECIAL"
    assert sort(10, 10, 10, 100) == "SPECIAL"
    # volume < 1,000,000, but mass >= 20
    assert sort(149, 149, 45, 20) == "SPECIAL"


def test_sort_rejected():
    # edge >= 150 and mass >= 20
    assert sort(150, 1, 1, 20) == "REJECTED"
    assert sort(1, 150, 1, 20) == "REJECTED"
    assert sort(1, 1, 150, 20) == "REJECTED"

    # volume >= 1,000,000 and mass >= 20
    assert sort(149, 149, 149, 20) == "REJECTED"
    assert sort(149, 149, 49, 20) == "REJECTED"
