'''This file contains the test functions for each
part of the solver: positioning the centers (for
convenience), and solving the white cross, the
first two layers, last-layer orientation, and
last-layer permutation.'''
from cross import solve_centers, solve_edge
from f2l import solve_f2l
from oll import solve_oll
import rotations
from display import print_cube
from test import verify_test
from move_parser import move

solved_cube = """      y y y
      y y y
      y y y
o o o b b b r r r g g g
o o o b b b r r r g g g
o o o b b b r r r g g g
      w w w
      w w w
      w w w"""

#function to test a step in the solving algorithm;
#runs through all test cases until a case fails,
#and the program stops at the failed case or
#reports that it finished successfully.
def test_step(test_func, cases):
    for case in range(cases):
        if not test_func(case):
            print(f"Test case {case} failed.")
            return False
        if case==cases - 1:
            print("All cases passed successfully.")
            return True

#tests function to position centers
def test_center_solve(test_case):
    match test_case:
        #starts at case 0 for for loop convenience
        case 0:
            #case with default center positioning
            #to test that function does mess with it
            pass
        #middle layer positioning switched
        case 1:
            rotations.y()
        case 2:
            rotations.yw()
        case 3:
            rotations.yTwo()
        case 4:
            rotations.z()
        case 5:
            rotations.z()
            rotations.x()
        case 6:
            rotations.z()
            rotations.xw()
        case 7:
            rotations.z()
            rotations.xTwo()
        case 8:
            rotations.x()
        case 9:
            rotations.x()
            rotations.z()
        case 10:
            rotations.x()
            rotations.zw()
        case 11:
            rotations.x()
            rotations.zTwo()
        case 12:
            rotations.xw()
        case 13:
            rotations.xw()
            rotations.z()
        case 14:
            rotations.xw()
            rotations.zw()
        case 15:
            rotations.xw()
            rotations.zTwo()
        case 16:
            rotations.xTwo()
        case 17:
            rotations.xTwo()
            rotations.y()
        case 18:
            rotations.xTwo()
            rotations.yw()
        case 19:
            rotations.xTwo()
            rotations.yTwo()
        case 20:
            rotations.zw()
        case 21:
            rotations.zw()
            rotations.x()
        case 22:
            rotations.zw()
            rotations.xw()
        case 23:
            rotations.zw()
            rotations.xTwo()
    solve_centers()
    test_state = print_cube()
    if verify_test(test_state, solved_cube):
        return True
    else:
        return False

#tests for other algorithms, to be worked on later
def test_cross(test_case):
    match test_case:
        case 0:
            pass
        case 1:
            move("d' l d l'")
        case 2:
            move("d r d' r'")
        case 3:
            move("d2 b d2 b'")
        case 4:
            move("d' l' d")
        case 5:
            move("d' l d")
        case 6:
            move("d r' d'")
        case 7:
            move("d r d'")
        case 8:
            move("f2")
        case 9:
            move("f2 u")
        case 10:
            move("f2 u'")
        case 11:
            move("f2 u2")
        case 12:
            move("d' l' d f'")
        case 13:
            move("f l")
        case 14:
            move("d r' d' b'")
        case 15:
            move("f' r'")
        case 16:
            move("f")
        case 17:
            move("f'")
        case 18:
            move("d2 b d2")
        case 19:
            move("d2 b' d2")
        case 20:
            move("r' f' r u")
        case 21:
            move("r' f' r")
        case 22:
            move("r' f' r u'")
        case 23:
            move("l f l'")
    solve_edge('b')
    test_state = print_cube()
    if verify_test(test_state, solved_cube):
        return True
    else:
        return False

def test_f2l(test_case):
    pass
def test_oll(test_case):
    pass
def test_pll(test_case):
    pass

test_step(test_center_solve, 24)
test_step(test_cross, 24)
