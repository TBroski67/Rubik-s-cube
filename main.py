# Rubik-s-cube
class facelet:
    def __init__(self, color):
        self.color=color
#make objects of facelet class to update piece color more efficiently
#top of cube starts out as yellow (u for up)
u1=facelet('y')
u2=facelet('y')
u3=facelet('y')
u4=facelet('y')
u5=facelet('y')
u6=facelet('y')
u7=facelet('y')
u8=facelet('y')
u9=facelet('y')
#front of cube is blue (f for front)
f1=facelet('b')
f2=facelet('b')
f3=facelet('b')
f4=facelet('b')
f5=facelet('b')
f6=facelet('b')
f7=facelet('b')
f8=facelet('b')
f9=facelet('b')
#right side is red (r for right)
r1=facelet('r')
r2=facelet('r')
r3=facelet('r')
r4=facelet('r')
r5=facelet('r')
r6=facelet('r')
r7=facelet('r')
r8=facelet('r')
r9=facelet('r')
#back is green (b for back)
b1=facelet('g')
b2=facelet('g')
b3=facelet('g')
b4=facelet('g')
b5=facelet('g')
b6=facelet('g')
b7=facelet('g')
b8=facelet('g')
b9=facelet('g')
#left is orange (l for left)
l1=facelet('o')
l2=facelet('o')
l3=facelet('o')
l4=facelet('o')
l5=facelet('o')
l6=facelet('o')
l7=facelet('o')
l8=facelet('o')
l9=facelet('o')
#bottom is white (d for down)
d1=facelet('w')
d2=facelet('w')
d3=facelet('w')
d4=facelet('w')
d5=facelet('w')
d6=facelet('w')
d7=facelet('w')
d8=facelet('w')
d9=facelet('w')
#all the faces of the cube and the pieces that will be affected by rotations
#pieces affected by rotations listed in clockwise order
u_face=[[u1, u2, u3],[u4, u5, u6],[u7, u8, u9]]
u_rotation1=[u1, u2, u3, u6, u9, u8, u7, u4]
u_rotation2=[[l1, l2, l3],[b1, b2, b3],[r1, r2, r3],[f1, f2, f3]]
l_face=[[l1, l2, l3],[l4, l5, l6],[l7, l8, l9]]
l_rotation1=[l1, l2, l3, l6, l9, l8, l7, l4]
l_rotation2=[[d1, d4, d7],[b9, b6, b3],[u1, u4, u7],[b1, b4, b7]]
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
{l1.color} {l2.color} {l3.color} {f1.color} {f2.color} {f3.color} {r1.color} {r2.color} {r3.color} {b1.color} {b2.color} {b3.color}
{l4.color} {l5.color} {l6.color} {f4.color} {f5.color} {f6.color} {r4.color} {r5.color} {r6.color} {b4.color} {b5.color} {b6.color}
{l7.color} {l8.color} {l9.color} {f7.color} {f8.color} {f9.color} {r7.color} {r8.color} {r9.color} {b7.color} {b8.color} {b9.color}
      {d1.color} {d2.color} {d3.color}
      {d4.color} {d5.color} {d6.color}
      {d7.color} {d8.color} {d9.color}""")

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
    if direction==1:
        temp1a=turn2[0,0]
        temp1b=turn2[0,1]
#test that function to display cube works
print_cube()