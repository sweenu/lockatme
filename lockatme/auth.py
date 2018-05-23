import os
import sys
from pathlib import Path
import configparser


def auth_loop():
    config = configparser.ConfigParser(allow_no_value=True)
    config_path = Path.home() / '.config' / 'lockatme/config'
    if os.getenv('XDG_CONFIG_HOME'):
        config_path = Path(os.getenv('XDG_CONFIG_HOME')) / 'lockatme/config'

    config.read(config_path)

    while True:
        try:
            for module in config['modules']:
                exec(f'from lockatme.unlockers.{module} import authenticate')
                pid = os.fork()
                if pid == 0:
                    if authenticate():  # noqa
                        sys.exit(0)
                else:
                    os.wait()

        except KeyboardInterrupt:
            # continue
            raise KeyboardInterrupt
