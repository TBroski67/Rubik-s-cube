import rotations
from random import randint

#scramble function
def scramble():
    moves = (rotations.u, rotations.uw, rotations.uTwo,
             rotations.l, rotations.lw, rotations.lTwo,
             rotations.f, rotations.fw, rotations.fTwo,
             rotations.r, rotations.rw, rotations.rTwo,
             rotations.b, rotations.bw, rotations.bTwo,
             rotations.d, rotations.dw, rotations.dTwo,
             rotations.m, rotations.mw, rotations.mTwo,
             rotations.e, rotations.ew, rotations.eTwo,
             rotations.s, rotations.sw, rotations.sTwo)
    move_count = 0
    while move_count<25:
        #generate random move
        move = randint(0,26)
        moves[move]()
        move_count+=1
