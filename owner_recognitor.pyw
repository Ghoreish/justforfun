import time

from pynput import keyboard
from pynput.keyboard import Key, Controller
import os

global inputs
global ave
inputs = []
ave = 0


def check_det(l):
    print(l)
    if len(l) < 2:
        return None
    size = len(l)
    res = (l[-1] - l[0]) / size
    return res


def lock_the_system():
    os.system('rundll32.exe user32.dll,LockWorkStation')


def calc_dif(x, y):
    if x == None or y == None:
        return 0
    if x > y:
        res = (x - y) / x * 100
    else:
        res = (y - x) / y * 100
    return res


def on_press(key):
    global inputs
    global ave
    try:
        if key.char in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
            inputs.append(time.time())
        else:
            if len(inputs) < 2:
                inputs = []
                return None
            det = check_det(inputs)
            if ave == 0:
                ave = det
                return None
            x = calc_dif(ave, det)
            if x > 60:
                lock_the_system()
            inputs = []
    except:
        if len(inputs) < 2:
            inputs = []
            return None
        det = check_det(inputs)
        if ave == 0:
            ave = det
            return None
        x = calc_dif(ave, det)
        if x > 60:
            lock_the_system()
        inputs = []


listener = keyboard.Listener(on_press=on_press)
listener.start()
while True:
    pass
