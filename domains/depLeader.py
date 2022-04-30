from employee import Employee
import pickle
import utils
import os 
import json

class DepLeader(Employee):
    def __init__(self, id, name, dob, email, pos, salary, dep):
        super().__init__(id, name, dob, email, pos, salary, dep)

    def addEmp():
        print("")
    def rmEmp():
        print("")
    def editEmp():
        print("")
        #Get all inputs
        #Locate data index using "find"
        #Edit data index with inputs
        #Overrwrite text file with new data
        

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
                f.seek(0)
                f.truncate(0)
                f.write(json.dumps(utils.sortListInDict(picData,"id")))

    def promote(self):
        promotedEmp = DepLeader.searchByName(self)
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
                elif(data[promotedEmpIndex]["pos"] == "sr"):
                    data[promotedEmpIndex]["pos"] = "leader"
                    data[promotedEmpIndex]["salary"] = Employee.getSalary(data[promotedEmpIndex]["dep"],data[promotedEmpIndex]["pos"])                    
                    break
                elif(data[promotedEmpIndex]["pos"] == "leader"):
                    data[promotedEmpIndex]["pos"] = "manager"
                    data[promotedEmpIndex]["salary"] = Employee.getSalary(data[promotedEmpIndex]["dep"],data[promotedEmpIndex]["pos"])
                    break
            print(data)
            f.write(json.dumps(utils.sortListInDict(data,"id")))
    
    def demote(self):
        promotedEmp = DepLeader.searchByName(self)
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
                elif(data[promotedEmpIndex]["pos"] == "leader"):
                    data[promotedEmpIndex]["pos"] = "sr"
                    data[promotedEmpIndex]["salary"] = Employee.getSalary(data[promotedEmpIndex]["dep"],data[promotedEmpIndex]["pos"])
                    break
                elif(data[promotedEmpIndex]["pos"] == "manager"):
                    data[promotedEmpIndex]["pos"] = "leader"
                    data[promotedEmpIndex]["salary"] = Employee.getSalary(data[promotedEmpIndex]["dep"],data[promotedEmpIndex]["pos"])
                    break
            print(data)
            f.write(json.dumps(utils.sortListInDict(data,"id")))
        
    def searchByName(self):
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
    
    def newDepLeader():
        id = input("Enter the employee's ID: ")
        name = input("Enter the employee's name: ")
        dob = Employee.setDob()
        email = input("Enter the employere's email: ")
        dep = input("Enter the employee's department: ")
        pos = input("Enter the employee's position: ")
        salary = Employee.getSalary(dep,pos)

        with open('myfile.pkl', 'ab') as f:
            pickle.dump(DepLeader(id,name,dob,email,pos,salary,dep), f)

        return DepLeader(id,name,dob,email,pos,salary,dep)

la = DepLeader("1","1","29/03/2003","ntqhai2002@gmail.com","manager",2,"marketing")
la.promote()
# print(la.searchByName())
# la.promote()

