import rotations
from display import print_cube
from cross import solve_cross
#scramble from online cube timer
rotations.uTwo()
rotations.r()
rotations.u()
rotations.bTwo()
rotations.l()
rotations.f()
rotations.u()
rotations.f()
rotations.lw()
rotations.f()
rotations.lw()
rotations.r()
rotations.uTwo()
rotations.l()
rotations.rw()
rotations.bw()
rotations.lTwo()
rotations.rw()
rotations.u()
rotations.fTwo()
#display cube
print_cube()
#apply solving alogrithms, then display cube
solve_cross()
print_cube()
