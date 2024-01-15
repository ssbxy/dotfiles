#!/usr/bin/env python3
"""
Install script for dotfiles
https://github.com/ssbxy/dotfiles
"""

import os
import pathlib
import sys

class Install:
    def __init__(self, script, home):
        self.script = script
        self.home = home

    def install_config(self) -> None:
        config = os.path.join(self.script, 'config')
        dot_config = os.path.join(self.home, '.config')
        print(f'{config}')
        print(f'{dot_config}')
        
        prompt = input('Installing .config files, this will replace current files. Continue (y/n)')
        if prompt == 'y':
            retun_code = os.system(f'cp -rv {config}/* {dot_config}/.')
            if retun_code != 0:
                print(f'Failed to run command. {retun_code}')
                sys.exit(1)
        else:
            print('.config files not installed')
        return None

    def install_profile(self) -> None:
        profile = os.path.join(self.script, 'profile')
        prompt = input(f'Installing files into {self.home}, this will repalce current files. Continue (y/n)')
        if prompt == 'y':
            return_code = os.system(f'cp -rv {profile}/* {self.home}/.')
            if return_code != 0:
                print(f'Fauled to run command. {return_code}')
                sys.exit(1)
        else:
            print('Files not installed')
        return None


def main() -> int:
    script_directory = pathlib.Path().resolve()
    home_directory = pathlib.Path.home()

    dotfiles = Install(script_directory, home_directory)
    dotfiles.install_config()
    dotfiles.install_profile()

    return 0

if __name__ == '__main__':
    sys.exit(main())
