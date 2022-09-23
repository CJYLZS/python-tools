import os
import sys
sys.path.append(os.path.realpath(__file__))
from utils import *


class cmd_base():
    opt_args = {
        "help": ("h", "help", "print help", "", False),
    }
    opt_short_args = {
        "h": ("h", "help", "print help", "", False),
    }
    sys_args = {}
    sys_short_args = {}
    sys_targets = []

    def __get_arg_short(self, arg):
        return arg[0]

    def __get_arg_long(self, arg):
        return arg[1]

    def __get_arg_help(self, arg):
        return arg[2]

    def __get_arg_default_value(self, arg):
        return arg[3]

    def __get_arg_required(self, arg):
        return arg[4]

    def __is_long_name(self, name):
        return len(name) > 1

    def __is_short_name(self, name):
        return len(name) == 1

    def __init_dirs(self):
        self.root_dir = repo_root_dir(".")
        cd(self.root_dir, show=False)
        self.cmd_dir = os.path.realpath(dirname(__file__))
        self.cmds_dir = pjoin(self.root_dir, 'cmds')
        if not pexist(self.cmds_dir):
            os.mkdir(self.cmds_dir)
        sys.path.append(self.cmds_dir)

    def __init_opt_args(self, options_argv):
        for arg in options_argv:
            assert len(
                arg) == 5, "argv: ([short opt],  [long opt], [help info], [default value], [required])"
            long_name = self.__get_arg_long(arg)
            assert len(long_name) > 1, f'long name length must more than 1'
            assert long_name not in self.opt_args.keys(), f"{arg} duplicate"
            self.opt_args[long_name] = arg
            short_name = self.__get_arg_short(arg)
            if len(short_name) > 0:
                self.opt_short_args[short_name] = arg

    def __is_opt(self, _str):
        rule1 = re.compile(r'-[a-zA-Z]+')
        rule2 = re.compile(r'--[a-zA-Z]+')
        return len(re.sub(rule1, "", _str)) == 0 or len(re.sub(rule2, "", _str)) == 0

    def __init_sys_argv(self):

        def add_to_sys_arg(arg, value):
            self.sys_args[self.__get_arg_long(arg)] = value
            self.sys_short_args[self.__get_arg_short(arg)] = value

        def solve_arg(arg, i) -> int:
            # return index
            default_value = self.__get_arg_default_value(arg)
            if isinstance(default_value, bool):
                add_to_sys_arg(arg, True)
            elif isinstance(default_value, str):
                if i + 1 < len(sys.argv) and not self.__is_opt(sys.argv[i + 1]):
                    add_to_sys_arg(arg, sys.argv[i + 1])
                    i += 1
                else:
                    add_to_sys_arg(arg, default_value)
            elif isinstance(default_value, int):
                if i + 1 < len(sys.argv) and not self.__is_opt(sys.argv[i + 1]):
                    add_to_sys_arg(arg, int(sys.argv[i + 1]))
                    i += 1
                else:
                    add_to_sys_arg(arg, default_value)
            else:
                err(f'args value type can\'t be {type(default_value)} type')
                raise TypeError
            return i
        i = 1
        while i < len(sys.argv):
            arg = sys.argv[i]
            if arg.startswith('--'):
                opt = arg[2:]
                if opt in self.opt_args:
                    arg = self.opt_args[opt]
                    i = solve_arg(arg, i)
                elif not self.__in_main_cmd:
                    assert False, f'{arg} not exist'
            elif arg.startswith('-'):
                opt = arg[1:]
                for o in opt:
                    if o in self.opt_short_args:
                        arg = self.opt_short_args[o]
                        i = solve_arg(arg, i)
                    elif not self.__in_main_cmd:
                        assert False, f'-{o} not exist'
            else:
                self.sys_targets.append(arg)
            i += 1

    def __check_required(self):
        for k in self.opt_args.keys():
            arg = self.opt_args[k]
            if self.__get_arg_required(arg):
                short_name = self.__get_arg_short(arg)
                long_name = self.__get_arg_long(arg)
                if short_name not in self.sys_short_args.keys() and long_name not in self.sys_args.keys():
                    err(f'-{short_name} or --{long_name} is required!')
                    assert False, "cmd check required arg failed"

    def __print_help(self):
        help_info = green("\nylzs cmd frame v0.1\n\n")
        help_info += yellow(self.brief_intro + '\n\n')
        args = set()
        for _, val in self.opt_short_args.items():
            args.add(val)
        for _, val in self.opt_args.items():
            args.add(val)
        for arg in args:
            required = 'required' if self.__get_arg_required(
                arg) else 'optional'
            help_info += f'{"-"+self.__get_arg_short(arg): <4}{"--"+self.__get_arg_long(arg): <10}{self.__get_arg_help(arg): <20}{required}\n'
        print(help_info)

    def __init__(self, options_argv=[], brief_intro="", in_main_cmd=False) -> None:
        self.__in_main_cmd = in_main_cmd
        self.brief_intro = brief_intro
        self.__init_dirs()
        self.__init_opt_args(options_argv)
        self.__init_sys_argv()
        self.__check_required()
        if 'h' in self.sys_short_args.keys() or 'help' in self.sys_args.keys():
            self.print_help()

    def init_ext_file(self, ext_file):
        content = f'import sys\nsys.path.append(r"{self.cmd_dir}")\n{">>> auto import from cmd_base <<<":#^80}\n'
        with open(ext_file, 'r+') as f:
            d = f.read(1024)
            f.seek(0)
            if content in d:
                return
            d = content + d
            f.write(d)

    def print_help(self):
        if self.get_opt('h'):
            target = self.get_opt('h')
            sys.argv.remove(target)
            ext_mod = f"{target + '_ext'}"
            self.init_ext_file(pjoin(self.cmds_dir, ext_mod + ".py"))
            ext = __import__(ext_mod)
            ext.cmd().main()
        elif len(self.sys_targets) > 0:
            target = self.sys_targets[0]
            sys.argv.remove(target)
            ext_mod = f"{target + '_ext'}"
            self.init_ext_file(pjoin(self.cmds_dir, ext_mod + ".py"))
            ext = __import__(ext_mod)
            ext.cmd().main()
        else:
            self.__print_help()
        sys.exit(0)

    def get_opt(self, opt: str):
        if self.__is_short_name(opt):
            if opt not in self.opt_short_args.keys():
                err(f'unknown opt -{opt}')
                assert False, 'cmd_base get_opt failed'
            if opt not in self.sys_short_args.keys():
                return False
            return self.sys_short_args[opt]
        elif self.__is_long_name(opt):
            if opt not in self.opt_args.keys():
                err(f'unknown opt --{opt}')
                assert False, 'cmd_base get_opt failed'
            if opt not in self.sys_args.keys():
                return False
            return self.sys_args[opt]
        else:
            err(f'unknown opt {opt}')
            assert False, 'cmd_base get_opt failed'

    def get_targets(self):
        return self.sys_targets


class cmd(cmd_base):
    def __init__(self) -> None:
        super().__init__(
            brief_intro="main cmd run with target",
            in_main_cmd=True
        )

    def main(self):
        targets = self.get_targets()
        if len(targets) == 0:
            self.print_help()
        target = targets[0]
        sys.argv.remove(target)
        ext_mod = f"{target + '_ext'}"
        self.init_ext_file(pjoin(self.cmds_dir, ext_mod + ".py"))
        ext = __import__(ext_mod)
        sys.exit(ext.cmd().main())


if __name__ == "__main__":
    cmd().main()
