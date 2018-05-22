import xcffib
import xcffib.xproto
import xcffib.randr


def get_nb_screens(conn):
    return conn.get_setup().root_len

def lock_screen(conn, screen):
    setup = conn.get_setup()
    root = setup.roots[0].root
    depth = setup.roots[0].root_depth
    disp_width = conn.randr.Get
    disp_height =

    mask = 
    conn.core.CreateWindow(depth, conn.generate_id(), root,
                           0, 0, disp_width, disp_height, 0,
                           WindowClass.InputOutput,
                           visual,
                           CW.BackPixel | CW.EventMask,
                           [ white, EventMask.ButtonPress | EventMask.EnterWindow | EventMask.LeaveWindow | EventMask.Exposure ])

if __name__ == '__main__':
    conn = xcffib.connect()
    lock_screen(conn
