import datetime
import json
from bson.objectid import  ObjectId
from bson.objectid import ObjectId
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token
from flask import Flask, jsonify, request
import jwt
from colored import fg, attr
import pymongo
class sign:
    def __init__(self, id, user_name=None, password=None,project=None):
        self.id = id
        if user_name != None and password != None:
            self.user_name = user_name
            self.password = password
            self.project=project

        else:
            self.password = ""
            self.user_name = ""
            self.project=[]
    def sign_up(self,user_name,email,project, clients, bcrypt):
        self.creation_date = datetime.datetime.today()
        self.user_name = user_name
        self.email = email
        self.project = project
        password = bcrypt.generate_password_hash(self.password).decode('utf-8')
        id = clients.insert_one(
            {'email': self.email,'user_name' : self.user_name ,
             'password': password,'project' : self.project , 'creation_date': self.creation_date}).inserted_id
        self.id = id
        # return self.access_tokens()
        return True

    def access_tokens(self):
        self.identity = { 'user_id': self.id,
                          'user_name': self.user_name,
                          'password': self.password }
        id = JSONEncoder().encode(self.identity)
        access_token = create_access_token(id, expires_delta=None , user_claims=None, headers=None)
        refresh_token = create_refresh_token(id,expires_delta=None, user_claims=None, headers=None)
        user_id = str(self.id)
        return {"user_id": user_id, "user_name": self.user_name, "token": access_token, 'refresh_token': refresh_token}

    def log_in(self, users, bcrypt):
        exists = users.find_one({'user_name': self.user_name})
        if exists:
            if bcrypt.check_password_hash(exists['password'], self.password):
                self.id = exists['_id']
                return str(self.id)
            else:
                return {'error': 'Invalid password', 'status_code': 401}
        else:
            return {'error': 'No users found for this address', 'status_code': 401}

    def isregistered(self, users):
        if users.find_one({'email': self.email}):
            return True
        else:
            return False
    def update(self,_id,email,user_name,password,project, users,bcrypt):
        self.user_name = user_name
        self.email = email
        self.password=password
        self.project = project
        if str(email)!='old':
            mal = users.update({ "_id":ObjectId(self.id)},{ '$set' : {"email": str(email)}})
        else :
            pass
        if str(user_name) != 'old' :
            nam = users.update({"_id":ObjectId(self.id) },{'$set' : { "user_name" : str(user_name)}})
        else :
            pass
        if str(password) != 'old' :
            passwordi = bcrypt.generate_password_hash(str(password)).decode('utf-8')
            pam = users.update({"_id":ObjectId(self.id)},{'$set' : { "password" : str(passwordi)}})
        else :
            pass
        if project != 'old' :
            ham = users.update({"_id":ObjectId(self.id) },{'$push': {'project': project }})
        else:
            pass
    def uppdate(self,_id,email,user_name,password,project,old,users,bcrypt):
        self.user_name = user_name
        self.email = email
        self.password=password
        self.project = project
        self.id=_id
        if str(email)!='old':
            mal = users.update({ "_id":ObjectId(self.id)},{ '$set' : {"email": str(email)}})
        else :
            pass
        if str(user_name) != 'old' :
            nam = users.update({"_id":ObjectId(self.id) },{'$set' : { "user_name" : str(user_name)}})
        else :
            pass
        if str(password) != 'old' :
            passwordi = bcrypt.generate_password_hash(str(password)).decode('utf-8')
            pam = users.update({"_id":ObjectId(self.id)},{'$set' : { "password" : str(passwordi)}})
        else :
            pass
        if project != 'old' :
            bam = users.update({"_id": ObjectId(self.id)}, {'$pull': {'project':{'$in':[old]}}})
            ham = users.update({"_id":ObjectId(self.id) },{'$push': {'project': project }})
        else:
            pass
    def updato(self,id,email,user_name,password,project, users,bcrypt):
        self.user_name = user_name
        self.email = email
        self.password=password
        self.project = project
        self.id=id
        if str(email)!='old':
            mal = users.update({ "_id":ObjectId(self.id)},{ '$set' : {"email": str(email)}})
        else :
            pass
        if str(user_name) != 'old' :
            nam = users.update({"_id":ObjectId(self.id) },{'$set': { "user_name" : str(user_name)}})
        else :
            pass
        if str(password) != 'old' :
            passwordi = bcrypt.generate_password_hash(str(password)).decode('utf-8')
            pam = users.update({"_id":ObjectId(self.id)},{'$set' : { "password" : str(passwordi)}})
        else :
            pass
        if project != 'old' :
            ham = users.update({"_id":ObjectId(self.id) },{'$push': {'project': project }})
        else:
            pass
    def find(self,id, users):
        self.id=id
        exists = users.find_one({'_id':ObjectId(str(self.id))})
        if exists:
            self.user_name=exists['user_name']
            self.user_proj=exists['project']
            return str(self.user_name),self.user_proj
        else:
            print('makhdamach')
            pass
    def findusr(self,user_name, users):
        self.user_name=user_name
        exists = users.find_one({'user_name': str(user_name)})
        if exists:
            self.user_id=exists['_id']
            return str(self.user_id)
        else:
            pass
    def findproject(self,id,users):
        self.id=id
        exists = users.find_one({'_id':ObjectId(str(self.id))})
        return exists
    def finuserinfos(self,usr_id,users):
        self.usr_id=usr_id
        exists = users.find_one({'_id': ObjectId(str(self.usr_id))})
        if exists:
            self.usr_mail=exists['email']
            self.usr_name=exists['user_name']
            self.usr_id = exists['_id']
            self.usr_passwd=exists['password']
            self.usr_creat_date=exists['creation_date']
            return str(self.usr_mail),str(self.usr_name),str(self.usr_passwd),str(self.usr_creat_date)
        else:
            pass
    def usrexist(self,user_name, users):
        self.user_name=user_name
        exists = users.find_one({'user_name': str(user_name)})
        if exists:
            return True
        else:
            return
    def removeprojforusr(self,usr_name,proj_info,users):
        self.usr_name=usr_name
        self.proj_infos=proj_info
        bam = users.update({'user_name': self.usr_name}, {'$pull': {'project': {'$in': [self.proj_infos]}}})

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)