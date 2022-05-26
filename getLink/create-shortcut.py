# windows only
import sys
import json
from turtle import update
from uuid import uuid4
from tqdm import tqdm
from subprocess import *
import os

if sys.platform != 'win32':
    print('windows only!')
    exit(0)

import pythoncom
from win32com.shell import shell


basedir = "D:\\programs\\"  # create short cut in this folder
if not os.path.exists(basedir):
    os.mkdir(basedir)


def _create_shortcut(filename):
    # create short cut
    try:
        dirname = os.path.dirname(filename)
        lnkname = os.path.basename(filename)
        lnkname = lnkname[:lnkname.rfind('.')]
        lnkname = os.path.join(basedir, lnkname)+'.lnk'

        shortcut = pythoncom.CoCreateInstance(
            shell.CLSID_ShellLink, None,
            pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
        shortcut.SetPath(filename)

        shortcut.SetWorkingDirectory(dirname)  # 设置快捷方式的起始位置, 不然会出现找不到辅助文件的情况
        shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(lnkname, 0)

        return True
    except Exception as e:
        print(e.args)
        return False


def get_output(data):
    result = data.decode().split('\r\n')
    for r in result[:]:
        if len(r) == 0:
            result.remove(r)
    return result


def get_path(program_name):
    # use everything's es get file abspath
    # please make sure everything is open and es is in system path
    command = f'es -regex "\\\\{program_name}$"'
    p = Popen(command, stdout=PIPE, stderr=PIPE)
    p.wait()
    errMsg = p.stderr.read().decode()
    if len(errMsg) != 0:
        # error occured
        print('error', errMsg)
        exit(-1)
    return get_output(p.stdout.read())


def create_shortcut():
    # return quickCommand explains
    with open('programs.txt', 'r') as f:
        # get needed programs
        programs = f.readlines()
    programs = [d.strip('\n') for d in programs]
    # create shortcut in refered dir
    for program in tqdm(programs):
        for result in get_path(program):
            _create_shortcut(result)
    return (['(auto inject)auto start ' + p for p in programs],
            [os.path.join(basedir, p[:p.rfind('.')]) for p in programs])


def update_quickCommand(new_explains, lnk_dirs):
    # generate new quickCommand.json
    # can import utools quickCommand plugin
    with open('quickCommand.json', 'r') as f:
        d = json.load(f)
    origin_explains = [d[key]['features']['explain'] for key in d.keys()]
    for e, l in zip(new_explains, lnk_dirs):
        if e not in origin_explains:
            key = str(uuid4())
            link_dir = l.replace('\\', '\\\\')
            d[key] = {
                "features": {
                    "code": key,
                    "explain": e,
                    "cmds": [
                        e.split()[-1]
                    ],
                    "icon": "logo/quickcommand.png",
                    "platform": [
                        "win32",
                    ]
                },
                "program": "quickcommand",
                "cmd": f'open("{link_dir}")',
                "output": "ignore",
                "hasSubInput": False,
                "scptarg": "",
                "charset": {
                    "scriptCode": "",
                    "outputCode": ""
                },
                "tags": []
            }
    with open('quickCommand_modified.json', 'w') as f:
        json.dump(d, fp=f, indent=4, separators=',:')


a, b = create_shortcut()
update_quickCommand(a, b)
