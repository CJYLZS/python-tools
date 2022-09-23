import os
import sys
sys.path.append(os.path.realpath(__file__))
from cmd import *
from utils import *

def test_log():
    d = (123, 'info', {'info': 1}, (1,2,3), test_log)
    info(*d)
    warn(*d)
    err(*d)

def test_cmd():
    pass


if __name__ == '__main__':
    test_log()