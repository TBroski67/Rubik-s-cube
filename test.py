"""INSTRUCTIONS FOR USAGE:
When you run this file, it should first display an unfolded cube, with
the sides laid out in a sideways lowercase t shape. To verify the next
test case, hold a solved cube with the yellow side on top and the blue
side in front. Rotate the yellow side clockwise, the blue side 180
degrees, and the yellow side clockwise again. It should match with the
output from the second print_cube command. The third test case will
generate a random scramble. Pieces with the same color should not be
next to each other on adjacent faces.

The first two test cases will also print a message in the console saying
whether the test case passes or fails.

You may comment out any sections of code to focus on specific test cases.
"""
from display import print_cube
import rotations
from scramble import scramble

#function to verify if test cases pass
def verify_test(cube_state, expected_state):
    if expected_state==cube_state:
        print("Test passed. Cube displays correctly.")
        return True
    else:
        print("Test failed. Correct cube state should be:")
        print(expected_state)
        return False
#test that function to display cube works, stored as function
#to prevent interfering with algorithm_test.py operations.
def test():
    test_state = print_cube()
    expected_state = """      y y y
      y y y
      y y y
o o o b b b r r r g g g
o o o b b b r r r g g g
o o o b b b r r r g g g
      w w w
      w w w
      w w w"""
    verify_test(test_state, expected_state)
    #do U and F2 rotation, then display the cube
    rotations.u()
    rotations.fTwo()
    rotations.u()
    test_state = print_cube()
    expected_state = """      w y y
      w y y
      w y y
b b b o g g o o o b b r
o o r b b b o r r g g g
o o g r r r b r r g g g
      y y y
      w w w
      w w w"""
    verify_test(test_state, expected_state)
    scramble()
    print_cube()
