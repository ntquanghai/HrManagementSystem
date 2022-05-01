import pickle
import utils
import os 
import json

class Department:
    def __init__(self, id, name, empNumber, entryRate, jrRate, srRate, leaderRate, managerRate):
        self.id = id
        self.name = name
        self.empNumber = empNumber
        self.salaryRate = {
            "entry": entryRate,
            "jrRate": jrRate,
            "srRate": srRate,
            "leaderRate": leaderRate,
            "managerRate": managerRate,
        }

    def newDep():
        id = input("Enter the department's ID: ")
        name = input("Enter the department's name: ")
        empNumber = Department.getEmployeeNumber(name)
        entryRate = input("Enter the department's salary rate for entry level employees: ")
        jrRate = input("Enter the department's salary rate for junior level employees: ")
        srRate = input("Enter the department's salary rate for senior level employees: ")
        leaderRate = input("Enter the department's salary rate for leader level employees: ")
        managerRate = input("Enter the department's salary rate for manager level employees: ")

        return Department(id,name,empNumber, entryRate, jrRate, srRate, leaderRate, managerRate)

    def getEmployeeNumber(dep):
        empCount = 0
        with open('data\empData\empData.txt', 'r+') as f:
            data = json.loads(f.read())
            for i in range(0, len(data)):
                if(data[i]["dep"] == dep.lower()):
                    empCount = empCount + 1
        return empCount
