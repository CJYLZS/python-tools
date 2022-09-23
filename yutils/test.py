import os
import sys
sys.path.append(os.path.realpath(__file__))
from cmd import *
from utils import *


def test_log():
    d = (123, 'info', {'info': 1}, (1, 2, 3), test_log)
    info(*d)
    warn(*d)
    err(*d)


def test_cmd():
    pushd()
    cd(repo_root_dir(__file__))
    code, _ = runex('./cmd test')
    assert code != 0
    code, _ = runex('./cmd test -a -b kkk')
    assert code != 0
    assert run(
        './cmd test -a -b 111 -c kkk') == "a<class 'int'>111<class 'str'>kkk", ""
    assert run(
        './cmd test -a -b -111 -c') == "a<class 'int'>-111<class 'str'>fuck", ""
    assert run(
        './cmd test -a -b -c kkk') == "a<class 'int'>888<class 'str'>kkk", ""
    assert run('./cmd test -a -b -c ') == "a<class 'int'>888<class 'str'>fuck", ""
    assert run('./cmd test -abc') == "a<class 'int'>888<class 'str'>fuck", ""
    assert run(
        './cmd test -abc 998 kkl') == "a<class 'int'>998<class 'str'>kkl", ""
    assert run('./cmd test -ac kkl') == "a<class 'str'>kkl", ""
    assert run(
        './cmd test --aa --bb 111 --cc kkk') == "a<class 'int'>111<class 'str'>kkk", ""
    assert run(
        './cmd test --aa --bb -111 --cc') == "a<class 'int'>-111<class 'str'>fuck", ""
    assert run(
        './cmd test --aa --bb --cc kkk') == "a<class 'int'>888<class 'str'>kkk", ""
    assert run(
        './cmd test --aa --bb --cc ') == "a<class 'int'>888<class 'str'>fuck", ""
    popd()


if __name__ == '__main__':
    test_log()
    test_cmd()
