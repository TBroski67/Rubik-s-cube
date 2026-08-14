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
    match test_case:
        case 0:
            pass
        case 1:
            move("r u' r' u r u2 r' u r u' r'")
        case 2:
            move("r u' r' u' r u r' u2 r u' r'")
        case 3:
            move("y' r' u' r u2 r' u2 r y u' r u r'")
        case 4:
            move("y' r' u r u r' u r y u' r u r'")
        case 5:
            move("y' r' u' r u r' u r y u2 r u r'")
        case 6:
            move("f' u' f u r u r' u'")
        case 7:
            move("f' r u r' u' r' f r u")
        case 8:
            move("y' r' u r u' r' u r y")
        case 9:
            move("r u r' u' r u r' u")
        case 10:
            move("y' r' u' r u r' u' r y")
        case 11:
            move("r u' r' u r u' r' u")
        case 12:
            move("r2 u2 r2 u' r2 u' r2")
        case 13:
            move("r u r' f r' f' r u")
        case 14:
            move("r u' r' u r u2 r'")
        case 15:
            move("r u r' f r' f' r2 u' r' u")
        case 16:
            move("r u r' u' r u2 r' u'")
        case 17:
            move("f' l' u2 l f")
        case 18:
            move("r u' r' u2 r u r'")
        case 19:
            move("y' r' u' r u r' u2 r u y")
        case 20:
            move("y' r' u r u' r' u2 r y")
        case 21:
            move("r2 u r' u r u2 r2 u2")
        case 22:
            move("r u' r' u' r u2 r' u")
        case 23:
            move("r u' r' u f' u f u'")
        case 24:
            move("r u' r' u' r u r' u")
        case 25:
            move("f' u f u2 r u r'")
        case 26:
            move("r u' r'")
        case 27:
            move("y' r' u' r u2 r' u2 r u' y")
        case 28:
            move("r u' r' u' r u' r' u")
        case 29:
            move("y' r' u' r u2 r' u r u' y")
        case 30:
            move("r' u' r2 u' r2 u2 r")
        case 31:
            move("r' f r f'")
        case 32:
            move("r u r' u2 r u r' u")
        case 33:
            move("f' u f u' r u' r' u")
        case 34:
            move("r u r' u'")
        case 35:
            move("f' u f u' r u2 r' u")
        case 36:
            move("r u r' u2 r u' r' u")
        case 37:
            move("f' u f u' r u r' u")
        case 38:
            move("f' u f")
        case 39:
            move("r u r' u2 r u2 r' u")
        case 40:
            move("r u r' u' r u r' u2 r u' r'")
        case 41:
            move("y' r' u r u r' u' r u' y")
    solve_f2l()
    solve_centers()
    test_state = print_cube()
    if verify_test(test_state, solved_cube):
        return True
    else:
        return False

def test_oll(test_case):
    match test_case:
        #1 default case
        case 0:
            pass
        #7 cases with all edges solved
        case 1:
            move("r u2 r' u' r u' r'")
        case 2:
            move("r' u2 r' d' r u2 r' d r2")
        case 3:
            move("r' f' x l u r u' x' l' f")
        case 4:
            move("r u r' u r u2 r'")
        case 5:
            move("f r' f' x l u r u' x' l'")
        case 6:
            move("r u2 r' u' r u r' u' r u' r'")
        case 7:
            move("r' u2 r2 u r2 u r2 u2 r'")
        #15 bar cases
        case 8:
            move("l x u r' u' m' u r u' r'")
        case 9:
            move("f r' f' r u r u' r'")
        case 10:
            move("f u r u' r' f'")
        case 11:
            move("r' u' f u r u' r' f' r")
        case 12:
            move("f u f' r' f r u' r' f' r")
        case 13:
            move("l' x' u' l x u' r' u r l' x' u l x")
        case 14:
            move("l x u r' u' l' x' f r u r u' r' f'")
        case 15:
            move("u' r' u' f r' f' r u r u")
        case 16:
            move("l u f' u' l' u l f l'")
        case 17:
            move("l x u l' x' u r u' r' l x u' l' x'")
        case 18:
            move("f' u' f l x u' l' x' u l x u l' x'")
        case 19:
            move("l x u r u' l' x' f r' u r u' r' f'")
        case 20:
            move("f u f' u f u' r u' r' f'")
        case 21:
            move("f s u r u' r' u r u' r' f' s'")
        case 22:
            move("f r' f' u2 r u r' u r2 u2 r' u'")
        #8 dot cases
        case 23:
            move("f s u r u' r' s' u r u' r' f'")
        case 24:
            move("f r' f' r u2 f r' f' r2 u2 r'")
        case 25:
            move("m' u r u r' u' m2 u r u' r' m'")
        case 26:
            move("f r' f' r m' u r u' r' u' m")
        case 27:
            move("r' m' u2 r u r' u r2 m2 u2 r' u' r u' r' m'")
        case 28:
            move("f r' f' r u2 f r' f' r u' r u' r'")
        case 29:
            move("f u r u' r' f' u f s u r u' r' f' s'")
        case 30:
            move("f u r u' r' f' u' f s u r u' r' f' s'")
        #cases where edges form l shape, 27 total
        case 31:
            move("r u r' u' m u r u' r' m'")
        case 32:
            move("f r u' r' u r u r' f'")
        case 33:
            move("f r u r' u' f'")
        case 34:
            move("f r' f' r u r u r' u' r u' r'")
        case 35:
            move("f2 r u' r' u r u r2 f' r f'")
        case 36:
            move("f u r u' r' f' r u2 r' u' r u' r'")
        case 37:
            move("r m u2 r' f r' f' r u' r u' r' m'")
        case 38:
            move("r m u2 r' u' r u' r' m'")
        case 39:
            move("f u r u' r2 f' r u r u' r'")
        case 40:
            move("r b' r2 f r2 b r2 f' r")
        case 41:
            move("r m u r' u r u' r' u r u2 r' m'")
        case 42:
            move("f u r u' r' u r u' r' f'")
        case 43:
            move("f u r u' r' f' r' u2 r u r' u r")
        case 44:
            move("y' f' u f s u r u' r' s' y")
        case 45:
            move("x' u' r u r' x u' r' u' r u r' u r")
        case 46:
            move("r' m' u2 r u r' u r m")
        case 47:
            move("r u2 r' f r' f' r u' r u' r'")
        case 48:
            move("f u r u' r' f' u' f u r u' r' f' u")
        case 49:
            move("r' f r2 b' r2 f' r2 b r'")
        case 50:
            move("r' m' u' r u' r' u r u' r' u2 r m")
        case 51:
            move("f' l' u' l u f")
        case 52:
            move("f' u f u r u2 r' f r' f' r")
        case 53:
            move("r m u r' u r u2 r' m'")
        case 54:
            move("r' u' f r' f' r f r' f' r u r")
        case 55:
            move("r u2 r' f r' f' r2 u2 r'")
        case 56:
            move("f s r' f' r u r u' r' s'")
        case 57:
            move("r' m' u' r u' r' u2 r m")
    solve_oll()
    test_state = print_cube()
    if verify_test(test_state, solved_cube):
        return True
    else:
        return False
def test_pll(test_case):
    pass

#commented out steps that have been tested successfully
#test_step(test_center_solve, 24)
#test_step(test_cross, 24)
#test_step(test_f2l, 42)
#test_step(test_oll, 58)
test_step(test_pll, 0)
