import os
import sys
from uuid import uuid4
from datetime import datetime

def red(str):
    return f'\033[31m{str}\033[0m'


def green(str):
    return f'\033[32m{str}\033[0m'


def yellow(str):
    return f'\033[33m{str}\033[0m'


def now(format='%y%m%d-%H:%M:%S'):
    return datetime.strftime(datetime.now(), format)


def create_empty_file(filename):
    if '/' in filename:
        dirname = os.path.dirname(os.path.realpath(dirname))
        if not os.path.exists(dirname):
            os.makedirs(dirname)
    with open(filename, 'w'):
        pass


def rm(filename):
    os.remove(filename)


def get_tmp_file():
    assert sys.platform == 'linux', 'only linux'
    filename = f'/tmp/tmp_{str(uuid4())}'
    create_empty_file(filename)
    return filename
