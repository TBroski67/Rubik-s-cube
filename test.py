"""INSTRUCTIONS FOR USAGE:
When you run this file, it should first display an unfolded cube, with
the sides laid out in a sideways lowercase t shape. To verify the next
test case, hold a solved cube with the yellow side on top and the blue
side in front. Rotate the yellow side clockwise, the blue side 180
degrees, and the yellow side clockwise again. It should match with the
output from the second print_cube command. The third test case will
generate a random scramble. Pieces with the same color should not be
next to each other on adjacent faces.

You may comment out any sections of code to focus on specific test cases.
"""
from display import print_cube
import rotations
from time import sleep
from scramble import scramble
#test that function to display cube works
print_cube()
sleep(5) #show unscrambled cube for a few seconds, may change this for testing
#do U and F2 rotation, then display the cube
rotations.u()
rotations.fTwo()
rotations.u()
print_cube()
sleep(5) #okay to change sleep time
scramble()
print_cube()