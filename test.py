from display import print_cube
import rotations
from time import sleep
#test that function to display cube works
print_cube()
sleep(5) #show unscrambled cube for five seconds
#do U and F2 rotation, then display the cube
rotations.u()
rotations.fTwo()
print_cube()