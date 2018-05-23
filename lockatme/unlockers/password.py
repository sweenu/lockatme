import getpass
import pamela as pam


def authenticate():
    user = getpass.getuser()
    while True:
        password = getpass.getpass(prompt='')
        try:
            pam.authenticate(user, password)
            return True
        except pam.PAMError:
            continue
