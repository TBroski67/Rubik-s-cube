import rotations
from display import print_cube, clear
from scramble import scramble

while True:
    print_cube()
    actions = input("Input moves using cube notation, or type 'O' for options: ").lower().strip().split()
    clear()
        for action in actions:
        match action:
            case "o":
                print("""Options:
The moves in cube notations are: u, l, f, r, b, d for clockwise turns on the corresponding face:
u for up, l for left, f for front, r for right, b for back, and d for down. The slice turn moves are m, e, and s,
for middle, equator, and standing. To input a move, type the letter (u, l, f, r, b, d, m, e, s), and if desired,
also add a ' to denote a counterclockwise turn, or 2 for a half turn (180 degrees). To perform multiple moves,
type in separate move commands separated by spaces. To generate a random scramble, type 'scramble'.""")
                break
            case "scramble":
                scramble()
                break
            case "u":
                rotations.u()
            case "u'":
                rotations.uw()
            case "u2":
                rotations.uTwo()
            case "l":
                rotations.l()
            case "l'":
                rotations.lw()
            case "l2":
                rotations.lTwo()
            case "f":
                rotations.f()
            case "f'":
                rotations.fw()
            case "f2":
                rotations.fTwo()
            case "r":
                rotations.r()
            case "r'":
                rotations.rw()
            case "r2":
                rotations.rTwo()
            case "b":
                rotations.b()
            case "b'":
                rotations.bw()
            case "b2":
                rotations.bTwo()
            case "d":
                rotations.d()
            case "d'":
                rotations.dw()
            case "d2":
                rotations.dTwo()
            case "m":
                rotations.m()
            case "m'":
                rotations.mw()
            case "m2":
                rotations.mTwo()
            case "e":
                rotations.e()
            case "e'":
                rotations.ew()
            case "e2":
                rotations.eTwo()
            case "s":
                rotations.s()
            case "s'":
                rotations.sw()
            case "s2":
                rotations.sTwo()
            case _:
                print("Sorry, input not recognized.")
                break
