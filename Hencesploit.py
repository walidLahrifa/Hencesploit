#!/usr/bin/python3
from colored import fg, attr
from cmd import Cmd
from core.adit import logo
from core.adit.loginshell import Sea
from core.adit.registershell import Reo
from core.adit import about
from core.help_menus import help_login_register
from core.help_menus import general_help_menu
from core.logos import logo_login
from core.logos import LOGO_REGISTER

class Hello(Cmd):
    prompt = '%sHencesploit > %s' % (fg(105), attr(0))

    def do_exit(self, line):
        module = globals()
        m = module['Hello']
        splits = m.prompt.split(' > ')
        if len(splits) == 2:
            print("%s Here is your way out %s" % (fg(196), attr(0)) )
            return True
        else:
            m.prompt = ' > '.join(splits[:-2]) + ' > '

    def do_login(self, line):
        logo_login.logo()
        Sea().cmdloop()
    def do_register(self,line):
        LOGO_REGISTER.logo()
        Reo().cmdloop()
    def do_about(self,line):
        about.about()
    def do_help(self, arg):
        if arg == "-h":
            general_help_menu.help()
        elif arg == '':
            help_login_register.help()
        else:
            print("%s Please enter help or help -h to find your guid %s" % (fg(196), attr(0)))


if __name__ == '__main__':
    logo.logo()
    Hello().cmdloop()
