import pytest

# Function to test Square
def square(n):
    return n**2

# Function to test cube
def cube(n):
    return n**3

# testing fifth power
def fifth_power(n):
    return n**5

# Testing the Square Function
def test_square():
    assert square(2)==4,"Test Failed: Square of 2 should be 4"
    assert square(3)==9,"Test Failed: Square of 3 should be 9"

# Testing the Cube Function
def test_cube():
    assert cube(2)==8,"Test Failed: cube of 2 should be 8"
    assert cube(3)==27,"Test Failed: cube of 3 should be 27"

# Testing  Fifth power function
def test_fifth_power():
    assert fifth_power(2)==32,"Test Failed: Fifth Power of 2 should be 32"
    assert fifth_power(3)==243,"Test Failed: Fifth Power of 3 should be 243"

# Test for invalid Input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")