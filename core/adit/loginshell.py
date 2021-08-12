#!/usr/bin/python3
from colored import fg, attr
from cmd import Cmd
from core.logos import logo_login
from core.logos.Project_Profile_logo import logo
from core.Project_Management.projectshell import Raw
from dataModel.Model import sign
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
app=Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://Walid:3.n.Z7kRB9dc!D8@hencedb-uhcuy.mongodb.net/Hencesploit20?retryWrites=true&w=majority'
mongo=PyMongo(app)
bcrypt = Bcrypt(app)
users = mongo.db.users
jwt = JWTManager(app)
CORS(app)
id=""
class Sea(Cmd):
    prompt =\
"""%s
                    
                    |-----------|
Hencesploit > %s"""% (fg(105), attr(0)) +"""Login | Username :| """

    def do_log(self, line):
        try:
            if line !="":
                user_login = line
                self.userlogin = user_login
                print('%sUsername ==> %s'%(fg(129), attr(0)) + self.userlogin)
                self.prompt =\
"""%s                    |-----------|
Hencesploit > %s"""% (fg(105), attr(0)) +"""Login | Password :| """
            else:
                print('%s--> Warning : Please enter a valid user name !%s'%(fg(160), attr(0)))
        except:
            print("%s--> Warning : Please enter the user name first !%s"%(fg(160), attr(0)))
    def do_pass(self, line):
        try:
            if line !="":
                user_passwd = line
                self.prompt = "%sHencesploit > %s" % (fg(105), attr(0))+ "%sPlease Submit %s" % (fg(202), attr(0)) + self.userlogin + "%s > %s"% (fg(202), attr(0))
                self.user_passwd = user_passwd
                print('%sPassword ==> %s'%(fg(129), attr(0)) + self.user_passwd)
            else:
                print("%s--> Warning : Please enter a valid password%s" %(fg(160), attr(0)))
        except:
                print("%s--> Warning : Please enter the user name first !%s"%(fg(160), attr(0)))
    def do_submit(self, line):
        try:
            i=0
            if i>=0 :
                if self.userlogin !=None and self.user_passwd !=None :
                    user = sign('', self.userlogin, self.user_passwd)
                    islogged = user.log_in(users, bcrypt)
                    if 'error' in islogged:
                        print('%s--> Warning : You have entered an invalid username or password ! Please '
                              'try again !%s'%(fg(160), attr(0)))
                        Sea().cmdloop()
                        return islogged
                    else:
                        print("")
                        print("%s----------------------------> Welcome back, we are super excited to have you on board <----------------------------------%s"% (fg(28), attr(0)))
                        logo()
                        Raw.user_passwd=self.user_passwd
                        Raw.user_id = islogged
                        Raw().cmdloop()
        except:
            print("%s--> Warning : Please complete your LOGIN first !!%s" % (fg(160), attr(0)))
    def do_back(self,inp):
            module = globals()
            m = module['Sea']
            splits = m.prompt.split(' > ')
            if len(splits) == 2:
                return True
            else:
                m.prompt = ' > '.join(splits[:-1]) + ' > '
    def do_help(self, arg):
        logo_login.logo()

if __name__ == '__main__':

    Sea().cmdloop()
