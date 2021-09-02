#YLZS 20210107
#获取以当前根目录下所有重名文件
#按修改时间降序排列
#格式化后存入json文件
import os
import time
import json
from time import gmtime
#{"fileName":[path,mtime]}
fileDict={}
oldFileList={}
#fMT 0文件名 1目录 2修改时间
def refreshDict(fMT):
    global fileDict,oldFileList
    for i in fileDict.keys():
        if i==fMT[0]:
            #如果当前文件是后修改好的
            if(i in oldFileList.keys()):
                oldFileList[i].append([fileDict[i][1],fileDict[i][0]])
            else:
                oldFileList[i]=[
                [fileDict[i][1],fileDict[i][0]],
                [fMT[2],fMT[1]]]
            fileDict[i][0]=fMT[1]
            fileDict[i][1]=fMT[2]
            return
    fileDict[fMT[0]]=[fMT[1],fMT[2]]

def GetFile(filepath):
#遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        if(fi[0]=='.'):continue
        fi_d = os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
            GetFile(fi_d)
        else:
            fMT=[fi,os.path.join(filepath,fi),os.path.getmtime(fi_d)+28800]
            refreshDict(fMT)
GetFile('.')
for i in oldFileList.keys():
	oldFileList[i].sort(reverse=True)
for i in oldFileList.keys():
	for j in oldFileList[i]:
		j[0]=time.strftime("%Y-%m-%d_%H:%M:%S", gmtime(j[0]))
with open ("resultBeautify.json","w",errors="ignore",encoding='utf-8') as f:
    #data=json.loads(oldFileList)
    data=json.dumps(oldFileList,indent=4,separators=(',', ':'))
    f.write(data)