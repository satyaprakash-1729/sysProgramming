from myLib1729 import *
from time import sleep
import os,sys

print "\n\nReading Input Files ...\n"
#sleep(1)
attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack", "Normal"]

fAddUser = open("totTrainAdduser.txt","r")
fHydraFTP = open("totTrainHydraFTP.txt","r")
fHydraSSH = open("totTrainHydraSSH.txt","r")
fJavaMetr = open("totTrainJavaMetr.txt","r")
fMetr = open("totTrainMeterpreter.txt","r")
fWebShell = open("totTrainWebShell.txt","r")
fNormal = open("totTrainDataNormal2.txt","r")

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

for i in AddUserData:       #O(n) : n = total no. of numbers
    AllAddUser += i             #Here, ~830000
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
addUserDict = ngramsDictionary(AllAddUser.split(),n)    #O(n) - 830000
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
top30Adduser = []
top30HydraFTP = []
top30HydraSSH = []
top30JavaMetr = []
top30Metr = []
top30Webshell = []
top30Normal = []

top30Data = [top30Adduser,top30HydraFTP,top30HydraSSH,top30JavaMetr,top30Metr,top30Webshell,top30Normal]

#sys.stdout.write("Please enter the threshold frequency for consideration: ")
#sentinel = int(raw_input())
for i in range(len(allDicts)):
    dict1 = allDicts[i]
    Ltot = len(dict1)
    c=0
    sentinel = Ltot*0.3
    top30 = top30Data[i]
    print "Creating top 30% arrays of tuples for "+attackType[i]+" . . .\n"
    #sleep(1)
    sortedDictArray = sorted(dict1.iteritems(), key=lambda (k,v): (v,k), reverse=True)      #O(nlogn) ~ 4900000
    for key, value in sortedDictArray:      #O(n) - 830000
        c+=1
        if(sentinel >= c):
            try:
                temp1 = addUserDict[key]+HydraFTPDict[key]+HydraSSHDict[key]+JavaMetrDict[key]+MetrDict[key]+WebShellDict[key]+NormalDict[key]
                #temp1 = [fileDict[key] for fileDict in AddUserFilesDict]+[fileDict[key] for fileDict in HydraFTPFilesDict]+[fileDict[key] for fileDict in HydraSSHFilesDict]+[fileDict[key] for fileDict in JavaMetrFilesDict]+[fileDict[key] for fileDict in MeterpreterFilesDict]+[fileDict[key] for fileDict in WebshellFilesDict]+[fileDict[key] for fileDict in NormaFilesDict]
                top30.append(key)
            except:
                pass

###################################
filesInDir = os.listdir("./")
k=1
string1 ="DATASET_"+str(k)+".arff"
while string1 in filesInDir:
    k+=1
    string1 = "DATASET_"+str(k)+".arff"
finalFile = open(string1,"a+")
print "--------------------------------------------------------\nCreating DATASET . . ."
#sleep(3)

features = []

for i in range(len(top30Data)):
    features+=top30Data[i]
    print str(len(top30Data[i])) + " --> " +attackType[i]

string3 = "featureVector"+str(n)+"-Grams.txt"
featureFile = open(string3,"w+")
for i in features:
    for j in i:
        featureFile.write(str(j)+" ")
    featureFile.write("\n")

###############################
'''
addUserTop = open("top30AddUser.txt","a+")
HydraFTPTop = open("top30HydraFTP.txt","a+")
HydraSSHTop = open("top30HydraSSH.txt","a+")
JavaMeterpreterTop = open("top30JavaMeterpreter.txt","a+")
MeterpreterTop = open("top30Meterpreter.txt","a+")
WebShellTop = open("top30WebShell.txt","a+")
NormalTop = open("top30Normal.txt","a+")

for i in top30Adduser:      
    addUserTop.write(str(i)+"\n")

for i in top30HydraFTP:
    HydraFTPTop.write(str(i)+"\n")

for i in top30HydraSSH:
    HydraSSHTop.write(str(i)+"\n")

for i in top30JavaMetr:
    JavaMeterpreterTop.write(str(i)+"\n")

for i in top30Metr:
    MeterpreterTop.write(str(i)+"\n")

for i in top30Webshell:
    WebShellTop.write(str(i)+"\n")

for i in top30Normal:
    NormalTop.write(str(i)+"\n")
'''
###############################
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
for i in range(noOfAddUserFiles):       #O(k*m) k:no. of files m:no. of features
    for j in range(len(features)):          #Here, 6918*1338 = 9200000
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

for i in range(noOfNormalFiles):
    for j in range(len(features)):
        try:
            dataSet7+=str(NormaFilesDict[i][features[j]])+", "
        except:
            dataSet7 += str(0) + ", "
    dataSet7+="normal\n"
finalFile.write(dataSet7)

print "###################################################################################"
print "DATASET Created in file "+ string1 +" !!!"
print "Dataset Specifications :\n"
print "------------------------------------------------------------"
print "Dataset Name : Attack Recognition Dataset"
print "No. of attributes :",len(features)
print "No. of instances :",noOfAddUserFiles+noOfHydraFTPFiles+noOfHydraSSHFiles+noOfMeterpreterFiles+noOfWebShellFiles+noOfJavaMetrFiles+noOfNormalFiles
classes = "Classes in Dataset : "
for i in attackType:
    classes += " "+i+" "
print classes
print "-------------------------------------------------------------"
print "################################################################################"

##################################
#O(n) ~ 830000
#O(n) ~ 830000
#O(nlogn) ~ 4900000
#O(n) ~ 830000
#O(k*m) ~ 9200000
#---------------
#O(k*m) ~ 14000000 ~ 10^7
##################################