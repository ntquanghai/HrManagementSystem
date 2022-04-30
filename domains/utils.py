import os
import json
import pickle
from employee import Employee

def find(lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return -1

def loadData(path):
    if(getFileType(path) == ".txt"):
        with open(path,"r") as f:
            data = json.loads(f.read())
            return data
    elif(getFileType(path) == ".pkl"):
        f = open(path,"rb")
        data = []
        while True:
            try:
                pic = pickle.load(f)
                currData = {}
                currData["name"] = pic.name
                currData["id"] = pic.id
                currData["dob"] = pic.dob
                currData["email"] = pic.email
                currData["pos"] = pic.pos
                currData["salary"] = pic.salary
                currData["dep"] = pic.dep
                data.append(currData)
            except EOFError:
                break
        return data

def sortListInDict(list, param):
    newList = sorted(list,key=lambda d: d[param])
    return newList

def getFileType(path):
    name, extension = os.path.splitext(path)
    return extension

# print(loadData("data\empData\empData.pkl"))