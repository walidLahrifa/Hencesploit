#!/usr/bin/python3
import os
from cmd import Cmd
from colored import fg,attr
from subprocess import Popen
from core.help_menus.project_help import help
from core.adit.searchshell import Mia
from modules.auxiliary.AWS_attacksurfacefinder_EC2.AWS_attacksurfacefinder_EC2 import AWS_attacksurfacefinder_EC2
from modules.auxiliary.s3_buckets_finder.s3_buckets_finder import s3_buckets_finder
from modules.auxiliary.SimplePortScanner.SimplePortScanner import SimplePortScanner
from modules.auxiliary.nmap.nmap import nmap
from modules.auxiliary.lava_Azure_scanner.lava_Azure_scanner import lava_Azure_scanner
from modules.auxiliary.ScoutSuite_SadCLoud.ScoutSuite_SadCLoud import ScoutSuite_SadCLoud
from modules.exploit.Simplewordpress.Simplewordpress import Simplewordpress
from modules.exploit.redis.redis import redis
from modules.exploit.AWS_EC2_ATTACK.AWS_EC2_ATTACK import AWS_EC2_ATTACK
from modules import *
from core.Project_Management.edit_project import Rifa
from core.logos.logo_edit_proj import logo
from core.logos.search_logo import logos
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask import Flask
from dataModel.ModelProj import ProjE
from dataModel.Model import sign
from terminaltables import AsciiTable
app=Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://Walid:3.n.Z7kRB9dc!D8@hencedb-uhcuy.mongodb.net/Hencesploit20?retryWrites=true&w=majority'
mongo=PyMongo(app)
projects = mongo.db.Projects
users = mongo.db.users
bcrypt = Bcrypt(app)


class Hero(Cmd):
    prompt = '%sHencesploit >%s'% (fg(105), attr(0)) + '%s project >%s' % (fg(202), attr(0))
    file = None
    def do_help(self, arg):
        help()
    def do_back(self, line):
        module = globals()
        m = module['Hero']
        splits = m.prompt.split(' > ')
        if len(splits) == 1:
            return True
        else:
            m.prompt = ' > '.join(splits[:-1]) + ' > '
            return True
    def do_use(self, line):
        try:
            module=globals()[line]
            module.projname=self.metaname
            module().cmdloop()
        except:
            print("%sWarning : Module not found please check the name again !%s" % (fg(160), attr(0)))
    def do_search(self,line):
        logos()
        Mia().cmdloop()
    def do_edit(self,line):
        try:
            if line=='project' :
                check_admin=sign.findusr(self,user_name=self.Author,users=users)
                if self.idusr == check_admin :
                    Rifa.Author=self.Author
                    Rifa.metadescription=self.metadescription
                    Rifa.metaname=self.metaname
                    Rifa.idusr=self.idusr
                    Rifa.Rid=self.Rawaa
                    logo()
                    Rifa().cmdloop()
                else :
                    print('%s--> Warning : Permission denied this option is reserved for your project administrator%s'% (fg(160), attr(0)))
            else:
                print("%s--> Warning : Please enter a valid argument or enter help for more options%s" % (fg(160), attr(0)))
        except:
            print("%s--> Warning : Please enter a valid argument or enter help for more options%s" % (fg(160), attr(0)))

    def do_show(self,line):
        try:
            if line=='projects' :
                pipa=sign.findproject(self,id=self.idusr,users=users)
                meta_proj=pipa['project']
                table_data = [['PROJECTS', 'DESCRIPTION']]
                for i in range(len(meta_proj)):
                    for j in range(len(meta_proj[i])):
                        if j==0 :
                            l=meta_proj[i][j]

                        else:
                            mono=meta_proj[i][j]

                    table_data.append([l,mono])
                    table = AsciiTable(table_data)
                print(table.table)
            else:
                l=""
                m=','
                pipa = sign.findproject(self, id=self.idusr, users=users)
                meta_proj = pipa['project']
                for i in range(len(meta_proj)):
                    l = l + ',' + meta_proj[i][0]
                if line in l :
                    project_infos=ProjE.findprojectinfos(self,Project_name=line,Projects=projects)
                    project_auditor=project_infos[1].split(' ')
                    project_author=project_auditor[0]
                    table_datas = [['PROJECT NAME','PROJECT DESCRIPTION','PROJECT AUDITORS','PROJECT AUTHOR','PROJECT CREATION DATE']]
                    table_datas.append([project_infos[2],project_infos[3],project_infos[1],project_author,project_infos[0]])
                    table = AsciiTable(table_datas)
                    print(table.table)
                else :
                    print("%s--> Warning : Please enter a valid argument%s" % (fg(160), attr(0)))
        except:
            print("%s--> Warning : No projects are available Please creat a new project %s" % (fg(160), attr(0)))

    def do_remove(self,line):
        try:
            check_admin = sign.findusr(self, user_name=self.Author, users=users)
            if self.idusr == check_admin:
                if 'project' in line :
                        get_audit=ProjE.findprojectinfoswithid(self,proj_id=self.Rawaa,Projects=projects)
                        proj_rminfo=[get_audit[2],get_audit[3]]
                        project_auditors_list=get_audit[1].split(' ')
                        for auditor in project_auditors_list:
                            remforaudit=sign.removeprojforusr(self,usr_name=auditor,proj_info=proj_rminfo,users=users)
                        remov=ProjE.removeproj(self,proj_id=self.Rawaa,Projects=projects)
                        print("%s------> Task Accomplished <------%s" % (fg(28), attr(0)))
                        module = globals()
                        m = module['Hero']
                        splits = m.prompt.split(' > ')
                        if len(splits) == 1:
                            return True
                        else:
                            return True
                elif 'auditor' or 'auditors' in line:
                        try :
                            project_metaAuditor = []
                            m = " "
                            extract = line.split(' ')
                            for s in extract:
                                if s == "auditor" or s=="auditors":
                                    pass
                                else:
                                    project_metaAuditor = project_metaAuditor + [s]
                            project_Auditor = m.join(project_metaAuditor)
                            self.project_Auditor=project_Auditor
                            print('%sProject auditor to delete are ==> %s'%(fg(129), attr(0)) + self.project_Auditor)
                            if self.Author in self.project_Auditor :
                                print("%s--> Warning : You can not delete yourself from the project %s" % (fg(160), attr(0)) + self.Author)
                            else:
                                get_audit = ProjE.findprojectinfoswithid(self, proj_id=self.Rawaa, Projects=projects)
                                proj_rminfo = [get_audit[2], get_audit[3]]
                                for auditor in self.project_Auditor.split(' '):
                                    pipa = sign.findusr(self, user_name=auditor, users=users)
                                    if pipa != None:
                                        remforaudit = sign.removeprojforusr(self, usr_name=auditor, proj_info=proj_rminfo,users=users)
                                    else:
                                        print("%s--> Warning : !!! Attention !!!! The user %s" % (fg(160), attr(0)) + auditor +
                                              "%s is not found %s" % (fg(160), attr(0)))
                                new_auditor_metalist=""
                                v=" "
                                for l in self.project_Auditor.split(' '):
                                    for auditar in get_audit[1].split(' ') :
                                        if str(l) != str(auditar) :
                                            new_auditor_metalist=new_auditor_metalist+ ' '+auditar
                                        else :
                                            pass
                                new_auditor_list = new_auditor_metalist
                                if new_auditor_list[0] == ' ':
                                    advanced_list = ""
                                    for i in range(1, len(new_auditor_list)):
                                        advanced_list = advanced_list + new_auditor_list[i]
                                    ham=ProjE.removeauditor(self,projo_id=self.Rawaa,proj_audite=advanced_list,Project=projects)
                                    print("%s------> Task Accomplished <------%s" % (fg(28), attr(0)))

                        except:
                            print("%s--> Warning : Please enter a valid description or project name%s" % (fg(160), attr(0)))

                else:
                    print("%s--> Warning : Please enter a valid argument or enter help for more options%s" % (fg(160), attr(0)))
            else:
                print('%s--> Warning : Permission denied this option is reserved for your project administrator%s' % (
                    fg(160), attr(0)))
        except:
            print("%s--> Warning : Please enter a valid argument or enter help for more options (dead end)")
    def do_record(self, arg):
        x='_'
        inorderd=self.metaname.split(' ')
        ordred=x.join(inorderd)
        self.file = open(ordred+'.txt', 'w')
    def do_playback(self, arg):
        self.close()
        x='_'
        inorderd=self.metaname.split(' ')
        ordred=x.join(inorderd)
        with open(ordred+'.txt') as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, arg):
        if self.file and 'playback' not in arg:
            print(arg, file=self.file)
        return arg
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def do_share(self,line):
        initial = []
        p = '/'
        flux = os.getcwd().split('/')
        for i in range(0, len(flux)):
            if flux[i] == 'Hencesploit2.0.2020':
                m = i
                for x in range(1, m + 1):
                    initial = initial + [flux[x]]
                dope = p.join(initial)
                iq = '/' + dope + "/core/adit/client_Hencesploit.py"
        sts = Popen("x-terminal-emulator -e python3 "+iq, shell=True).wait()

if __name__ == '__main__':
    Hero().cmdloop()