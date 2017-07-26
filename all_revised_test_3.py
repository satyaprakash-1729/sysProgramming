print "\n\nReading Input Files ...\n"
#sleep(1)
attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack", "Normal"]
flistList = ["adduser.txt","hydrassh.txt","hydraftp.txt","javametr.txt","metr.txt","webshell.txt"]
outList = ["totTestAdduser2.txt","totTestHydraSSH2.txt","totTestHydraFTP2.txt","totTestJavaMetr2.txt","totTestMeterpreter2.txt","totTestWebShell2.txt"]
sentL = ["./Adduser_", "./Hydra_SSH_", "./Hydra_FTP_", "./Java_Meterpreter_", "./Meterpreter_", "./Web_Shell_"]

for index in range(len(sentL)):
    sent = sentL[index]
    flist = open(flistList[index],"r")
    out = open(outList[index],"w+")
    a = flist.read().splitlines()
    print "Concatenating " + outList[index] + " files data together . . . "
    for f in a:
        if f.startswith(sent+"8")==True or f.startswith(sent + "9")==True or f.startswith(sent + "10")==True:
            fileo = open(f,"r")
            r = fileo.read()
            out.write(r)
            out.write("-1 ")
            sys.stdout.write(attackType[index]+" ("+f+") data written to "+outList[index]+" \n")

out = open("totTestDataValidation2.txt","w+")

sys.stdout.write("Concatenating all normal test data files ...\n")

for f in os.listdir("../../Validation Data/Validation_Data_Master (copy)/"):
    if f.startswith("UVD"):
        fileRead = open("../../Validation Data/Validation_Data_Master (copy)/" + f,"r")
        inp = fileRead.read()
        out.write(inp)
        out.write("-1 ")

fAddUser = open("totTestAdduser2.txt","r")
fHydraFTP = open("totTestHydraFTP2.txt","r")
fHydraSSH = open("totTestHydraSSH2.txt","r")
fJavaMetr = open("totTestJavaMetr2.txt","r")
fMetr = open("totTestMeterpreter2.txt","r")
fWebShell = open("totTestWebShell2.txt","r")
fNormal = open("totTestDataValidation2.txt","r")

# sys.stdout.write("What Weight do u want to use for ngrams division? ")
# n = int(raw_input())

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

print "Deleting Temporary Data Files . . ."
for i in outList:
    os.system("sudo rm "+i)
os.system("sudo rm totTestDataValidation2.txt")

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
filesInDir = os.listdir("./")
k=1
string1 ="TEST_DATASET_"+str(k)+".arff"
while string1 in filesInDir:
    k+=1
    string1 = "TEST_DATASET_"+str(k)+".arff"
finalFile = open(string1,"w+")
print "--------------------------------------------------------\nCreating DATASET . . ."

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