from main import rotate
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