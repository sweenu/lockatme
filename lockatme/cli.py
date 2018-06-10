import os

from click import command, option, argument
from Xlib.display import Display

from .lock import lock
from .auth import auth_loop


@command()
def main():
    """
    lockatme: Modulable screen locker.
    """
    display = Display()
    lock(display) 
    auth_loop()
    os._exit(0)
