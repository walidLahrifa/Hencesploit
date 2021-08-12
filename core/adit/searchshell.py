#!/usr/bin/python3
import os
from cmd import Cmd
from core.adit import help_search
from colored import fg, attr


class Mia(Cmd):
    prompt = '%sHencesploit >%s' % (fg(105), attr(0)) + '%s search >%s' % (fg(202), attr(0))

    def do_help(self, line):
        help_search.do_help()

    def do_back(self, line):
        module = globals()
        m = module['Mia']
        splits = m.prompt.split(' > ')
        if len(splits) == 1:
            return True
        else:
            m.prompt = ' > '.join(splits[:-1]) + ' > '
            return True
    def do_search(self, line):
        print("""%s

Matching Modules
================

Name                                       type                    
----                                       -----                     
                                                              %s""" % (fg(26), attr(0)))
        initial = []
        p = '/'
        flux = os.getcwd().split('/')
        for i in range(0, len(flux)):
            if flux[i] == 'Hencesploit2.0.2020':
                m = i
                for x in range(1, m + 1):
                    initial = initial + [flux[x]]
                dope = p.join(initial)
                iq = '/' + dope + "/modules"
                os.chdir(iq)
                for moduledir in os.listdir(os.getcwd()):
                    if moduledir == '__init__.py' or moduledir == '__pycache__':
                        pass
                    else:
                        iq = '/' + dope + "/modules/" + moduledir
                        os.chdir(iq)
                        for module in os.listdir(os.getcwd()):
                            if module == '__init__.py' or module == '__pycache__':
                                pass
                            else:
                                if line=='':
                                    print('{0:40} {1:12}'.format(module, moduledir))
                                elif line in module :
                                    print('{0:40} {1:12}'.format(module, moduledir))
                                else:
                                    pass

if __name__ == '__main__':
    Mia().cmdloop()
