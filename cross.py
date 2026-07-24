import cube
import rotations
#function to turn centers into position
def solve_centers():
    #move white center to bottom of cube
    if cube.u5.color=='w':
        rotations.xTwo
    elif cube.l5.color=='w':
        rotations.zw()
    elif cube.f5.color=='w':
        rotations.xw()
    elif cube.r5.color=='w':
        rotations.z()
    elif cube.b5.color=='w':
        rotations.x()
    #move middle layer centers into position
    if cube.l5.color=='b':
        rotations.yw()
    elif cube.r5.color=='b':
        rotations.y()
    elif cube.b5.color=='b':
        rotations.yTwo()
#function to locate edge
def find_edge(color1, color2):
    edge_list = [(cube.u2, cube.b2),
                 (cube.u4, cube.l2),
                 (cube.u8, cube.f2),
                 (cube.u6, cube.r2),
                 (cube.b6, cube.l4),
                 (cube.f4, cube.l6),
                 (cube.f6, cube.r4),
                 (cube.b4, cube.r6),
                 (cube.d4, cube.l8),
                 (cube.d2, cube.f8),
                 (cube.d6, cube.r8),
                 (cube.d8, cube.b8)]
    for edge in edge_list:
        #test if both colors of edge are in an edge's location
        if edge[0].color==color1 or edge[1].color==color1:
            if edge[0].color==color2 or edge[1].color==color2:
                return (edge[0], edge[1])
#function to turn edge into correct position
def solve_edge(other_color):
    #rotate cube to help simplify cases for each edge
    if other_color=='b':
        solve_centers()
    elif other_color=='r':
        solve_centers()
        rotations.y()
    elif other_color=='g':
        solve_centers()
        rotations.yTwo()
    elif other_color=='o':
        solve_centers()
        rotations.yw()
    edge = find_edge('w', other_color)
    if edge[0].color=='w':
        if edge[1] is cube.l8:
            rotations.l()
            rotations.dw()
            rotations.lw()
            rotations.d()
        elif edge[1] is cube.r8:
            rotations.r()
            rotations.d()
            rotations.rw()
            rotations.dw()
        elif edge[1] is cube.b8:
            rotations.b()
            rotations.dTwo()
            rotations.bw()
            rotations.dTwo()
        elif edge[1] is cube.l6:
            rotations.dw()
            rotations.l()
            rotations.d()
        elif edge[1] is cube.l4:
            rotations.dw()
            rotations.lw()
            rotations.d()
        elif edge[1] is cube.r6:
            rotations.d()
            rotations.r()
            rotations.dw()
        elif edge[1] is cube.r4:
            rotations.d()
            rotations.rw()
            rotations.dw()
        elif edge[1] is cube.f2:
            rotations.fTwo()
        elif edge[1] is cube.l2:
            rotations.uw()
            rotations.fTwo()
        elif edge[1] is cube.r2:
            rotations.u()
            rotations.fTwo()
        elif edge[1] is cube.b2:
            rotations.uTwo()
            rotations.fTwo()
    elif edge[1].color=='w':
        if edge[0] is cube.d2:
            rotations.f()
            rotations.dw()
            rotations.l()
            rotations.d()
        elif edge[0] is cube.d4:
            rotations.lw()
            rotations.fw()
        elif edge[0] is cube.d8:
            rotations.b()
            rotations.d()
            rotations.r()
            rotations.dw()
        elif edge[0] is cube.d6:
            rotations.r()
            rotations.f()
        elif edge[0] is cube.f4:
            rotations.fw()
        elif edge[0] is cube.f6:
            rotations.f()
        elif edge[0] is cube.b4:
            rotations.dTwo()
            rotations.bw()
            rotations.dTwo()
        elif edge[0] is cube.b6:
            rotations.dTwo()
            rotations.b()
            rotations.dTwo()
        elif edge[0] is cube.u8:
            rotations.uw()
            rotations.rw()
            rotations.f()
            rotations.r()
        elif edge[0] is cube.u6:
            rotations.rw()
            rotations.f()
            rotations.r()
        elif edge[0] is cube.u2:
            rotations.u()
            rotations.rw()
            rotations.f()
            rotations.r()
        elif edge[0] is cube.u4:
            rotations.l()
            rotations.fw()
            rotations.lw()
def solve_cross():
    for i in ['b', 'r', 'g', 'o']:
        solve_edge(i)
