import sys
from Xlib import display

from .lock import lock_screen
from .auth import auth_loop
from .unlockers.password import authenticate


def main(args=sys.argv[1:0]):
    dpy = display.Display()
    for screen in range(dpy.screen_count()):
        lock_screen(dpy, screen)
    dpy.sync()

    auth_loop()
