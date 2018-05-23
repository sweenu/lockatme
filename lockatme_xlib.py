from Xlib import X, display
import time

# from lockatme.unlockers.facial_recognition import authenticate
from lockatme.unlockers.facial_recognition import authenticate


def lock_screen(display, screen_nb):
    screen = display.screen(screen_nb)
    root = screen.root
    depth = screen.root_depth
    display_width = screen.width_in_pixels
    display_height = screen.height_in_pixels

    window = root.create_window(0, 0, display_width, display_height,
                                0, depth, window_class=X.CopyFromParent,
                                visual=screen.root_visual,
                                override_redirect=1, background_pixel=screen.black_pixel)

    pixmap = window.create_pixmap(8, 8, 1)
    invisible_cursor = pixmap.create_cursor(pixmap, (0, 0, 0), (0, 0, 0), 0, 0)
    window.change_attributes(cursor=invisible_cursor) # what XDefineCursor does under the hood

    pointer_mask = X.ButtonPressMask | X.ButtonReleaseMask | X.PointerMotionMask
    window.grab_pointer(False, event_mask=pointer_mask,
                        pointer_mode=X.GrabModeAsync, keyboard_mode=X.GrabModeAsync,
                        confine_to=X.NONE, cursor=X.NONE, time=X.CurrentTime)

    window.grab_keyboard(True, pointer_mode=X.GrabModeAsync,
                         keyboard_mode=X.GrabModeAsync, time=X.CurrentTime)
    window.map()


def main_loop():
    while True:
        try:
            if authenticate(): break
        except KeyboardInterrupt:
            continue


if __name__ == '__main__':
    display = display.Display()
    for screen in range(display.screen_count()):
        lock_screen(display, screen)

    display.sync()
    main_loop()
