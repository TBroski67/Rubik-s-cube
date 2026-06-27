# Rubik-s-cube
class facelet:
    def __init__(self, color):
        self.color=color
#make objects of facelet class to update piece color more efficiently
#top of cube starts out as yellow (u for up)
u1, u2, u3, u4, u5, u6, u7, u8, u9=facelet('y')
#front of cube is blue (f for front)
f1, f2, f3, f4, f5, f6, f7, f8, f9=facelet('b')
#right side is red (r for right)
r1, r2, r3, r4, r5, r6, r7, r8, r9=facelet('r')
#back is green (b for back)
b1, b2, b3, b4, b5, b6, b7, b8, b9=facelet('g')
#left is orange (l for left)
l1, l2, l3, l4, l5, l6, l7, l8, l9=facelet('o')
#bottom is white (d for down)
d1, d2, d3, d4, d5, d6, d7, d8, d9=facelet('w')
#all the faces of the cube and the pieces that will be affected by rotations
#pieces affected by rotations listed in clockwise order
u_face=[[u1, u2, u3],[u4, u5, u6],[u7, u8, u9]]
u_rotation1=[u1, u2, u3, u6, u9, u8, u7, u4]
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

#displays the cube in an unfolded state
def print_cube():
    print(f"""
      {u1.color} {u2.color} {u3.color}
      {u4.color} {u5.color} {u6.color}
      {u7.color} {u8.color} {u9.color}
""")

#function to perform rotations on cube
def rotate(face, direction):
    if face=='u':
        turn1=u_rotation1
        turn2=u_rotation2
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