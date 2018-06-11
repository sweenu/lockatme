import os
import configparser
from importlib import import_module
from pathlib import Path
from threading import Thread, Event


def get_modules_auth_functions():
    if os.environ.get('XDG_CONFIG_HOME'):
        config_home = Path(os.environ.get('XDG_CONFIG_HOME'))
    else:
        config_home = Path.home() / '.config' 

    config_dir = config_home / 'lockatme'
    config_dir.mkdir(exist_ok=True)

    config_path = config_dir / 'config'

    try:
        config_file = config_path.open()
    except FileNotFoundError:
        config_path.write_text('[unlockers]\npassword')
        config_file = config_path.open()
    finally:
        config = configparser.ConfigParser(allow_no_value=True)
        config.read_file(config_file)
        config_file.close()

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
