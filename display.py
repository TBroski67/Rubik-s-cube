import cube
import os
#displays the cube in an unfolded state
def print_cube():
    #print individual facelets of cube
    print(f"""
      {cube.u1.color} {cube.u2.color} {cube.u3.color}
      {cube.u4.color} {cube.u5.color} {cube.u6.color}
      {cube.u7.color} {cube.u8.color} {cube.u9.color}
{cube.l1.color} {cube.l2.color} {cube.l3.color} {cube.f1.color} {cube.f2.color} {cube.f3.color} {cube.r1.color} {cube.r2.color} {cube.r3.color} {cube.b1.color} {cube.b2.color} {cube.b3.color}
{cube.l4.color} {cube.l5.color} {cube.l6.color} {cube.f4.color} {cube.f5.color} {cube.f6.color} {cube.r4.color} {cube.r5.color} {cube.r6.color} {cube.b4.color} {cube.b5.color} {cube.b6.color}
{cube.l7.color} {cube.l8.color} {cube.l9.color} {cube.f7.color} {cube.f8.color} {cube.f9.color} {cube.r7.color} {cube.r8.color} {cube.r9.color} {cube.b7.color} {cube.b8.color} {cube.b9.color}
      {cube.d1.color} {cube.d2.color} {cube.d3.color}
      {cube.d4.color} {cube.d5.color} {cube.d6.color}
      {cube.d7.color} {cube.d8.color} {cube.d9.color}""")
def clear():
    #clear console using os module
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')