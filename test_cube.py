from cube import cube_number

def test_case1():
    assert cube_number(3) == "Number : 3\nCube : 27"

def test_case2():
    assert cube_number(5) == "Number : 5\nCube : 125"

def test_case3():
    assert cube_number(0) == "Number : 0\nCube : 0"