from yutils import *

def test_log():
    y = ylog()
    d = (123, 'info', {'info': 1}, (1,2,3))
    y.info(*d)
    y.warn(*d)
    y.err(*d)


if __name__ == '__main__':
    test_log()