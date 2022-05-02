import json
import datetime
import pickle
import os

hierarchy = [
    {
        "id": 0,
        "name": "Marketing",
        "empNumber": 0,
        "salaryRate": {
            "entry": 1,
            "jr": 2,
            "sr": 3,
            "leader": 4,
            "manager": 5,
        }
    },
    {
        "id": 1,
        "name": "IT",
        "empNumber": 0,
        "salaryRate": {
            "entry": 1,
            "jr": 2,
            "sr": 3,
            "leader": 4,
            "manager": 5,
        }
    },
    {
        "id": 2,
        "name": "Finance",
        "empNumber": 0,
        "salaryRate": {
            "entry": 1,
            "jr": 2,
            "sr": 3,
            "leader": 4,
            "manager": 5,
        }
    }, {
        "id": 3,
        "name": "HR",
        "empNumber": 0,
        "salaryRate": {
            "entry": 1,
            "jr": 2,
            "sr": 3,
            "leader": 4,
            "manager": 5,
        }
    },
    {
        "id": 4,
        "name": "Operations",
        "empNumber": 0,
        "salaryRate": {
            "entry": 1,
            "jr": 2,
            "sr": 3,
            "leader": 4,
            "manager": 5,
        }
    },
    {
        "id": 5,
        "name": "Executives",
        "empNumber": 0,
        "salaryRate": {
            "cob": 1,
            "ceo": 2,
            "coo": 3,
            "cfo": 4,
            "chro": 5,
            "cmo": 6,
            "cio": 7,
        }
    }
]

# for i in range(0,len(hierarchy)):
#     if(i==0):
#         with open("data\marketing.txt","w") as f:
#             f.write(json.dumps(hierarchy[0]))
#     elif(i==1):
#         with open("data\it.txt","w") as f:
#             f.write(json.dumps(hierarchy[1]))
#     elif(i==2):
#         with open("data/finance.txt","w") as f:
#             f.write(json.dumps(hierarchy[2]))
#     elif(i==3):
#         with open("data\hr.txt","w") as f:
#             f.write(json.dumps(hierarchy[3]))
#     if(i==4):
#         with open("data\operations.txt","w") as f:
#             f.write(json.dumps(hierarchy[4]))
#     if(i==5):
#         with open("data\executives.txt","w") as f:
#             f.write(json.dumps(hierarchy[5]))


class Employee:
    def __init__(self, id, name, dob, email, pos, salary, dep):
        self.id = id
        self.name = name
        self.dob = dob
        self.email = email
        self.pos = pos
        self.salary = salary
        self.dep = dep

    def find(lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return -1

    def setDob():
        dayFlag = True
        while(dayFlag):
            dayInput = int(input("Enter the student's day of birth: "))
            if(isinstance(int(dayInput), int)):
                if(int(dayInput) < 32 and int(dayInput) > 0):
                    dayFlag = False
                else:
                    print("Entred day was invalid. Please try again.")
            else:
                print("Entred day was invalid. Please try again.")
        monthFlag = True
        while(monthFlag):
            monthInput = int(input("Enter the student's month of birth: "))
            if(isinstance(int(monthInput), int)):
                if(int(monthInput) == 2 and int(dayInput) > 29):
                    print("Entered month was invalid. Please try again")
                elif(int(monthInput) < 13 and int(monthInput) > 0):
                    monthFlag = False
                else:
                    print("Entered month was invalid. Please try again")
        yearFlag = True
        while(yearFlag):
            yearInput = int(input("Enter student's year of birth: "))
            if(isinstance((yearInput), int)):
                if(yearInput < 1900 or yearInput > int(datetime.datetime.now().strftime("%Y"))-18):
                    print("Enter year was invalid. Please try again.")
                else:
                    yearFlag = False
        returnedValue = str(dayInput)+"/"+str(monthInput)+"/"+str(yearInput)
        return returnedValue

    def getSalary(dep, pos):
        with open("data/depData/"+dep.lower()+".txt", "r") as f:
            data = json.loads(f.read())
            return data["salaryRate"][pos.lower()]

    def setNewDob(self):
        newDob = Employee.setDob()
        self.dob = newDob
    
    def initName(self):
        while True:
            firstName = input("Enter first name: ")
            if(firstName.isalpha()):
                break
            else:
                print("Invalid input. Please try again")
        while True:
            lastName = input("Enter last name: ")
            if(firstName.isalpha()):
                break
            else:
                print("Invalid input. Please try again")
        fullName = firstName + " " + lastName
        return fullName

    def setSalary(self):
        Employee.getSalary(self.dep, self.pos)

s1 = ""
print(s1.isalpha())
