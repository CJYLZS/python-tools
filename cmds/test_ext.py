import sys
sys.path.append(r"/root/work/python-tools/yutils")
#######################>>> auto import from cmd_base <<<########################
from cmd import *


class cmd(cmd_base):
    def __init__(self, options_argv=[
            ("a", "aa", "test a", False, False),
            ("b", "bb", "test b", 888, False),
            ("c", "cc", "test c", "fuck", True),
        ],
        brief_intro='a test extension'
    ) -> None:
        super().__init__(options_argv, brief_intro=brief_intro)

    def main(self):
        res = ''
        if self.get_opt('a'):
            res += 'a'
        if self.get_opt('bb'):
            val = self.get_opt('b')
            res += str(type(val)) + str(val)
        if self.get_opt('c'):
            val = self.get_opt('cc')
            res += str(type(val)) + str(val)
        print(res)
        return 0
