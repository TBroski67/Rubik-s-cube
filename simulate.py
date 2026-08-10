import rotations
from display import print_cube, clear
from scramble import scramble

valid_inputs = ("exit", "o", "scramble",
                "u", "u'", "u2", "l", "l'", "l2",
                "f", "f'", "f2", "r", "r'", "r2",
                "b", "b'", "b2", "d", "d'", "d2",
                "m", "m'", "m2", "e", "e'", "e2",
                "s", "s'", "s2", "x", "x'", "x2",
                "y", "y'", "y2", "z", "z'", "z2")

def is_valid(commands):
    for command in commands:
        if command not in valid_inputs:
            return command
    return None

def main():
    while True:
        print_cube()
        actions = input("Input moves using cube notation, or type 'O' for options: ").lower().strip().split()
        clear()
        if "exit" in actions:
            print("""Thanks for trying out this program.
Have a nice day!""")
            return
        invalid_action = is_valid(actions)
        if invalid_action is not None:
            print(f"Sorry, '{invalid_action}' not recognized.")
            continue
        for action in actions:
            match action:
                case "o":
                    print("""Options:
The moves in cube notations are: u, l, f, r, b, d for clockwise turns on the corresponding face:
u for up, l for left, f for front, r for right, b for back, and d for down.
The whole cube rotation moves are x, y, and z, which move in the r, u, and f directions respectively.
The slice turn moves are m, e, and s, for middle, equator, and standing.
To input a move, type the letter for the move (u, l, f, r, b, d, m, e, s, x, y, z), and if desired,
also add a ' to denote a counterclockwise turn, or 2 for a half turn (180 degrees). To perform multiple moves,
type in separate move commands separated by spaces. To generate a random scramble, type 'scramble'.

To exit the program, type 'exit'.""")
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
                case "x":
                    rotations.x()
                case "x'":
                    rotations.xw()
                case "x2":
                    rotations.xTwo()
                case "y":
                    rotations.y()
                case "y'":
                    rotations.yw()
                case "y2":
                    rotations.yTwo()
                case "z":
                    rotations.z()
                case "z'":
                    rotations.zw()
                case "z2":
                    rotations.zTwo()

main()
