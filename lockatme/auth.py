import os
import configparser
from importlib import import_module
from pathlib import Path
from threading import Thread, Event


def get_modules_auth_functions():
    config = configparser.ConfigParser(allow_no_value=True)
    config_path = Path.home() / '.config' / 'lockatme/config'
    if os.environ.get('XDG_CONFIG_HOME'):
        config_path = Path(os.environ.get('XDG_CONFIG_HOME')) / 'lockatme/config'

    config.read(config_path)

    auth_functions = []
    for unlocker in config['unlockers']:
        u = import_module(f'.{unlocker}', 'lockatme.unlockers')
        auth_functions.append(u.authenticate)

    return auth_functions


def add_event(func, event):
    def f():
        func()
        event.set()

    return f


def auth_loop():
    authenticated = Event()
    auth_functions = get_modules_auth_functions()

    for auth_function in auth_functions:
        authenticate = add_event(auth_function, authenticated)
        t = Thread(target=authenticate)
        t.start()

    authenticated.wait()
