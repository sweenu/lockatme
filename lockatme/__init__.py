"""
lockatme - a screen lock with facial recognition abilites.
"""
__version__ = '1.0.0-dev'
__author__ = 'Jakub Roztocil'
__licence__ = 'BSD'


class ExitStatus:
    """Exit status code constants."""
    OK = 0
    ERROR = 1

    # 128+2 SIGINT <http://www.tldp.org/LDP/abs/html/exitcodes.html>
    ERROR_CTRL_C = 130


EXIT_STATUS_LABELS = dict(
    (value, key)
    for key, value in ExitStatus.__dict__.items()
    if key.isupper()
)
