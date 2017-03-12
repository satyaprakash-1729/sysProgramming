from myLib1729 import *
from time import sleep
import os

print "\n\nReading Input Files ...\n"
sleep(1)
attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack"]

fAddUser = open("totTrainAdduser.txt","r")
fHydraFTP = open("totTrainHydraFTP.txt","r")
fHydraSSH = open("totTrainHydraSSH.txt","r")
fJavaMetr = open("totTrainJavaMetr.txt","r")
fMetr = open("totTrainMeterpreter.txt","r")
fWebShell = open("totTrainWebShell.txt","r")

print "What Weight do u want to use for ngrams division?\n"
n = int(raw_input())

AddUserString = fAddUser.read()
HydraSSHString = fHydraSSH.read()
HydraFTPString = fHydraFTP.read()
JavaMetrString = fJavaMetr.read()
MeterpreterString = fMetr.read()
WebshellString = fWebShell.read()

print "Creating individual file records..."
sleep(1)
AddUserData = AddUserString.split("-1")[:-1]
HydraSSHData = HydraSSHString.split("-1")[:-1]
HydraFTPData = HydraFTPString.split("-1")[:-1]
JavaMetrData = JavaMetrString.split("-1")[:-1]
MeterpreterData = MeterpreterString.split("-1")[:-1]
WebshellData = WebshellString.split("-1")[:-1]

noOfAddUserFiles = len(AddUserData)
noOfHydraSSHFiles = len(HydraSSHData)
noOfHydraFTPFiles = len(HydraFTPData)
noOfJavaMetrFiles = len(JavaMetrData)
noOfMeterpreterFiles = len(MeterpreterData)
noOfWebShellFiles = len(WebshellData)

AddUserFilesDict = []
HydraSSHFilesDict = []
HydraFTPFilesDict = []
JavaMetrFilesDict = []
MeterpreterFilesDict = []
WebshellFilesDict = []

AllAddUser = ""
AllHydraSSH = ""
AllHydraFTP = ""
AllJavaMetr = ""
AllMeterpreter = ""
AllWebShell = ""

for i in AddUserData:
    AllAddUser += i
    AddUserFilesDict.append(ngramsDictionary(i.split(),n))

for i in HydraSSHData:
    AllHydraSSH += i
    HydraSSHFilesDict.append(ngramsDictionary(i.split(),n))

for i in HydraFTPData:
    AllHydraFTP += i
    HydraFTPFilesDict.append(ngramsDictionary(i.split(),n))

for i in JavaMetrData:
    AllJavaMetr += i
    JavaMetrFilesDict.append(ngramsDictionary(i.split(),n))

for i in MeterpreterData:
    AllMeterpreter += i
    MeterpreterFilesDict.append(ngramsDictionary(i.split(),n))

for i in WebshellData:
    AllWebShell += i
    WebshellFilesDict.append(ngramsDictionary(i.split(),n))



print "\n\nCreating ngrams dictionaries for all files. Please Wait ...\n"
addUserDict = ngramsDictionary(AllAddUser.split(),n)
print "Add User Dictionary Created!\n"
sleep(1)
HydraFTPDict = ngramsDictionary(AllHydraFTP.split(),n)
print "Hydra FTP Dictionary Created!\n"
sleep(1)
HydraSSHDict = ngramsDictionary(AllHydraSSH.split(),n)
print "Hydra SSH Dictionary Created!\n"
sleep(1)
JavaMetrDict = ngramsDictionary(AllJavaMetr.split(),n)
print "Java Meterpreter Dictionary Created!\n"
sleep(1)
MetrDict = ngramsDictionary(AllMeterpreter.split(),n)
print "Meterpreter Dictionary Created!\n"
sleep(1)
WebShellDict = ngramsDictionary(AllWebShell.split(),n)
print "Webshell Dictionary Created!\n"
sleep(1)

print "\nCreating Data for Dictionaries ...\n"
sleep(1)
allDicts = [addUserDict,HydraFTPDict,HydraSSHDict,JavaMetrDict,MetrDict,WebShellDict]
top30Adduser = []
top30HydraFTP = []
top30HydraSSH = []
top30JavaMetr = []
top30Metr = []
top30Webshell = []
top30Data = [top30Adduser,top30HydraFTP,top30HydraSSH,top30JavaMetr,top30Metr,top30Webshell]
for i in range(len(allDicts)):
    dict1 = allDicts[i]
    Ltot = len(dict1)
    c=0
    #sentinel = Ltot*0.3
    sentinel = 450
    top30 = top30Data[i]
    print "Creating top 30% arrays of tuples for "+attackType[i]+" . . .\n"
    sleep(1)
    sortedDictArray = sorted(dict1.iteritems(), key=lambda (k,v): (v,k), reverse=True)
    for key, value in sortedDictArray:
        c+=1
        if(sentinel >= c):
            top30.append(key)

###################################
filesInDir = os.listdir("./")
k=1
string1 ="DATASET_"+str(k)+".arff"
while string1 in filesInDir:
    k+=1
    string1 = "DATASET_"+str(k)+".arff"
finalFile = open(string1,"a+")
print "--------------------------------------------------------\nCreating DATASET . . ."
sleep(3)

features = []

for i in top30Data:
    features+=i

string2 = ""
for l in range(1,len(features)+1):
    string2+="@attribute feature" + str(l) + " numeric\n"
configString = "@relation KDDTrain-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.supervised.instance.Resample-B0.0-S1-Z18.0-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.supervised.instance.SMOTE-C2-K5-P1000.0-S1-weka.filters.supervised.instance.SMOTE-C2-K5-P500.0-S1-weka.filters.supervised.instance.SMOTE-C2-K5-P125.0-S1-weka.filters.supervised.instance.SMOTE-C3-K5-P500.0-S1-weka.filters.supervised.instance.SMOTE-C3-K5-P150.0-S1-weka.filters.supervised.instance.SMOTE-C4-K5-P800.0-S1-weka.filters.unsupervised.instance.Randomize-S42\n"+string2+"@attribute class {adduser,hydraftp,hydrassh,javameter,meterpreter,webshell}\n\n@data\n"
finalFile.write(configString)

dataSet1 = ""
dataSet2 = ""
dataSet3 = ""
dataSet4 = ""
dataSet5 = ""
dataSet6 = ""
for i in range(noOfAddUserFiles):
    for j in range(len(features)):
        try:
            dataSet1+=str(AddUserFilesDict[i][features[j]])+", "
        except:
            dataSet1 += str(0) + ", "
    dataSet1+="adduser\n"
    finalFile.write(dataSet1)
for i in range(noOfHydraFTPFiles):
    for j in range(len(features)):
        try:
            dataSet2+=str(HydraFTPFilesDict[i][features[j]])+", "
        except:
            dataSet2 += str(0) + ", "
    dataSet2+="hydraftp\n"
    finalFile.write(dataSet2)
for i in range(noOfHydraSSHFiles):
    for j in range(len(features)):
        try:
            dataSet3+=str(HydraSSHFilesDict[i][features[j]])+", "
        except:
            dataSet3 += str(0) + ", "
    dataSet3+="hydrassh\n"
    finalFile.write(dataSet3)
for i in range(noOfJavaMetrFiles):
    for j in range(len(features)):
        try:
            dataSet4+=str(JavaMetrFilesDict[i][features[j]])+", "
        except:
            dataSet4 += str(0) + ", "
    dataSet4+="javameter\n"
    finalFile.write(dataSet4)
for i in range(noOfMeterpreterFiles):
    for j in range(len(features)):
        try:
            dataSet5+=str(MeterpreterFilesDict[i][features[j]])+", "
        except:
            dataSet5 += str(0) + ", "
    dataSet5+="meterpreter\n"
    finalFile.write(dataSet5)
for i in range(noOfWebShellFiles):
    for j in range(len(features)):
        try:
            dataSet6+=str(WebshellFilesDict[i][features[j]])+", "
        except:
            dataSet6 += str(0) + ", "
    dataSet6+="webshell\n"
    finalFile.write(dataSet6)

print "###################################################################################"
print "DATASET Created in file "+ string1 +" !!!"
print "Dataset Specifications :\n"
print "------------------------------------------------------------"
print "Dataset Name : Attack Recognition Dataset"
print "No. of attributes :",len(features)
print "No. of instances :",noOfAddUserFiles+noOfHydraFTPFiles+noOfHydraSSHFiles+noOfMeterpreterFiles+noOfWebShellFiles+noOfJavaMetrFiles
classes = "Classes in Dataset : "
for i in attackType:
    classes += " "+i+" "
print classes
print "-------------------------------------------------------------"
print "################################################################################"


'''
    f1 = top30Adduser[i]
    f2 = top30Adduser[i+1]
    f3 = top30Adduser[i+2]
    f4 = top30HydraFTP[i]
    f5 = top30HydraFTP[i+1]
    f6 = top30HydraFTP[i+2]
    f7 = top30HydraSSH[i]
    f8 = top30HydraSSH[i+1]
    f9 = top30HydraSSH[i+2]
    f10 = top30JavaMetr[i]
    f11 = top30JavaMetr[i+1]
    f12 = top30JavaMetr[i+2]
    f13 = top30Metr[i]
    f14 = top30Metr[i+1]
    f15 = top30Metr[i+2]
    f16 = top30Webshell[i]
    f17 = top30Webshell[i+1]
    f18 = top30Webshell[i+2]
    features = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18]
'''