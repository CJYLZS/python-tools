import sys
sys.path.append(r"D:\code\python\tools\yutils")
#######################>>> auto import from cmd_base <<<########################
from cmd import *

class cmd(cmd_base):
    def __init__(self, options_argv=[
            ("a", "aa", "test a", False, False),
            ("b", "bb", "test b", 888, False),
            ("c", "cc", "test c", "fuck", True),
            ("d", "dd", "test d", "", False),
            ("e", "ee", "test e", -1, False)
        ],
        brief_intro='a test extension'
    ) -> None:
        super().__init__(options_argv, brief_intro=brief_intro)
    
    def main(self):
        if self.get_opt('a'):
            print('a')
        if self.get_opt('bb'):
            print(self.get_opt('b'))
        if self.get_opt('c'):
            print(self.get_opt('c'))
        info('test ok')
        return 0