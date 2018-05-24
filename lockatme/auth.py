import os
import configparser
from pathlib import Path
from importlib import import_module


def auth_loop():
    config = configparser.ConfigParser(allow_no_value=True)
    config_path = Path.home() / '.config' / 'lockatme/config'
    if os.environ.get('XDG_CONFIG_HOME'):
        config_path = Path(os.environ.get('XDG_CONFIG_HOME')) / 'lockatme/config'

    config.read(config_path)

    try:
        for unlocker in config['unlockers']:
            if os.fork() == 0:
                u = import_module(f'.{unlocker}', 'lockatme.unlockers')
                while True:
                    if u.authenticate():
                        os._exit(0)

        os.waitpid(-1, 0)

    except KeyboardInterrupt:
        # continue
        raise KeyboardInterrupt
