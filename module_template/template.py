import os
import threading
from cmd import Cmd
from subprocess import Popen
from colored import fg, attr
from terminaltables import AsciiTable
from core.help_menus import project_help
getmodulename=__name__.split('.')
module_name=getmodulename[3]
key = ['CHANGEHERE']   # CHANGE HERE YOUR PROJECT PARAMETERS
values = ["CHANGEHERE"]                    # ADD DEFAULT VALUES OR LEAVE BLANKS TO BE CONFIGURED LATER
req = ['CHANGEHERE']              # IF THE PARAMETER IS REQUIRED ADD YES ELSE ADD NO
class CHANGEHERE(Cmd):      # CHANGE HERE( USE THE SAME NAME OF YOUR FOLDER AND PYTHON FILE TO NAME YOUR CLASS )
    prompt = '%sHencesploit > %s' % (fg(105), attr(0)) + '%s USE >%s' % (fg(202), attr(0)) + '%s ' \
                                                                                             '(%s'% (fg(196), attr(0)) + __name__ + '%s) > %s' % (fg(196), attr(0))
    file = None

    def do_scan(self, line):
        try:
            return True                           # YOU CAN RUN YOUR EXPLOIT OR AUXILIARY FROM HERE
        except:
            print("%s please check your arguments %s"% (fg(160), attr(0)))
            CHANGEHERE().cmdloop()  # CHANGE HERE (NAME OF YOUR CLASS IN CLASS().CMDLOOP())
    def do_show(self, line):
        if line == 'options':
            table_data = [['OPTION', 'VALUE', 'REQUIRED']]
            for i in range(0, len(key)):
                table_data.append([key[i], values[i], req[i]])
            table = AsciiTable(table_data)
            print(table.table)

        else:
            print("%son development%s" % (fg(196), attr(0)))

    def do_set(self, line):
        try:
            meta_values=[]
            x=" "
            meta= line.split(' ')
            k=meta[0].upper()
            for i in range(1,len(meta)):
                meta_values=meta_values+[meta[i]]
            v=x.join(meta_values)
            if k=='' or v == '' :
                print("%s*** Unknown Option! option not has value!%s"% (fg(160), attr(0)))
                pass

            for i in range(0, len(key)):
                if k == key[i]:
                    values[i] = v
                    print(k, "===> ", v)
                    break
                else :
                    if i==len(key)-1:
                        print("%s*** Unknown Option! option not has value!%s"% (fg(160), attr(0)))
                    else:
                        pass

        except KeyError:
            print("%s*** Unknown Option! option not has value!%s"% (fg(160), attr(0)))
        except ValueError:
            print("%s*** Option not has value!%s"% (fg(160), attr(0)))
            print("%s*** Example : set lhost 127.0.0.1%s"% (fg(160), attr(0)))

    def do_back(self, line):
        module = globals()
        m = module['CHANGEHERE']   # CHANGE HERE ( NAME OF YOUR CLASS IN ['CLASS_NAME'])
        splits = m.prompt.split(' > ')
        if len(splits) == 1:
            return True
        else:
            m.prompt = ' > '.join(splits[:-1]) + ' > '
            return True

    def do_help(self, arg):
        print(self.projname)
        project_help.help()
    def do_record(self, arg):
        x='_'
        inorderd=self.projname.split(' ')
        ordred=x.join(inorderd)
        module_file=ordred+ '_' + str(module_name)
        self.file = open(module_file+'.txt', 'w')
    def do_stop_record(self,arg):
        self.close()
    def do_playback(self, arg):
        self.close()
        x='_'
        inorderd=self.projname.split(' ')
        ordred=x.join(inorderd)
        module_file=ordred+ '_' + str(module_name)
        with open(module_file+'.txt') as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, arg):
        if self.file and 'playback' not in arg:
            print(arg, file=self.file)
        return arg
    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    CHANGEHERE().cmdloop()           # CHANGE HERE (NAME OF YOUR CLASS IN CLASS().CMDLOOP())