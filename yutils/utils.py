from uuid import uuid4
from datetime import datetime
import os
import sys
import re
import os
import sys
import time
import json
import base64
import traceback
import subprocess as sp


if 'dirs' not in __builtins__.keys():
    __builtins__['dirs'] = []


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


def is_linux():
    return sys.platform == 'linux'


if is_linux():
    import fcntl


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
                self.lock = fileLock(filename=filename + '.lck')
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


if "logger" not in __builtins__.keys():
    __builtins__["logger"] = ylog()


def info(*args):
    __builtins__["logger"].info(*args)


def warn(*args):
    __builtins__["logger"].warn(*args)


def err(*args):
    __builtins__["logger"].err(*args)


def is_windows():
    return sys.platform == 'win32'


def python():
    if is_windows():
        return 'python'
    return runok('which python3')


def __run(cmd):
    if is_windows():
        cmd = cmd.replace('sudo', '').strip()
    return sp.getstatusoutput(cmd)


def sys_run(cmd):
    os.system(cmd)


def run(cmd) -> str:
    info(f'{green("-")} {cmd}')
    code, output = __run(cmd)
    if code != 0:
        warn(code, output)
    return output


def runex(cmd) -> tuple:
    info(f'{green("-")} {cmd}')
    code, output = __run(cmd)
    if code != 0:
        warn(code, output)
    return code, output


def runok(cmd) -> tuple:
    info(f'ensure: {cmd}')
    code, output = __run(cmd)
    if code != 0:
        err(code, output)
        assert code == 0, f'{cmd} failed'
    return code, output


def pexist(path):
    return os.path.exists(path)


def pjoin(*args):
    return os.path.join(*args)


def home():
    return os.environ["HOME"]


def me():
    return os.environ["USER"]


def check_file(file_name, package_name):
    code, output = runex(f'which {file_name}')
    if code != 0:
        warn(f'not found {file_name}, try to install {package_name}')
        code, output = runex(f'sudo apt install -y {package_name}')
        if code != 0:
            warn(output)
            err(f'auto install {package_name} failed')
            exit(-1)
        code, output = runex(f'which {file_name}')
        if code != 0:
            warn(output)
            err(f'auto install {package_name} failed')
            exit(-1)


def clone(url, depth=1, dst_dir='.'):
    dst_dir = dst_dir.replace('~', home())
    if dst_dir != '.' and pexist(dst_dir):
        run(f'rm -rf {dst_dir}')

    def _clone():
        runok(f'git clone {url} --depth={depth} {dst_dir}')
    retry(_clone)


def cp(source, dest, args=''):
    runok(f'cp {args} {source} {dest}')


def mv(source, dest, args=''):
    runok(f'mv {args} {source} {dest}')


def lns(source, dest):
    # dest -> source
    dest = dest.replace('~', home())
    if pexist(dest):
        backup(dest)
    source = os.path.realpath(source)
    assert pexist(source), f'{source} not exist'
    runok(f'ln -s {source} {dest}')


def backup(source):
    if not pexist(source):
        return
    source = source.replace('~', home())
    if is_windows():
        cmd = 'move'
    else:
        cmd = 'mv'
    runok(f'{cmd} {source} {source}.bak')


def curdir():
    return os.path.realpath(os.curdir)


def dirname(path):
    return os.path.dirname(path)


def pushd(dir=None):
    if not dir:
        __builtins__['dirs'].append(curdir())
    else:
        assert pexist(dir), f'{dir} not exist'
        __builtins__['dirs'].append(os.path.realpath(dir))


def cd(path, show=True):
    assert pexist(path), f'{path} not exist'
    if os.path.isfile(path):
        os.chdir(dirname(path))
    else:
        os.chdir(path)
    if show:
        info(f'cd {path}')


def popd():
    assert len(__builtins__['dirs']
               ) > 0, 'not dir in __builtins__.dirs'
    d = __builtins__['dirs'].pop()
    cd(d)
    return d


def repo_root_dir(path):
    assert pexist(path), f"{path} not exist"
    real_path = os.path.realpath(path)
    while real_path != '/':
        if pexist(pjoin(real_path, '.git')):
            return real_path
        real_path = dirname(real_path)
    assert False, f'{path} not in git repo'


def retry(func, times=5, interval=3):
    res = None
    for t in range(1, times + 1):
        try:
            res = func()
        except Exception as e:
            traceback.print_exc()
            warn(f'run {func} failed {t} time(s)')
            info(f'wait {interval} second(s)')
            time.sleep(interval)
            continue
        break
    return res


def dump_json(d: dict):
    return '\n' + json.dumps(d, indent=4, separators=',:', ensure_ascii=True)
