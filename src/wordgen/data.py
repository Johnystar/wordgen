from typing  import Dict
from pathlib import Path
from appdirs import user_config_dir
import os

def get_available_files(type:str) -> Dict[str, str]:
    built_in = Path(__file__).parent / "data" / type
    user_defined = Path(user_config_dir(
        appname="wordgen",
        appauthor="octelly",
        roaming=True
    )) / type

    found = {}

    for file in [built_in / file
                 for file in os.listdir(built_in)
                 if os.path.isfile(built_in / file)]:
        found[os.path.basename(file).split('.')[0]] = file
    try:
        for file in [user_defined / file
                     for file in os.listdir(user_defined)
                     if os.path.isfile(user_defined / file)]:
            found[os.path.basename(file).split('.')[0]] = file
    except FileNotFoundError:
        pass

    return found

def parse_file(path:str) -> list[str]:
    output = []

    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.split('\n')[0]

            line = line.split('#')[0]
            line = line.replace(' ', '')

            if line == '': continue

            output.append(line)

    return output

