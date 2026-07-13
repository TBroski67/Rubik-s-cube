import main
#function to perform rotations on cube
def rotate(face, direction):
    if face=='u':
        turn1=main.u_rotation1
        turn2=main.u_rotation2
    elif face=='l':
        turn1=main.l_rotation1
        turn2=main.l_rotation2
    elif face=='f':
        turn1=main.f_rotation1
        turn2=main.f_rotation2
    elif face=='r':
        turn1=main.r_rotation1
        turn2=main.r_rotation2
    elif face=='b':
        turn1=main.b_rotation1
        turn2=main.b_rotation2
    elif face=='d':
        turn1=main.d_rotation1
        turn2=main.d_rotation2
    elif face=='m':
        turn2=main.m_rotation
    elif face=='e':
        turn2=main.e_rotation
    elif face=='s':
        turn2=main.s_rotation
    if face not in ['m','e','s']:
        #use basic steps to simulate rotating cube by switching colors of pieces
        if direction==1:
            #clockwise rotation
            temp_a=turn1[0].color
            temp_b=turn1[1].color
            turn1[0].color=turn1[2].color
            turn1[1].color=turn1[3].color
            turn1[2].color=turn1[4].color
            turn1[3].color=turn1[5].color
            turn1[4].color=turn1[6].color
            turn1[5].color=turn1[7].color
            turn1[6].color=temp_a
            turn1[7].color=temp_b
        else:
            #counterclockwise
            temp_a=turn1[0].color
            temp_b=turn1[1].color
            turn1[0].color=turn1[6].color
            turn1[1].color=turn1[7].color
            turn1[7].color=turn1[5].color
            turn1[6].color=turn1[4].color
            turn1[5].color=turn1[3].color
            turn1[4].color=turn1[2].color
            turn1[3].color=temp_b
            turn1[2].color=temp_a
    temp1a=turn2[0][0].color
    temp1b=turn2[0][1].color
    temp1c=turn2[0][2].color
    if direction==1:
        #clockwise
        turn2[0][0].color=turn2[3][0].color
        turn2[3][0].color=turn2[2][0].color
        turn2[2][0].color=turn2[1][0].color
        turn2[1][0].color=temp1a
        turn2[0][1].color=turn2[3][1].color
        turn2[3][1].color=turn2[2][1].color
        turn2[2][1].color=turn2[1][1].color
        turn2[1][1].color=temp1b
        turn2[0][2].color=turn2[3][2].color
        turn2[3][2].color=turn2[2][2].color
        turn2[2][2].color=turn2[1][2].color
        turn2[1][2].color=temp1c
    else:
        #counterclockwise
        for i in range(0,3):
            turn2[i][0].color=turn2[i+1][0].color
            turn2[i][1].color=turn2[i+1][1].color
            turn2[i][2].color=turn2[i+1][2].color
        turn2[3][0].color=temp1a
        turn2[3][1].color=temp1b
        turn2[3][2].color=temp1c
#individual functions for rotations (w represents ' in cube notation, or a counterclockwise rotation)
def u():
    rotate('u',1)
def uw():
    rotate('u',-1) #-1 indicates counterclockwise rotation
def uTwo():
    #do two u-turns
    u()
    u()
def l():
    rotate('l',1)
def lw():
    rotate('l',-1)
def lTwo():
    l()
    l()
def f():
    rotate('f',1)
def fw():
    rotate('f',-1)
def fTwo():
    f()
    f()
def r():
    rotate('r',1)
def rw():
    rotate('r',-1)
def rTwo():
    r()
    r()
def b():
    rotate('b',1)
def bw():
    rotate('b',-1)
def bTwo():
    b()
    b()
def d():
    rotate('d',1)
def dw():
    rotate('d',-1)
def dTwo():
    d()
    d()
def m():
    rotate('m',1)
def mw():
    rotate('m',-1)
def mTwo():
    m()
    m()
def e():
    rotate('e',1)
def ew():
    rotate('e',-1)
def eTwo():
    e()
    e()
def s():
    rotate('s',1)
def sw():
    rotate('s',-1)
def sTwo():
    s()
    s()