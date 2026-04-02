# Rubik-s-cube
from pynput import keyboard
#all the faces of the cube and the pieces that will be affected by rotations
u_face=[['y','y','y'],['y','y','y'],['y','y','y']]
u_rotation1=['y','y','y','y','y','y','y','y']
u_rotation2=[['o','o','o'],['g','g','g'],['r','r','r'],['b','b','b']]
l_face=[['o','o','o'],['o','o','o'],['o','o','o']]
l_rotation1=['o','o','o','o','o','o','o','o']
l_rotation2=[['w','w','w'],['g','g','g'],['y','y','y'],['b','b','b']]
f_face=[['b','b','b'],['b','b','b'],['b','b','b']]
f_rotation1=['b','b','b','b','b','b','b','b']
f_rotation2=[['w','w','w'],['o','o','o'],['y','y','y'],['r','r','r']]
r_face=[['r','r','r'],['r','r','r'],['r','r','r']]
r_rotation1=['r','r','r','r','r','r','r','r']
r_rotation2=[['w','w','w'],['b','b','b'],['y','y','y'],['g','g','g']]
b_face=[['g','g','g'],['g','g','g'],['g','g','g']]
b_rotation1=['g','g','g','g','g','g','g','g']
b_rotation2=[['w','w','w'],['r','r','r'],['y','y','y'],['o','o','o']]
d_face=[['w','w','w'],['w','w','w'],['w','w','w']]
d_rotation1=['w','w','w','w','w','w','w','w']
d_rotation2=[['o','o','o'],['b','b','b'],['r','r','r'],['g','g','g']]
m_rotation=[['b','b','b'],['y','y','y'],['g','g','g'],['w','w','w']]
e_rotation=[['o','o','o'],['g','g','g'],['r','r','r'],['b','b','b']]
s_rotation=[['w','w','w'],['o','o','o'],['y','y','y'],['r','r','r']]
side_list=[u_face, l_face, f_face, r_face, b_face, d_face]
def rotate(face, direction):
    if face=='u':
        turn1=u_rotation1
        turn2=u_rotation2
        no_update_face=d_face
    elif face=='l':
        turn1=l_rotation1
        turn2=l_rotation2
    elif face=='f':
        turn1=f_rotation1
        turn2=f_rotation2
    elif face=='r':
        turn1=r_rotation1
        turn2=r_rotation2
    elif face=='b':
        turn1=b_rotation1
        turn2=b_rotation2
    elif face=='d':
        turn1=d_rotation1
        turn2=d_rotation2
    elif face=='m':
        turn2=m_rotation
    elif face=='e':
        turn2=e_rotation
    elif face=='s':
        turn2=s_rotation
    temp1=turn2[-1]
    if face not in ['m','e','s']:
        if direction==1:
            temp_a=turn1[-1]
            temp_b=turn1[-2]
            turn1[0]=turn1[2]
            turn1[1]=turn1[3]
            turn1[2]=turn1[4]
            turn1[3]=turn1[5]
            turn1[4]=turn1[6]
            turn1[5]=turn1[7]
            turn1[6]=temp_a
            turn1[7]=temp_b
