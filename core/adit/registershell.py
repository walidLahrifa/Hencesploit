from cmd import Cmd
from core.adit.loginshell import Sea
from colored import fg, attr
import re
from core.logos import LOGO_REGISTER
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask import Flask
from dataModel.Model import sign
from core.logos.LOGO_REGISTER import logo
from core.logos import logo_login
app=Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://Walid:3.n.Z7kRB9dc!D8@hencedb-uhcuy.mongodb.net/Hencesploit20?retryWrites=true&w=majority'
mongo=PyMongo(app)
bcrypt = Bcrypt(app)
users = mongo.db.users
class Reo(Cmd):
    prompt = \
            """%s                       |-----------|
Hencesploit >%s"""% (fg(105), attr(0)) + """ Register | Username :| """


    def do_log(self, line):
        try:
            if line != "":
                user_infos = sign.usrexist(self, user_name=line, users=users)
                if user_infos:
                    print('%s--> Warning : This user name is alre'
                          'ady used Please try again with different username !%s'%(fg(160), attr(0)))
                    pass
                else:
                    self.userlogin= line
                    print('%sUsername ==> %s'%(fg(129), attr(0)) + self.userlogin)
                    self.prompt = \
    """%s                       |---------|
Hencesploit >%s""" % (fg(105), attr(0)) + """ Register | E_Mail :| """

        except:
            print("%s--> Warning : Please enter the user name first !%s"%(fg(160), attr(0)))
    def do_mail(self, line):
        try:
            if self.userlogin:
                regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
                if (re.search(regex, line)):
                    user_Mail = line
                    self.user_Mail = user_Mail
                    print('%sE_Mail ==> %s'%(fg(129), attr(0)) + self.user_Mail)
                    self.prompt ="""%s                       |-----------|
Hencesploit >%s""" % (fg(105), attr(0)) + """ Register | Password :| """

                else:
                    print('%s--> Warning : Invalid Email, please try with a mail on the form example@example.example %s'%(fg(160), attr(0)))
            else :
                print("%s--> Warning : Please enter the user name first !%s" % (fg(160), attr(0)))
        except:
            print("%s--> Warning : Please enter the user name and an e-Mail first !%s"%(fg(160), attr(0)))

    def do_pass(self, line):
        try:
            if line != "" and self.user_Mail != None:
                user_passwd = line
                self.prompt = "%sHencesploit > %s" % (fg(105), attr(0))+ "%sPlease Submit %s" % (fg(202), attr(0)) + self.userlogin + "%s > %s"% (fg(202), attr(0))
                self.user_passwd = user_passwd
                print('%sPassword ==> %s'%(fg(129), attr(0)) + self.user_passwd)
                project = []
                self.project = project
            else:
                print("%s--> Warning : Please enter a valid password%s" % (fg(160), attr(0)))
        except:
            print("%s--> Warning : Please login first ! %s" % (fg(160), attr(0)))

    def do_submit(self, line):
        try:
            if self.userlogin != None and self.user_passwd != None and self.user_Mail !=None:
                user = sign('',self.userlogin,self.user_passwd,self.project)
                user.sign_up(self.userlogin,self.user_Mail,self.project, users, bcrypt)
                print("%s"
"--------> Congratulations !! you have completed your sign up, all you need to "
                      "do now in order to start your Hencesploit experience is to sign in !!"
                      "<--------%s"% (fg(28), attr(0)))
                logo_login.logo()
                Sea().cmdloop()
        except:
            print("%s--> Warning : Please enter your login and password fist !%s" % (fg(160), attr(0)))

    def do_back(self, inp):
        module = globals()
        m = module['Reo']
        splits = m.prompt.split(' > ')
        if len(splits) == 1:
            return True
        else:
            m.prompt = ' > '.join(splits[:-1]) + "%sHencesploit >%s" % (fg(105), attr(0))

    def do_help(self, arg):
        LOGO_REGISTER.logo()

if __name__ == '__main__':

    Reo().cmdloop()


