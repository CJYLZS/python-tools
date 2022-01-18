# windows only
import sys
if sys.platform != 'win32':
    print('windows only!')
    exit(0)
from tqdm import tqdm
from subprocess import *
import os
import pythoncom
from win32com.shell import shell


basedir = "C:\\Users\\YLZS\\Desktop\\programs\\" # create short cut in this folder
if not os.path.exists(basedir):
    os.mkdir(basedir)

def create_shortcut(filename):
    # create short cut
    try:
        dirname = os.path.dirname(filename)
        lnkname = os.path.join(basedir, os.path.basename(filename))+'.lnk'

        shortcut = pythoncom.CoCreateInstance(
            shell.CLSID_ShellLink, None,
            pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
        shortcut.SetPath(filename)

        shortcut.SetWorkingDirectory(dirname) # 设置快捷方式的起始位置, 不然会出现找不到辅助文件的情况
        shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(lnkname, 0)

        return True
    except Exception as e:
        print(e.args)
        return False

def get_output(data):
    result =  data.decode().split('\r\n')
    for r in result[:]:
        if len(r) == 0:
            result.remove(r)
    return result

def get_path(program_name):
    # use everything's es get file abspath
    command = f'es -regex "\\\\{program_name}$"'
    p = Popen(command, stdout=PIPE, stderr=PIPE)
    p.wait()
    return get_output(p.stdout.read())



with open('programs.txt', 'r') as f:
    # get needed programs
    programs = f.readlines()
programs = [d.strip('\n') for d in programs]
# create shortcut in refered dir
for program in tqdm(programs):
    for result in get_path(program):
        create_shortcut(result)