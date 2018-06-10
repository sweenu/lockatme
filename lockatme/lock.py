from Xlib import X, display


def lock_screen(display: display.Display, screen_nb: int):
    screen = display.screen(screen_nb)
    root = screen.root
    display_width = screen.width_in_pixels
    display_height = screen.height_in_pixels

    window = root.create_window(0, 0, display_width, display_height,
                                0, screen.root_depth, window_class=X.CopyFromParent,
                                visual=screen.root_visual,
                                override_redirect=1, background_pixel=screen.black_pixel)

    pixmap = window.create_pixmap(8, 8, 1)
    invisible_cursor = pixmap.create_cursor(pixmap, (0, 0, 0), (0, 0, 0), 0, 0)
    window.change_attributes(cursor=invisible_cursor) # what XDefineCursor does under the hood

    pointer_mask = X.ButtonPressMask | X.ButtonReleaseMask | X.PointerMotionMask
    window.grab_pointer(False, event_mask=pointer_mask,
                        pointer_mode=X.GrabModeAsync, keyboard_mode=X.GrabModeAsync,
                        confine_to=X.NONE, cursor=invisible_cursor, time=X.CurrentTime)

    window.grab_keyboard(True, pointer_mode=X.GrabModeAsync,
                         keyboard_mode=X.GrabModeAsync, time=X.CurrentTime)
    window.map()


def lock(display: display.Display):
    for screen in range(display.screen_count()):
        lock_screen(display, screen)
    display.sync()
