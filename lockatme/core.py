import os
from Xlib import display

from .lock import lock_screen
from .auth import auth_loop


def main():
    dpy = display.Display()
    for screen in range(dpy.screen_count()):
        lock_screen(dpy, screen)
    dpy.sync()

    auth_loop()
    os._exit(0)
