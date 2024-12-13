import main  # The code to test

def test_one():
    assert main.fixMe([1,9,1,5]) == [1,9,5,1]

def test_two():
    assert main.fixMe([3,9,1,5,2,9,1,5]) == [3,9,5,1,2,9,5,1]

def test_three():
    assert main.fixMe([9,1,2,5,1,9,2,5,1]) == [9,5,1,2,1,9,5,2,1]

def test_four():
    assert main.fixMe([9,1,2,3,4,5]) == [9,5,1,2,3,4,5]
