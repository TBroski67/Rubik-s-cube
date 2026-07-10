from pynput import keyboard
import rotations

def on_press(key):
    if hasattr(key, 'char') and key.char == 'u':
        rotations.u()
    elif hasattr(key, 'char') and key.char == 'l':
        rotations.l()
    elif hasattr(key, 'char') and key.char == 'f':
        rotations.f()
    elif hasattr(key, 'char') and key.char == 'r':
        rotations.r()
    elif hasattr(key, 'char') and key.char == 'b':
        rotations.b()
    elif hasattr(key, 'char') and key.char == 'd':
        rotations.d()
    elif hasattr(key, 'char') and key.char == 'm':
        rotations.m()
    elif hasattr(key, 'char') and key.char == 'e':
        rotations.e()
    elif hasattr(key, 'char') and key.char == 's':
        rotations.s()