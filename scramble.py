import rotations
from random import randint

#scramble function
def scramble():
    prev_move = '' #prevent rotationg same face consecutive times
    #letters for each move, indexes used with randint command below
    move_letters = ('u','u','u','l','l','l','f','f','f','r','r','r','b','b','b','d','d','d','m','m','m','e','e','e','s','s','s')
    moves = (rotations.u(), rotations.uw(), rotations.uTwo(),
             rotations.l(), rotations.lw(), rotations.lTwo(),
             rotations.f(), rotations.fw(), rotations.fTwo(),
             rotations.b(), rotations.bw(), rotations.bTwo(),
             rotations.d(), rotations.dw(), rotations.dTwo(),
             rotations.m(), rotations.mw(), rotations.mTwo(),
             rotations.e(), rotations.ew(), rotations.eTwo(),
             rotations.s(), rotations.sw(), rotations.sTwo())
    for i in range(25):
        
        #generate random move
        move = randint(0,20)
        #check for repeating move on same side as last move
        if move_letters[move]!=prev_move:
            prev_move = move_letters[move]
            moves[move]
        else:
            #run loop another time to generate new move
            i-=1