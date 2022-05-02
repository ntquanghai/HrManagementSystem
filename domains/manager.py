from employee import Employee
import pickle
import utils
import os 
import json
from department import Department
from depLeader import DepLeader

class Manager(DepLeader):
    def __init__(self, id, name, dob, email, pos, salary, dep):
        super().__init__(id, name, dob, email, pos, salary, dep)
        self.pos = "manager"

    def newDepLeader(self):
        name = input("Enter the employee's name: ")
        dob = Employee.setDob()
        dep = input("Enter the manager's department: ")
        pos = "leader"
        salary = Employee.getSalary(dep,pos)

        if((not os.path.exists("data\empData\empData.txt")) or (os.path.getsize("data\empData\empData.txt")==0)):
            with open('data\empData\empData.txt', 'w+') as f:
                wrapper = []
                currData = {}
                email = utils.emailName(name)+"."+"er-1"+"@gmail.com"
                pic = DepLeader("ER-1",name,dob,email,pos,salary,dep)
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
                pic = DepLeader(id,name,dob,email,pos,salary,dep)
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

    def managerPromote(self):
        promotedEmp = DepLeader.searchById(self)
        dep = DepLeader.getDep(self)
        with open('data\empData\empData.txt', 'r+') as f:
            data = json.loads(f.read())
            promotedEmpIndex = utils.find(data,"id",promotedEmp["id"])
        with open('data\empData\empData.txt', 'w+') as f:
            while True:
                if(data[promotedEmpIndex]["pos"] == "sr"):
                    data[promotedEmpIndex]["pos"] = "depLeader"
                    data[promotedEmpIndex]["salary"] = Employee.getSalary(data[promotedEmpIndex]["dep"],data[promotedEmpIndex]["pos"])
                    break
            print(data)
            f.write(json.dumps(utils.sortListInDict(data,"id")))
    
    def managerDemote(self):
        demotedEmp = DepLeader.searchById(self)
        dep = DepLeader.getDep(self)
        with open('data\empData\empData.txt', 'r+') as f:
            data = json.loads(f.read())
            promotedEmpIndex = utils.find(data,"id",demotedEmp["id"])
        with open('data\empData\empData.txt', 'w+') as f:
            while True:
                if(data[promotedEmpIndex]["pos"] == "depLeader"):
                    data[promotedEmpIndex]["pos"] = "sr"
                    data[promotedEmpIndex]["salary"] = Employee.getSalary(data[promotedEmpIndex]["dep"],data[promotedEmpIndex]["pos"])
                    break
            print(data)
            f.write(json.dumps(utils.sortListInDict(data,"id")))

    
