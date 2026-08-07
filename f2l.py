import cube
import rotations
from cross import solve_centers, find_edge
from move_parser import move
from display import print_cube
def find_corner(color1, color2, color3):
    corner_list = [(cube.u1, cube.l1, cube.b3),
                   (cube.u3, cube.b1, cube.r3),
                   (cube.u9, cube.r1, cube.f3),
                   (cube.u7, cube.f1, cube.l3),
                   (cube.d1, cube.l9, cube.f7),
                   (cube.d3, cube.f9, cube.r7),
                   (cube.d9, cube.r9, cube.b7),
                   (cube.d7, cube.b9, cube.l7)]
    for corner in corner_list:
        if corner[0].color==color1 or corner[1].color==color1 or corner[2].color==color1:
            if corner[0].color==color2 or corner[1].color==color2 or corner[2].color==color2:
                if corner[0].color==color3 or corner[1].color==color3 or corner[2].color==color3:
                    return corner
def solve_f2l_pair(color1, color2):
    if color1=='b':
        solve_centers()
    elif color1=='r':
        solve_centers()
        rotations.y()
    elif color1=='g':
        solve_centers()
        rotations.yTwo()
    elif color1=='o':
        solve_centers()
        rotations.yw()
    corner = find_corner('w', color1, color2)
    edge = find_edge(color1, color2)
    #move corner out of bottom layer if misplaced, then move it to UFR (upper-front-right) position
    if corner[0] in [cube.d1, cube.d7, cube.d9]:
        if corner[0] is cube.d1:
            rotations.f()
            rotations.uw()
            rotations.fw()
            rotations.uw()
        elif corner[0] is cube.d7:
            rotations.l()
            rotations.uTwo()
            rotations.lw()
        elif corner[0] is cube.d9:
            rotations.rw()
            rotations.u()
            rotations.r()
            rotations.u()
        corner = find_corner('w', color1, color2)
    #move edge out of middle layer if misplaced, move with corner to set up standard F2L cases
    if edge[0] in [cube.f4, cube.b6, cube.b4]:
        if edge[0] is cube.f4:
            rotations.u()
            rotations.f()
            rotations.uw()
            rotations.fw()
            rotations.u()
        elif edge[0] is cube.b6:
            rotations.uTwo()
            rotations.l()
            rotations.uw()
            rotations.lw()
        elif edge[0] is cube.b4:
            rotations.rw()
            rotations.u()
            rotations.r()
        corner = find_corner('w', color1, color2)
        edge = find_edge(color1, color2)
    #identify standard F2L cases and solve
    #case where corner is in correct position, possibly incorrect orientation
    if corner[0] is cube.d3:
        #case where edge is in correct position, possibly incorrect orientation
        if edge[0] is cube.f6:
            if edge[0].color==color1:
                if corner[1].color=='w':
                    print("Case 1")
                    move("r u r' u' r u2 r' u' r u r'")
                elif corner[2].color=='w':
                    print("Case 2")
                    move("r u r' u2 r u' r' u r u r'")
            else:
                if corner[0].color=='w':
                    print("Case 3")
                    move("r u' r' u y' r' u2 r u2 r' u r")
                elif corner[1].color=='w':
                    print("Case 4")
                    move("r u' r' u y' r' u' r u' r' u' r")
                elif corner[2].color=='w':
                    print("Case 5")
                    move("r u' r' u2 y' r' u' r u' r' u r")
        else:
            if edge[0] is cube.u4:
                rotations.uw()
            elif edge[0] is cube.u2:
                rotations.uTwo()
            elif edge[0] is cube.u6:
                rotations.u()
            edge = find_edge(color1, color2)
            if corner[0].color=='w':
                if edge[1].color==color1:
                    print("Case 6")
                    move("u r u' r' u' f' u f")
                else:
                    print("Case 7")
                    move("u' r' f' r u r u' r' f")
            elif corner[1].color=='w':
                if edge[1].color==color1:
                    print("Case 8")
                    move("y' r' u' r u r' u' r")
                else:
                    print("Case 9")
                    move("u' r u' r' u r u' r'")
            else:
                if edge[1].color==color1:
                    print("Case 10")
                    move("y' r' u r u' r' u r")
                else:
                    print("Corner:", corner)
                    print("Edge:", edge)
                    print("Case 11")
                    move("u' r u r' u' r u r'")
    else:
        if corner[0] is cube.u3:
            rotations.u()
        elif corner[0] is cube.u1:
            rotations.uTwo()
        elif corner[0] is cube.u7:
            rotations.uw()
        corner = find_corner('w', color1, color2)
        edge = find_edge(color1, color2)
        if corner[0].color=='w':
            if edge[0] is cube.f6:
                if edge[0].color==color1:
                    print("Case 12")
                    move("r2 u r2 u r2 u2 r2")
                else:
                    print("Case 13")
                    move("u' r' f r f' r u' r'")
            elif edge[0] is cube.u6:
                if edge[0].color==color1:
                    print("Case 14")
                    move("r u2 r' u' r u r'")
                else:
                    print("Case 15")
                    move("u' r u r2 f r f' r u' r'")
            elif edge[0] is cube.u2:
                if edge[0].color==color1:
                    print("Case 16")
                    move("u r u2 r' u r u' r'")
                else:
                    print("Case 17")
                    move("f' l' u2 l f")
            elif edge[0] is cube.u4:
                if edge[0].color==color1:
                    print("Case 18")
                    move("r u' r' u2 r u r'")
                else:
                    print("Case 19")
                    move("y' u' r' u2 r u' r' u r")
            else:
                if edge[1].color==color1:
                    print("Case 20")
                    move("y' r' u2 r u r' u' r")
                else:
                    print("Case 21")
                    move("u2 r2 u2 r' u' r u' r2")
        elif corner[1].color=='w':
            if edge[0] is cube.f6:
                if edge[0].color==color1:
                    print("Case 22")
                    move("u' r u2 r' u r u r'")
                else:
                    print("Case 23")
                    move("u f' u' f u' r u r'")
            elif edge[0] is cube.u6:
                if edge[0].color==color1:
                    print("Case 24")
                    move("u' r u' r' u r u r'")
                else:
                    print("Case 25")
                    move("r u' r' u2 f' u' f")
            elif edge[0] is cube.u2:
                if edge[0].color==color1:
                    print("Case 26")
                    move("r u r'")
                else:
                    print("Case 27")
                    move("y' u r' u2 r u2 r' u r")
            elif edge[0] is cube.u4:
                if edge[0].color==color1:
                    print("Case 28")
                    move("u' r u r' u r u r'")
                else:
                    print("Case 29")
                    move("y' u r' u' r u2 r' u r")
            else:
                if edge[0].color==color1:
                    print("Case 30")
                    move("r' u2 r2 u r2 u r")
                else:
                    print("Case 31")
                    move("f r' f' r")
        elif corner[2].color=='w':
            if edge[0] is cube.f6:
                if edge[0].color==color1:
                    print("Case 32")
                    move("u' r u' r' u2 r u' r'")
                else:
                    print("Case 33")
                    move("u' r u r' u f' u' f")
            elif edge[0] is cube.u6:
                if edge[0].color==color1:
                    print("Case 34")
                    move("u r u' r'")
                else:
                    print("Case 35")
                    move("u' r u2 r' u f' u' f")
            elif edge[0] is cube.u2:
                if edge[0].color==color1:
                    print("Case 36")
                    move("u' r u r' u2 r u' r'")
                else:
                    print("Case 37")
                    move("u' r u' r' u f' u' f")
            elif edge[0] is cube.u4:
                if edge[1].color==color1:
                    print("Case 38")
                    move("f' u' f")
                else:
                    print("Case 39")
                    move("u' r u2 r' u2 r u' r'")
            else:
                if edge[0].color==color1:
                    print("Case 40")
                    move("r u r' u2 r u' r' u r u' r'")
                else:
                    print("Case 41")
                    move("y' u r' u r u' r' u' r")
def solve_f2l():
    solve_f2l_pair('b', 'r')
    print_cube()
    solve_f2l_pair('o', 'b')
    print_cube()
    print("\n=== GREEN-ORANGE ===")
    corner = find_corner("w", "g", "o")
    edge = find_edge("g", "o")
    print(corner)
    print(edge)
    solve_f2l_pair('g', 'o')
    corner = find_corner("w", "g", "o")
    edge = find_edge("g", "o")
    print("Corner:", corner)
    print("Edge:", edge)
    print_cube()
    solve_f2l_pair('r', 'g')
