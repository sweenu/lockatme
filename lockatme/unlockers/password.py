import time
import getpass

import pamela as pam


def authenticate():
    user = getpass.getuser()
    password = getpass.getpass(prompt='')
    if pam.authenticate(user, password):
        return True

    time.sleep(15)
    return True
