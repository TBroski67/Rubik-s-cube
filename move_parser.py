import rotations
def move(sequence):
    move_list = sequence.lower().split()
    for move in move_list:
        match move:
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
