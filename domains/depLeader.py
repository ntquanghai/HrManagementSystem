from employee import Employee
import pickle
import utils
import os 
import json
from department import Department

class DepLeader(Employee):
    def __init__(self, id, name, dob, email, pos, salary, dep):
        super().__init__(id, name, dob, email, pos, salary, dep)
        self.pos = "leader"
    
    def rmEmp(self):
        removedEmp = DepLeader.searchById(self)
        dep = DepLeader.getDep(self)
        with open('data\empData\empData.txt', 'r+') as f:
            data = json.loads(f.read())
            updatedEmpIndex = utils.find(data,"id",removedEmp["id"])
        with open('data\empData\empData.txt', 'w+') as f:
            del data[updatedEmpIndex]
            f.write(json.dumps(utils.sortListInDict(data,"id")))
    
    def updateEmpInfo(self,info,newInfo):
        updatedEmp = DepLeader.searchById(self)
        dep = DepLeader.getDep(self)
        with open('data\empData\empData.txt', 'r+') as f:
            data = json.loads(f.read())
            updatedEmpIndex = utils.find(data,info,updatedEmp[info])
        with open('data\empData\empData.txt', 'w+') as f:
            data[updatedEmpIndex][info] = newInfo
            data[updatedEmpIndex]["salary"] = Employee.getSalary(data[updatedEmpIndex]["dep"],data[updatedEmpIndex]["pos"])
            f.write(json.dumps(utils.sortListInDict(data,"id")))

    def newEmp(self):
        id = input("Enter the employee's ID: ")
        name = input("Enter the employee's name: ")
        dob = Employee.setDob()
        email = input("Enter the employere's email: ")
        dep = DepLeader.getDep(self)
        pos = input("Enter the employee's position: ")
        salary = Employee.getSalary(dep,pos)

        if((not os.path.exists("data\empData\empData.txt")) or (os.path.getsize("data\empData\empData.txt")==0)):
            with open('data\empData\empData.txt', 'w+') as f:
                wrapper = []
                currData = {}
                pic = Employee(id,name,dob,email,pos,salary,dep)
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
                pic = Employee(id,name,dob,email,pos,salary,dep)
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

    def promote(self):
        promotedEmp = DepLeader.searchById(self)
        dep = DepLeader.getDep(self)
        with open('data\empData\empData.txt', 'r+') as f:
            data = json.loads(f.read())
            promotedEmpIndex = utils.find(data,"id",promotedEmp["id"])
        with open('data\empData\empData.txt', 'w+') as f:
            while True:
                if(data[promotedEmpIndex]["pos"] == "entry"):
                    data[promotedEmpIndex]["pos"] = "jr"
                    data[promotedEmpIndex]["salary"] = Employee.getSalary(data[promotedEmpIndex]["dep"],data[promotedEmpIndex]["pos"])
                    break
                elif(data[promotedEmpIndex]["pos"] == "jr"):
                    data[promotedEmpIndex]["pos"] = "sr"
                    data[promotedEmpIndex]["salary"] = Employee.getSalary(data[promotedEmpIndex]["dep"],data[promotedEmpIndex]["pos"])
                    break
            print(data)
            f.write(json.dumps(utils.sortListInDict(data,"id")))
    
    def demote(self):
        promotedEmp = DepLeader.searchById(self)
        dep = DepLeader.getDep(self)
        with open('data\empData\empData.txt', 'r+') as f:
            data = json.loads(f.read())
            promotedEmpIndex = utils.find(data,"id",promotedEmp["id"])
        with open('data\empData\empData.txt', 'w+') as f:
            while True:
                if(data[promotedEmpIndex]["pos"] == "jr"):
                    data[promotedEmpIndex]["pos"] = "entry"
                    data[promotedEmpIndex]["salary"] = Employee.getSalary(data[promotedEmpIndex]["dep"],data[promotedEmpIndex]["pos"])
                    break
                elif(data[promotedEmpIndex]["pos"] == "sr"):
                    data[promotedEmpIndex]["pos"] = "jr"
                    data[promotedEmpIndex]["salary"] = Employee.getSalary(data[promotedEmpIndex]["dep"],data[promotedEmpIndex]["pos"])
                    break
            print(data)
            f.write(json.dumps(utils.sortListInDict(data,"id")))
        
    def searchById(self,id):
        data = DepLeader.listEmp(self)
        searchedID = str(input("Find employee's ID: "))
        empIndex = utils.find(data,"id",searchedID)
        if(empIndex>=0):
            return data[empIndex]

    def listEmp(self):
        data = utils.loadData("data\empData\empData.txt")
        returnedList = []
        for i in range(0,len(data)):
            if(data[i]["dep"].lower() == DepLeader.getDep(self)):
                returnedList.append(data[i])
        return returnedList

    def getDep(self):
        return self.dep


# la = DepLeader("1","1","29/03/2003","ntqhai2002@gmail.com","manager",2,"IT")
# la.newEmp()
# print(la.searchById())
# la.promote()
