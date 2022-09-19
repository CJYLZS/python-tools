import os
import sys
import fcntl
from utils import *

# if sys.platform == 'win32':
#     print('fuck windows')
# else:
#     uname = subprocess.getoutput('whoami')
#     python_dir = os.path.join('/home', uname, '.py/')
#     if not os.path.exists(python_dir):
#         os.makedirs(python_dir)
#     save_dir = os.path.join('/home', uname, '.py/yutils/')
#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)



class fileLock:
    def __init__(self, filename=None) -> None:
        if not filename:
            self.filename = get_tmp_file()
        else:
            self.filename = filename
            create_empty_file(self.filename)
        self.__f = None

    def __del__(self):
        rm(self.filename)

    def lock(self):
        assert self.__f is None, 'dead lock'
        self.__f = open(self.filename, 'r+')
        fcntl.flock(self.__f.fileno(), fcntl.LOCK_EX)

    def unlock(self):
        if not self.__f:
            return
        fcntl.flock(self.__f.fileno(), fcntl.LOCK_UN)
        self.__f.close()
        self.__f = None

    def __enter__(self):
        self.lock()

    def __exit__(self, *args):
        self.unlock()


class ylog:
    def __init__(self, filename=None, lock=False) -> None:
        self.filename = filename
        if self.filename and not os.path.exists(self.filename):
            create_empty_file(self.filename)

        if lock and sys.platform == 'linux':
            if filename:
                self.lock = fileLock(filename=filename+'.lck')
            else:
                self.lock = fileLock()
        else:
            self.lock = None

    def __print(self, _str):
        if self.filename:
            with open(self.filename, 'a') as f:
                f.write(_str + '\n')
        else:
            print(_str)

    def info(self, *args):
        args = [f'{arg}' for arg in args]
        if not self.filename:
            _str = f'{now()}|{green("INFO")} {" ".join(args)}'
        else:
            _str = f'{now()}|{"INFO"} {" ".join(args)}'
        if self.lock is not None:
            with self.lock:
                self.__print(_str)
        else:
            self.__print(_str)

    def warn(self, *args):
        args = [f'{arg}' for arg in args]
        if not self.filename:
            _str = f'{now()}|{yellow("WARN")} {" ".join(args)}'
        else:
            _str = f'{now()}|{"WARN"} {" ".join(args)}'
        if self.lock is not None:
            with self.lock:
                self.__print(_str)
        else:
            self.__print(_str)

    def err(self, *args):
        args = [f'{arg}' for arg in args]
        if not self.filename:
            _str = f'{now()}|{red("ERROR")} {" ".join(args)}'
        else:
            _str = f'{now()}|{"ERROR"} {" ".join(args)}'
        if self.lock is not None:
            with self.lock:
                self.__print(_str)
        else:
            self.__print(_str)
