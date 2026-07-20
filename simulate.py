import rotations
from display import print_cube, clear
from scramble import scramble

while True:
    print_cube()
    actions = input("Input moves using cube notation, or type 'O' for options: ").lower().strip().split()
    clear()
    for action in actions:
        if action=="o":
            print("""Options:
The moves in cube notations are: u, l, f, r, b, d for clockwise turns on the corresponding face:
u for up, l for left, f for front, r for right, b for back, and d for down. The slice turn moves are m, e, and s,
for middle, equator, and standing. To input a move, type the letter (u, l, f, r, b, d, m, e, s), and if desired,
also add a ' to denote a counterclockwise turn, or 2 for a half turn (180 degrees). To perform multiple moves,
type in separate move commands separated by spaces. To generate a random scramble, type 'scramble'.""")
            break
        elif action=="scramble":
            scramble()
            break
        elif action=="u":
            rotations.u()
        elif action=="u'":
            rotations.uw()
        elif action=="u2":
            rotations.uTwo()
        elif action=="l":
            rotations.l()
        elif action=="l'":
            rotations.lw()
        elif action=="l2":
            rotations.lTwo()
        elif action=="f":
            rotations.f()
        elif action=="f'":
            rotations.fw()
        elif action=="f2":
            rotations.fTwo()
        elif action=="r":
            rotations.r()
        elif action=="r'":
            rotations.rw()
        elif action=="r2":
            rotations.rTwo()
        elif action=="b":
            rotations.b()
        elif action=="b'":
            rotations.bw()
        elif action=="b2":
            rotations.bTwo()
        elif action=="d":
            rotations.d()
        elif action=="d'":
            rotations.dw()
        elif action=="d2":
            rotations.dTwo()
        elif action=="m":
            rotations.m()
        elif action=="m'":
            rotations.mw()
        elif action=="m2":
            rotations.mTwo()
        elif action=="e":
            rotations.e()
        elif action=="e'":
            rotations.ew()
        elif action=="e2":
            rotations.eTwo()
        elif action=="s":
            rotations.s()
        elif action=="s'":
            rotations.sw()
        elif action=="s2":
            rotations.sTwo()
        else:
            print("Sorry, input not recognized.")
            break
