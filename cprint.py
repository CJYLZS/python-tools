class color_print:
    color_dict = {
        'red':'\033[0;31;40m', # \033[{showmode};{frontcolor};{backgroundcolor}m
        'green':'\033[0;32;40m',
        'yellow':'\033[0;33;40m',
        'blue':'\033[0;34;40m',
        'default':'\033[0m'
    }
    def __call__(self, *argv, color = 'default'):
        for arg in argv:
            print(self.color_dict[color]+str(arg)+self.color_dict['default'],end=' ')
        print()

if __name__ == '__main__':
	# print different colors
    cp = color_print()
    cp('CJYLZS','red',color='red')
    cp('CJYLZS','green',color='green')
    cp('CJYLZS','yellow',color='yellow')
    cp('CJYLZS','blue',color='blue')
    cp('CJYLZS','default')
