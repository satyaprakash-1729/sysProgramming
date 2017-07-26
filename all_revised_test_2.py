from myLib1729 import *
from time import sleep
import os,sys

print "\n\nReading Input Files ...\n"
#sleep(1)
attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack", "Normal"]

fAddUser = open("totTestAdduser.txt","r")
fHydraFTP = open("totTestHydraFTP.txt","r")
fHydraSSH = open("totTestHydraSSH.txt","r")
fJavaMetr = open("totTestJavaMetr.txt","r")
fMetr = open("totTestMeterpreter.txt","r")
fWebShell = open("totTestWebShell.txt","r")
fNormal = open("totTestDataValidation.txt","r")

sys.stdout.write("What Weight do u want to use for ngrams division? ")
n = int(raw_input())

AddUserString = fAddUser.read()
HydraSSHString = fHydraSSH.read()
HydraFTPString = fHydraFTP.read()
JavaMetrString = fJavaMetr.read()
MeterpreterString = fMetr.read()
WebshellString = fWebShell.read()
NormalString = fNormal.read()

print "Creating individual file records..."
#sleep(1)
AddUserData = AddUserString.split("-1")[:-1]
HydraSSHData = HydraSSHString.split("-1")[:-1]
HydraFTPData = HydraFTPString.split("-1")[:-1]
JavaMetrData = JavaMetrString.split("-1")[:-1]
MeterpreterData = MeterpreterString.split("-1")[:-1]
WebshellData = WebshellString.split("-1")[:-1]
NormalData = NormalString.split("-1")[:-1]

noOfAddUserFiles = len(AddUserData)
noOfHydraSSHFiles = len(HydraSSHData)
noOfHydraFTPFiles = len(HydraFTPData)
noOfJavaMetrFiles = len(JavaMetrData)
noOfMeterpreterFiles = len(MeterpreterData)
noOfWebShellFiles = len(WebshellData)
noOfNormalFiles = len(NormalData)

AddUserFilesDict = []
HydraSSHFilesDict = []
HydraFTPFilesDict = []
JavaMetrFilesDict = []
MeterpreterFilesDict = []
WebshellFilesDict = []
NormaFilesDict = []

AllAddUser = ""
AllHydraSSH = ""
AllHydraFTP = ""
AllJavaMetr = ""
AllMeterpreter = ""
AllWebShell = ""
AllNormal = ""

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

for i in NormalData:
    AllNormal += i
    NormaFilesDict.append(ngramsDictionary(i.split(),n))


print "\n\nCreating ngrams dictionaries for all files. Please Wait ...\n"
addUserDict = ngramsDictionary(AllAddUser.split(),n)
print "Add User Dictionary Created!\n"
#sleep(1)
HydraFTPDict = ngramsDictionary(AllHydraFTP.split(),n)
print "Hydra FTP Dictionary Created!\n"
#sleep(1)
HydraSSHDict = ngramsDictionary(AllHydraSSH.split(),n)
print "Hydra SSH Dictionary Created!\n"
#sleep(1)
JavaMetrDict = ngramsDictionary(AllJavaMetr.split(),n)
print "Java Meterpreter Dictionary Created!\n"
#sleep(1)
MetrDict = ngramsDictionary(AllMeterpreter.split(),n)
print "Meterpreter Dictionary Created!\n"
#sleep(1)
WebShellDict = ngramsDictionary(AllWebShell.split(),n)
print "Webshell Dictionary Created!\n"
#sleep(1)
NormalDict = ngramsDictionary(AllNormal.split(),n)
print "Normal Dictionary Created!\n"
#sleep(1)

print "\nCreating Data for Dictionaries ...\n"
#sleep(1)
allDicts = [addUserDict,HydraFTPDict,HydraSSHDict,JavaMetrDict,MetrDict,WebShellDict,NormalDict]
# top30Adduser = []
# top30HydraFTP = []
# top30HydraSSH = []
# top30JavaMetr = []
# top30Metr = []
# top30Webshell = []
# top30Normal = []

# top30Data = [top30Adduser,top30HydraFTP,top30HydraSSH,top30JavaMetr,top30Metr,top30Webshell,top30Normal]

#MAXENTRY = 90000

#sys.stdout.write("Please enter the threshold frequency for consideration: ")
#sentinel = int(raw_input())
'''
for i in range(len(allDicts)):
    dict1 = allDicts[i]
    Ltot = len(dict1)
    c=0
    sentinel = Ltot*0.3
    top30 = top30Data[i]
    print "Creating top 30% arrays of tuples for "+attackType[i]+" . . .\n"
    #sleep(1)
    sortedDictArray = countSort(dict1,MAXENTRY)#sorted(dict1.iteritems(), key=lambda (k,v): (v,k), reverse=True)
    for key, value in sortedDictArray:
        c+=1
        if(sentinel >= c):
            try:
                temp1 = addUserDict[key]+HydraFTPDict[key]+HydraSSHDict[key]+JavaMetrDict[key]+MetrDict[key]+WebShellDict[key]+NormalDict[key]
                top30.append(key)
            except:
                pass
'''
###################################
filesInDir = os.listdir("./")
k=1
string1 ="TEST_DATASET_"+str(k)+".arff"
while string1 in filesInDir:
    k+=1
    string1 = "TEST_DATASET_"+str(k)+".arff"
finalFile = open(string1,"a+")
print "--------------------------------------------------------\nCreating DATASET . . ."
#sleep(3)
##################################
'''
addUserTop = open("top30TestAddUser.txt","a+")
HydraFTPTop = open("top30TestHydraFTP.txt","a+")
HydraSSHTop = open("top30TestHydraSSH.txt","a+")
JavaMeterpreterTop = open("top30TestJavaMeterpreter.txt","a+")
MeterpreterTop = open("top30TestMeterpreter.txt","a+")
WebShellTop = open("top30TestWebShell.txt","a+")
NormalTop = open("top30TestNormal.txt","a+")

for i in top30Adduser:      
    addUserTop.write(str(i)+" -> "+str(addUserDict[i])+"\n")

for i in top30HydraFTP:
    HydraFTPTop.write(str(i)+" -> "+str(HydraFTPDict[i])+"\n")

for i in top30HydraSSH:
    HydraSSHTop.write(str(i)+" -> "+str(HydraSSHDict[i])+"\n")

for i in top30JavaMetr:
    JavaMeterpreterTop.write(str(i)+" -> "+str(JavaMetrDict[i])+"\n")

for i in top30Metr:
    MeterpreterTop.write(str(i)+" -> "+str(MetrDict[i])+"\n")

for i in top30Webshell:
    WebShellTop.write(str(i)+" -> "+str(WebShellDict[i])+"\n")

for i in top30Normal:
    NormalTop.write(str(i)+" -> "+str(NormalDict[i])+"\n")
'''
##################################

'''
features = []
for i in range(len(top30Data)):
    for j in top30Data[i]:
        if j not in features:
            features.append(j)
    print str(len(top30Data[i])) + " --> " +attackType[i]
'''
features = []
############# 'unk' features #################
string3 = "featureVector"+str(n)+"-Grams.txt"
try:
    trainFeaturesFile = open(string3,"r")
except:
    print "First Run the training for "+str(n)+"-grams"
    sys.exit(1)
featureFileString = trainFeaturesFile.read()
tempList = featureFileString.rstrip().split("\n")

for i in tempList:
    tup = tuple(i.split())
    features.append(tup)

##############################

string2 = ""
for l in range(1,len(features)+1):
    string2+="@attribute feature" + str(l) + " numeric\n"
configString = "@relation KDDTrain-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.supervised.instance.Resample-B0.0-S1-Z18.0-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.supervised.instance.SMOTE-C2-K5-P1000.0-S1-weka.filters.supervised.instance.SMOTE-C2-K5-P500.0-S1-weka.filters.supervised.instance.SMOTE-C2-K5-P125.0-S1-weka.filters.supervised.instance.SMOTE-C3-K5-P500.0-S1-weka.filters.supervised.instance.SMOTE-C3-K5-P150.0-S1-weka.filters.supervised.instance.SMOTE-C4-K5-P800.0-S1-weka.filters.unsupervised.instance.Randomize-S42\n"+string2+"@attribute class {adduser,hydraftp,hydrassh,javameter,meterpreter,webshell,normal}\n\n@data\n"
finalFile.write(configString)

dataSet1=""    
dataSet2=""    
dataSet3=""    
dataSet4=""    
dataSet5=""    
dataSet6=""
dataSet7=""        

threshold = 0
ignored = 0
for i in range(noOfAddUserFiles):       #O(k*m) k:no. of files m:no. of features
    countNonZero = 0
    tempStr = ""
    for j in range(len(features)):          #Here, 6918*1338 = 9200000
        try:
            tempStr+=str(AddUserFilesDict[i][features[j]])+", "
            countNonZero+=1
        except:
            tempStr += str(0) + ", "
    tempStr+="adduser\n"
    if(countNonZero>threshold*len(features)):
        dataSet1+=tempStr
    else:
        ignored+=1
finalFile.write(dataSet1)

for i in range(noOfHydraFTPFiles):
    countNonZero = 0
    tempStr = ""
    for j in range(len(features)):          #Here, 6918*1338 = 9200000
        try:
            tempStr+=str(HydraFTPFilesDict[i][features[j]])+", "
            countNonZero+=1
        except:
            tempStr += str(0) + ", "
    tempStr+="hydraftp\n"
    if(countNonZero>threshold*len(features)):
        dataSet2+=tempStr
    else:
        ignored+=1
finalFile.write(dataSet2)

for i in range(noOfHydraSSHFiles):
    countNonZero = 0
    tempStr = ""
    for j in range(len(features)):          #Here, 6918*1338 = 9200000
        try:
            tempStr+=str(HydraSSHFilesDict[i][features[j]])+", "
            countNonZero+=1
        except:
            tempStr += str(0) + ", "
    tempStr+="hydrassh\n"
    if(countNonZero>threshold*len(features)):
        dataSet3+=tempStr
    else:
        ignored+=1
finalFile.write(dataSet3)

for i in range(noOfJavaMetrFiles):
    countNonZero = 0
    tempStr = ""
    for j in range(len(features)):          #Here, 6918*1338 = 9200000
        try:
            tempStr+=str(JavaMetrFilesDict[i][features[j]])+", "
            countNonZero+=1
        except:
            tempStr += str(0) + ", "
    tempStr+="javameter\n"
    if(countNonZero>threshold*len(features)):
        dataSet4+=tempStr
    else:
        ignored+=1
finalFile.write(dataSet4)

for i in range(noOfMeterpreterFiles):
    countNonZero = 0
    tempStr = ""
    for j in range(len(features)):          #Here, 6918*1338 = 9200000
        try:
            tempStr+=str(MeterpreterFilesDict[i][features[j]])+", "
            countNonZero+=1
        except:
            tempStr += str(0) + ", "
    tempStr+="meterpreter\n"
    if(countNonZero>threshold*len(features)):
        dataSet5+=tempStr
    else:
        ignored+=1
finalFile.write(dataSet5)

for i in range(noOfWebShellFiles):
    countNonZero = 0
    tempStr = ""
    for j in range(len(features)):          #Here, 6918*1338 = 9200000
        try:
            tempStr+=str(WebshellFilesDict[i][features[j]])+", "
            countNonZero+=1
        except:
            tempStr += str(0) + ", "
    tempStr+="webshell\n"
    if(countNonZero>threshold*len(features)):
        dataSet6+=tempStr
    else:
        ignored+=1
finalFile.write(dataSet6)

for i in range(noOfNormalFiles):
    countNonZero = 0
    tempStr = ""
    for j in range(len(features)):          #Here, 6918*1338 = 9200000
        try:
            tempStr+=str(NormaFilesDict[i][features[j]])+", "
            countNonZero+=1
        except:
            tempStr += str(0) + ", "
    tempStr+="normal\n"
    if(countNonZero>threshold*len(features)):
        dataSet7+=tempStr
    else:
        ignored+=1
finalFile.write(dataSet7)

print "###################################################################################"
print "TEST DATASET Created in file "+ string1 +" !!!"
print "Dataset Specifications :\n"
print "------------------------------------------------------------"
print "Dataset Name : Attack Recognition Dataset for testing. . ."
print "No. of attributes :",len(features)
print "No. of ignored instances : ",ignored
print "No. of instances :",noOfAddUserFiles+noOfHydraFTPFiles+noOfHydraSSHFiles+noOfMeterpreterFiles+noOfWebShellFiles+noOfJavaMetrFiles+noOfNormalFiles - ignored
classes = "Classes in Dataset : "
for i in attackType:
    classes += "| "+i+" |"
print classes
print "-------------------------------------------------------------"
print "################################################################################"