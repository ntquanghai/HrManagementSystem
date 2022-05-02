from depLeader import DepLeader
from department import Department
import json
from employee import Employee
import utils
import os
from manager import Manager

class Executive(DepLeader):
    def __init__(self, id, name, dob, email, pos, salary):
        super().__init__(id, name, dob, email, pos, salary)
        self.pos = "executive"

    def newDep():
        id = input("Enter the department's ID: ")
        name = input("Enter the department's name: ")
        empNumber = Department.getEmployeeNumber(name)

        with open('data/depData/'+name.lower()+".txt", 'w+') as f:
            picData = json.loads(f.read())
            pic = Department(id,name,empNumber)
            currData = {}
            currData["name"] = pic.name
            currData["id"] = pic.id
            currData["dob"] = pic.dob
            currData["email"] = pic.email
            currData["pos"] = pic.pos
            currData["salary"] = pic.salary
            currData["dep"] = pic.dep
            picData.append(currData)
        with open('data\empData\empData.txt', 'w+') as f:
            f.write(json.dumps(utils.sortListInDict(picData,"id")))  
 
    def rmDep(self,info):
        removedDep = "" 
        #Put input here
        removedDep = input("Choose the department you would like to delete: ")
        os.remove("data/depData/"+removedDep+".txt")
    
    def updateDepInfo(self,info,newInfo):
        updatedDep = input("Enter your updated dep: ")
        with open('data/depData/'+updatedDep+".txt", 'r+') as f:
            data = json.loads(f.read())
        with open('data\empData\empData.txt', 'w+') as f:
            data[info] = newInfo
            f.write(json.dumps(data))

    def newManager(self):
        name = input("Enter the manager's name: ")
        dob = Employee.setDob()
        dep = input("Enter the manager's department: ")
        pos = "manager"
        salary = Employee.getSalary(dep,pos)

        if((not os.path.exists("data\empData\empData.txt")) or (os.path.getsize("data\empData\empData.txt")==0)):
            with open('data\empData\empData.txt', 'w+') as f:
                wrapper = []
                currData = {}
                email = utils.emailName(name)+"."+"er-1"+"@gmail.com"
                pic = Manager("ER-1",name,dob,email,pos,salary,dep)
                currData["name"] = pic.name
                currData["id"] = pic.id
                currData["dob"] = pic.dob
                currData["email"] = pic.email
                currData["pos"] = pic.pos
                currData["salary"] = pic.salary
                currData["dep"] = pic.dep
                wrapper.append(currData)
                f.write(json.dumps(wrapper))
        else:
            with open('data\empData\empData.txt', 'r+') as f:
                picData = json.loads(f.read())
                id = "ER-"+str(utils.getIdNum(picData[-1]["id"])+1)
                email = utils.emailName(name)+"."+id.lower()+"@gmail.com"
                pic = Manager(id,name,dob,email,pos,salary,dep)
                currData = {}
                currData["name"] = pic.name
                currData["id"] = pic.id
                currData["dob"] = pic.dob
                currData["email"] = pic.email
                currData["pos"] = pic.pos
                currData["salary"] = pic.salary
                currData["dep"] = pic.dep
                picData.append(currData)
            with open('data\empData\empData.txt', 'w+') as f:
                f.write(json.dumps(utils.sortListInDict(picData,"id")))