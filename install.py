#!/usr/bin/env python3
"""
Install script for dotfiles
https://github.com/ssbxy/dotfiles

TO DO: 
    - Replace os.system with shutil
    - Add in if path exists statement
    - Change if prompt == to case statement  
"""

import os
import pathlib
import sys


class Install:
    def __init__(self, script, home) -> None:
        self.script = script
        self.home = home

    def install_config(self) -> None:
        config = os.path.join(self.script, 'config')
        dot_config = os.path.join(self.home, '.config')
        prompt = input(f'Installing dotfiles into {dot_config}.\n'\
                        'This will replace current files, continue? (y/n)')

        if prompt == 'y':
            retun_code = os.system(f'cp -rv {config}/* {dot_config}/.')
            if retun_code != 0:
                print(f'Failed to run command. {retun_code}')
                sys.exit(1)
        else:
            print('Files not installed')

        return None

    def install_profile(self) -> None:
        profile = os.path.join(self.script, 'profile')
        prompt = input(f'Installing dotfiles into {self.home}.\n'\
                        'This will repalce current files, continue? (y/n)')
        
        if prompt == 'y':
            return_code = os.system(f'cp -rv {profile}/* {self.home}/.')
            if return_code != 0:
                print(f'Failed to run command. {return_code}')
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
