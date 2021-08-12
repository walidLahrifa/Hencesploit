import datetime
import json
from bson.objectid import ObjectId
from colored import fg, attr

class ProjE:
    def __init__(self, id, Project_name=None, Project_description=None,Project_auditors=None,user_name=None):
        self.id = id
        if Project_name != None and Project_description != None and Project_auditors != None:
            self.Project_name = Project_name
            self.Project_description = Project_description
            self.Project_auditors = Project_auditors
            self.user_name=user_name
        else:
            self.Project_auditors = ""
            self.Project_description = ""
            self.Project_name = ""
            self.user_name =""
    def Proj_up(self,Project_name,Project_description,Project_auditors, clients):
        self.creation_date = datetime.datetime.today()
        self.Project_name = Project_name
        self.Project_description = Project_description
        self.Project_auditors = Project_auditors
        id = clients.insert_one(
            {'Project name':  self.Project_name,'Project_description' : self.Project_description ,
             'Project_auditors': self.Project_auditors,'creation_date': self.creation_date}).inserted_id
        self.id = id
        return True

    def log_in(self,users):
        exists = users.find_one({'user_name': self.user_name})
        if exists:
            exosts = users.find_one({'project': [self.Project_name,self.Project_description] })
            if exosts:
                self.id = exists['_id']
                return str(self.id)
            else:
                return {'error': '!!!!! Attention !!!!!'}
        else:
            return {'error': '!!!!! Attention !!!!!'}

    def update(self, _id, Project_name, Project_description, Project_auditors, Projects):
        self.Project_name = Project_name
        self.Project_description = Project_description
        self.Project_auditors=Project_auditors
        if str(Project_description)!='old':
            mal = Projects.update({"_id":ObjectId(self.id)}, {'$set' : {"Project_description": str(Project_description)}})
        else :
            print("%s Your description has not been changed %s" %(fg(196), attr(0)))
            pass
        if str(Project_name) != 'old' :
            nam = Projects.update({"_id":ObjectId(self.id)}, {'$set' : {"Project name" : str(Project_name)}})
        else :
            print("%s Your project name has not been changed %s" % (fg(196), attr(0)))
            pass
        if str(Project_auditors) != 'old' :
            pam = Projects.update({"_id":ObjectId(self.id)}, {'$set' : {"Project_auditors" : str(Project_auditors)}})
        else :
            print("%s Your auditors have not been changed  %s" % (fg(196), attr(0)))
            pass
    def findauditor(self,Project_name,Projects):
        self.Project_name = Project_name
        exists = Projects.find_one({'Project name':(str(Project_name))})
        if exists:
            self.project_auditors = exists['Project_auditors']
            return str(self.project_auditors)
        else:
            pass
    def findprojectid(self,Project_name,Projects):
        self.Project_name = Project_name
        exists = Projects.find_one({'Project name': (str(Project_name))})
        if exists:
            self.project_id = exists['_id']
            return str(self.project_id)
        else:
            pass
    def findprojectinfos(self,Project_name,Projects):
        self.Project_name = Project_name
        exists = Projects.find_one({'Project name': (str(Project_name))})
        if exists:
            self.proj_auditors=exists['Project_auditors']
            self.proj_name=exists['Project name']
            self.proj_id = exists['_id']
            self.proj_description=exists['Project_description']
            self.proj_creat_date=exists['creation_date']
            return str(self.proj_creat_date),str(self.proj_auditors),str(self.proj_name),str(self.proj_description)
        else:
            pass
    def projectexist(self,Project_name,Projects):
        self.Project_name = Project_name
        exists = Projects.find_one({'Project name': (str(Project_name))})
        if exists:
            pass
        else :
            return {'error': '!!!!! Attention !!!!!'}
    def removeproj(self,proj_id,Projects):
        self.proj_id=proj_id
        rem=Projects.remove({"_id":ObjectId(self.proj_id)})
    def findprojectinfoswithid(self,proj_id,Projects):
        self.proj_id=proj_id
        exists = Projects.find_one({"_id":ObjectId(self.proj_id)})
        if exists:
            self.proj_auditors=exists['Project_auditors']
            self.proj_name=exists['Project name']
            self.proj_id = exists['_id']
            self.proj_description=exists['Project_description']
            self.proj_creat_date=exists['creation_date']
            return str(self.proj_creat_date),str(self.proj_auditors),str(self.proj_name),str(self.proj_description)
        else:
            pass
    def removeauditor(self,projo_id,proj_audite,Project):
        self.proj_audite=proj_audite
        self.projo_id=projo_id
        pam = Project.update({"_id": ObjectId(self.projo_id)}, {'$set': {"Project_auditors": str(proj_audite)}})


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

