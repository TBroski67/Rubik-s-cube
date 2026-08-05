'''This file uses a constant scramble (always the same scramble)
and uses the solving algorithm to attempt to solve the scramble.
Once the solver is complete, this program should produce a solved
cube as the final result.'''
import rotations
from display import print_cube
from cross import solve_cross
from f2l import solve_f2l
#scramble generated on an online cube timer website
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
print_cube()
solve_cross()
print_cube()
solve_f2l()
print_cube()
