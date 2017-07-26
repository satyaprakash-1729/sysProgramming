from myLib1729 import *
from time import sleep
import os,sys


#sleep(1)
#sys.stdout.write("What Weight do u want to use for ngrams division? ")
n = 3#int(raw_input())

def trainDataset(n):
    print "\n\nReading Input Files ...\n"
    attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack", "Normal"]

    #attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack"]
    flistList = ["adduser.txt","hydrassh.txt","hydraftp.txt","javametr.txt","metr.txt","webshell.txt"]
    outList = ["totTrainAdduser2.txt","totTrainHydraSSH2.txt","totTrainHydraFTP2.txt","totTrainJavaMetr2.txt","totTrainMeterpreter2.txt","totTrainWebShell2.txt"]
    sentL = ["./Adduser_", "./Hydra_SSH_", "./Hydra_FTP_", "./Java_Meterpreter_", "./Meterpreter_", "./Web_Shell_"]
    print "Concatenating Training files data together . . . "
    for index in range(len(sentL)):
        sent = sentL[index]
        flist = open(flistList[index],"r")
        out = open(outList[index],"w+")
        a = flist.read().splitlines()
        ###print "Concatenating " + outList[index] + " files data together . . . "
        for f in a:
            if f.startswith(sent+"8")==False and f.startswith(sent + "9")==False and f.startswith(sent + "10")==False:
                fileo = open(f,"r")
                r = fileo.read()
                out.write(r)
                out.write("-1 ")
                #sys.stdout.write(attackType[index]+" ("+f+") data written to "+outList[index]+" \n")

    print("Concatenating all normal data files ...")
    out = open("totTrainDataNormal3.txt","w+")

    for f in os.listdir("../../Training Data/Training_Data_Master (copy)/"):
        if f.startswith("UTD"):
            fileRead = open("../../Training Data/Training_Data_Master (copy)/" + f,"r")
            inp = fileRead.read()
            out.write(inp)
            out.write("-1 ")

    fAddUser = open("totTrainAdduser2.txt","r")
    fHydraFTP = open("totTrainHydraFTP2.txt","r")
    fHydraSSH = open("totTrainHydraSSH2.txt","r")
    fJavaMetr = open("totTrainJavaMetr2.txt","r")
    fMetr = open("totTrainMeterpreter2.txt","r")
    fWebShell = open("totTrainWebShell2.txt","r")
    fNormal = open("totTrainDataNormal3.txt","r")

    AddUserString = fAddUser.read()
    HydraSSHString = fHydraSSH.read()
    HydraFTPString = fHydraFTP.read()
    JavaMetrString = fJavaMetr.read()
    MeterpreterString = fMetr.read()
    WebshellString = fWebShell.read()
    NormalString = fNormal.read()

    print "Deleting Temporary Data Files . . ."
    for i in outList:
        os.system("sudo rm "+i)
    os.system("sudo rm totTrainDataNormal3.txt")

    print "Creating individual file records..."
    #sleep(1)
    AddUserData = AddUserString.split("-1")[:-1]                    #Split the different files' records
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

    numbersOfFiles = [noOfAddUserFiles,noOfHydraFTPFiles, noOfHydraSSHFiles, noOfJavaMetrFiles,noOfMeterpreterFiles,noOfWebShellFiles,noOfNormalFiles]

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

    for i in AddUserData:                                                                   #O(n) : n = total no. of numbers
        AllAddUser += i                                                                         #Concatenate all files' data
        AddUserFilesDict.append(ngramsDictionary(i.split(),n))              #Create individual files' dictionary for dataset creation

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


    print "\n\nCreating ngrams dictionaries for all files. Please Wait ...\n"           #Create Total data Dictionary
    addUserDict = ngramsDictionary(AllAddUser.split(),n)    #O(n)
    ###print "Add User Dictionary Created!\n"
    #sleep(1)
    HydraFTPDict = ngramsDictionary(AllHydraFTP.split(),n)
    ###print "Hydra FTP Dictionary Created!\n"
    #sleep(1)
    HydraSSHDict = ngramsDictionary(AllHydraSSH.split(),n)
    ###print "Hydra SSH Dictionary Created!\n"
    #sleep(1)
    JavaMetrDict = ngramsDictionary(AllJavaMetr.split(),n)
    ###print "Java Meterpreter Dictionary Created!\n"
    #sleep(1)
    MetrDict = ngramsDictionary(AllMeterpreter.split(),n)
    ###print "Meterpreter Dictionary Created!\n"
    #sleep(1)
    WebShellDict = ngramsDictionary(AllWebShell.split(),n)
    ###print "Webshell Dictionary Created!\n"
    #sleep(1)
    NormalDict = ngramsDictionary(AllNormal.split(),n)
    ###print "Normal Dictionary Created!\n"
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

    MAXENTRY = 25000

    for i in range(len(allDicts)):                          #Find the top 30% data
        dict1 = allDicts[i]
        Ltot = len(dict1)
        c=0
        sentinel = Ltot*0.3
        top30 = top30Data[i]
        ###print "Creating top 30% arrays of tuples for "+attackType[i]+" . . .\n"
        #sleep(1)
        sortedDictArray = sorted(dict1.iteritems(), key=lambda (k,v): (v,k), reverse=True)      #O(nlogn)
        for key, value in sortedDictArray:      #O(n)
            c+=1
            if(sentinel > c):
                top30.append(key)
                # try:
                #     #temp1 = addUserDict[key]+HydraFTPDict[key]+HydraSSHDict[key]+JavaMetrDict[key]+MetrDict[key]+WebShellDict[key]+NormalDict[key]
                #     #temp1 = [fileDict[key] for fileDict in AddUserFilesDict]+[fileDict[key] for fileDict in HydraFTPFilesDict]+[fileDict[key] for fileDict in HydraSSHFilesDict]+[fileDict[key] for fileDict in JavaMetrFilesDict]+[fileDict[key] for fileDict in MeterpreterFilesDict]+[fileDict[key] for fileDict in WebshellFilesDict]+[fileDict[key] for fileDict in NormaFilesDict]
                #     top30.append(key)
                # except:
                #     pass

    ###################################

    featuresDict = {}
    features = []

    for i in range(len(top30Data)):                                 #Create Feature Vector
        for j in top30Data[i]:
            featuresDict[j] = 1
        ###print str(len(top30Data[i])) + " --> " +attackType[i]

    features = featuresDict.keys()

    string3 = "featureVector"+str(n)+"-Grams.txt"       #Write Feature Vector in file
    featureFile = open(string3,"w+")
    for i in features:
        for j in i:
            featureFile.write(str(j)+" ")
        featureFile.write("\n")

    filesInDir = os.listdir("./")
    k=1
    string1 ="DATASET_"+str(k)+"_"+ str(n) +"-grams_" + "attr" + str(len(features))+".arff"
    while string1 in filesInDir:
        k+=1
        string1 = "DATASET_"+str(k)+"_"+ str(n) +"-grams_" + "attr" + str(len(features))+".arff"

    finalFile = open(string1,"w+")
    print "--------------------------------------------------------\nCreating DATASET . . ."
    #sleep(3)
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

    threshold = 0                                       #Create the final dataaset by finding the corresponding frequency in the individual files
    ignored = 0
    for i in range(noOfAddUserFiles):       #O(k*m) k:no. of files m:no. of features
        countNonZero = 0
        tempStr = ""
        for j in range(len(features)): 
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
        for j in range(len(features)): 
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
        for j in range(len(features)): 
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
        for j in range(len(features)):
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
        for j in range(len(features)): 
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
        for j in range(len(features)): 
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
        for j in range(len(features)):
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
    print "DATASET Created in file "+ string1 +" !!!"
    print "Dataset Specifications :\n"
    print "------------------------------------------------------------"
    print "Dataset Name : Attack Recognition Dataset"
    print "No. of attributes :",len(features)
    print "No. of ignored instances: ",ignored
    print "No. of instances :",noOfAddUserFiles+noOfHydraFTPFiles+noOfHydraSSHFiles+noOfMeterpreterFiles+noOfWebShellFiles+noOfJavaMetrFiles+noOfNormalFiles - ignored
    classes = "Classes in Dataset : "
    for i in attackType:
        classes += "| "+i+" |"
    print classes
    print "-------------------------------------------------------------"
    print "################################################################################"
    return features

def testDataset(n, features):
    #sleep(1)
    attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack", "Normal"]
    flistList = ["adduser.txt","hydrassh.txt","hydraftp.txt","javametr.txt","metr.txt","webshell.txt"]
    outList = ["totTestAdduser2.txt","totTestHydraSSH2.txt","totTestHydraFTP2.txt","totTestJavaMetr2.txt","totTestMeterpreter2.txt","totTestWebShell2.txt"]
    sentL = ["./Adduser_", "./Hydra_SSH_", "./Hydra_FTP_", "./Java_Meterpreter_", "./Meterpreter_", "./Web_Shell_"]
    print "\n\nReading Input Files ...\n"
    for index in range(len(sentL)):
        sent = sentL[index]
        flist = open(flistList[index],"r")
        out = open(outList[index],"w+")
        a = flist.read().splitlines()
        ###print "Concatenating " + outList[index] + " files data together . . . "
        for f in a:
            if f.startswith(sent+"8")==True or f.startswith(sent + "9")==True or f.startswith(sent + "10")==True:
                fileo = open(f,"r")
                r = fileo.read()
                out.write(r)
                out.write("-1 ")
                print(attackType[index]+" ("+f+") data written to "+outList[index])

    out = open("totTestDataValidation2.txt","w+")

    print("Concatenating all normal test data files ...")

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


    ###print "\n\nCreating ngrams dictionaries for all files. Please Wait ...\n"
    addUserDict = ngramsDictionary(AllAddUser.split(),n)
    ###print "Add User Dictionary Created!\n"
    #sleep(1)
    HydraFTPDict = ngramsDictionary(AllHydraFTP.split(),n)
    ###print "Hydra FTP Dictionary Created!\n"
    #sleep(1)
    HydraSSHDict = ngramsDictionary(AllHydraSSH.split(),n)
    ###print "Hydra SSH Dictionary Created!\n"
    #sleep(1)
    JavaMetrDict = ngramsDictionary(AllJavaMetr.split(),n)
    ###print "Java Meterpreter Dictionary Created!\n"
    #sleep(1)
    MetrDict = ngramsDictionary(AllMeterpreter.split(),n)
    ###print "Meterpreter Dictionary Created!\n"
    #sleep(1)
    WebShellDict = ngramsDictionary(AllWebShell.split(),n)
    ###print "Webshell Dictionary Created!\n"
    #sleep(1)
    NormalDict = ngramsDictionary(AllNormal.split(),n)
    ###print "Normal Dictionary Created!\n"
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
    print "################################################################################"

features1 = trainDataset(n)
testDataset(n, features1)