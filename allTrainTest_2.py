from myLib1729 import *
import os,sys


def trainDataset(n, threshold):
    print "\n\nReading Input Files ...\n"
    attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack", "Normal"]
    AddUserString = ""
    HydraSSHString = ""
    HydraFTPString = ""
    JavaMetrString = ""
    MeterpreterString = ""
    WebshellString = ""
    NormalString = ""
    attackStrings = [AddUserString, HydraFTPString, HydraSSHString, JavaMetrString, MeterpreterString, WebshellString,NormalString]
    
    flistList = ["adduser.txt","hydrassh.txt","hydraftp.txt","javametr.txt","metr.txt","webshell.txt"]
    sentL = ["./Adduser_", "./Hydra_SSH_", "./Hydra_FTP_", "./Java_Meterpreter_", "./Meterpreter_", "./Web_Shell_"]
    
    print "Concatenating Training files data together . . .\n "
    for index in range(len(sentL)):
        sent = sentL[index]
        flist = open(flistList[index],"r")
        a = flist.read().splitlines()
        for f in a:
            if f.startswith(sent+"8")==False and f.startswith(sent + "9")==False and f.startswith(sent + "10")==False:
                fileo = open(f,"r")
                r = fileo.read()
                attackStrings[index] += (r + "-1 ")

    for f in os.listdir("../../Training Data/Training_Data_Master (copy)/"):
        if f.startswith("UTD"):
            fileRead = open("../../Training Data/Training_Data_Master (copy)/" + f,"r")
            inp = fileRead.read()
            NormalString += (inp + "-1 ")

    print "Creating individual file records..."
     
    AddUserData = attackStrings[0].split("-1")[:-1]                    #Split the different files' records
    HydraSSHData = attackStrings[2].split("-1")[:-1]
    HydraFTPData = attackStrings[1].split("-1")[:-1]
    JavaMetrData = attackStrings[3].split("-1")[:-1]
    MeterpreterData = attackStrings[4].split("-1")[:-1]
    WebshellData = attackStrings[5].split("-1")[:-1]
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


    print "\nCreating ngrams dictionaries for all files. Please Wait ...\n"           #Create Total data Dictionary
    addUserDict = ngramsDictionary(AllAddUser.split(),n)    #O(n) 
    HydraFTPDict = ngramsDictionary(AllHydraFTP.split(),n)
    HydraSSHDict = ngramsDictionary(AllHydraSSH.split(),n)
    JavaMetrDict = ngramsDictionary(AllJavaMetr.split(),n)
    MetrDict = ngramsDictionary(AllMeterpreter.split(),n)
    WebShellDict = ngramsDictionary(AllWebShell.split(),n)
    NormalDict = ngramsDictionary(AllNormal.split(),n)

    print "\nCreating Data for Dictionaries ...\n"
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
        sortedDictArray = countSort(dict1,MAXENTRY)#sorted(dict1.iteritems(), key=lambda (k,v): (v,k), reverse=True)      #O(nlogn)
        for key, value in sortedDictArray:      #O(n)
            c+=1
            if(sentinel > c):
                top30.append(key)
                # try:
                #     #temp1 = addUserDict[key]+HydraFTPDict[key]+HydraSSHDict[key]+JavaMetrDict[key]+MetrDict[key]+WebShellDict[key]+NormalDict[key]
                #     top30.append(key)
                # except:
                #     pass

    featuresDict = {}
    features = []
    for i in range(len(top30Data)):                                 #Create Feature Vector
        print len(top30Data[i])
        for j in top30Data[i]:
            featuresDict[j] = 1

    features = featuresDict.keys()

    # string3 = "featureVector"+str(n)+"-Grams.txt"       #Write Feature Vector in file
    # featureFile = open(string3,"w+")
    # for i in features:
    #     for j in i:
    #         featureFile.write(str(j)+" ")
    #     featureFile.write("\n")

    filesInDir = os.listdir("./")
    k=1
    string1 ="DATASET_"+str(k)+"_"+ str(n) +"-grams_" + "attr" + str(len(features))+".arff"
    while string1 in filesInDir:
        k+=1
        string1 = "DATASET_"+str(k)+"_"+ str(n) +"-grams_" + "attr" + str(len(features))+".arff"

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
                                      #Create the final dataaset by finding the corresponding frequency in the individual files
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
    if ignored!=0:
        print "No. of ignored instances: ",ignored
    print "No. of instances :",noOfAddUserFiles+noOfHydraFTPFiles+noOfHydraSSHFiles+noOfMeterpreterFiles+noOfWebShellFiles+noOfJavaMetrFiles+noOfNormalFiles - ignored
    classes = "Classes in Dataset : "
    for i in attackType:
        classes += i+", "
    print classes[:-2]
    print "-------------------------------------------------------------"
    print "################################################################################"
    return features

def testDataset(n, features, threshold):
    AddUserString = ""
    HydraSSHString = ""
    HydraFTPString = ""
    JavaMetrString = ""
    MeterpreterString = ""
    WebshellString = ""
    NormalString = ""
    attackStrings = [AddUserString, HydraFTPString, HydraSSHString, JavaMetrString, MeterpreterString, WebshellString,NormalString]
    attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack", "Normal"]
    flistList = ["adduser.txt","hydrassh.txt","hydraftp.txt","javametr.txt","metr.txt","webshell.txt"]
    sentL = ["./Adduser_", "./Hydra_SSH_", "./Hydra_FTP_", "./Java_Meterpreter_", "./Meterpreter_", "./Web_Shell_"]
    print "\n\nReading Input Files ...\n"
    for index in range(len(sentL)):
        sent = sentL[index]
        flist = open(flistList[index],"r")
        a = flist.read().splitlines()
        ###print "Concatenating " + outList[index] + " files data together . . . "
        for f in a:
            if f.startswith(sent+"8")==True or f.startswith(sent + "9")==True or f.startswith(sent + "10")==True:
                fileo = open(f,"r")
                r = fileo.read()
                attackStrings[index] += (r + "-1 ")

    for f in os.listdir("../../Validation Data/Validation_Data_Master (copy)/"):
        if f.startswith("UVD"):
            fileRead = open("../../Validation Data/Validation_Data_Master (copy)/" + f,"r")
            inp = fileRead.read()
            NormalString += (inp+"-1 ")
    print "Creating individual file records..."
     
    AddUserData = attackStrings[0].split("-1")[:-1]                    #Split the different files' records
    HydraSSHData = attackStrings[2].split("-1")[:-1]
    HydraFTPData = attackStrings[1].split("-1")[:-1]
    JavaMetrData = attackStrings[3].split("-1")[:-1]
    MeterpreterData = attackStrings[4].split("-1")[:-1]
    WebshellData = attackStrings[5].split("-1")[:-1]
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


    addUserDict = ngramsDictionary(AllAddUser.split(),n)
     
    HydraFTPDict = ngramsDictionary(AllHydraFTP.split(),n)
     
    HydraSSHDict = ngramsDictionary(AllHydraSSH.split(),n)
     
    JavaMetrDict = ngramsDictionary(AllJavaMetr.split(),n)
     
    MetrDict = ngramsDictionary(AllMeterpreter.split(),n)
     
    WebShellDict = ngramsDictionary(AllWebShell.split(),n)
     
    NormalDict = ngramsDictionary(AllNormal.split(),n)     

    print "\nCreating Data for Dictionaries ...\n"
     
    allDicts = [addUserDict,HydraFTPDict,HydraSSHDict,JavaMetrDict,MetrDict,WebShellDict,NormalDict]
    filesInDir = os.listdir("./")
    k=1
    string1 ="TEST_DATASET_"+str(k)+"_"+ str(n) +"-grams_" + "attr" + str(len(features))+".arff"
    while string1 in filesInDir:
        k+=1
        string1 = "TEST_DATASET_"+str(k)+"_"+ str(n) +"-grams_" + "attr" + str(len(features))+".arff"
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
    if ignored!=0:
        print "No. of ignored instances : ",ignored
    print "No. of instances :",noOfAddUserFiles+noOfHydraFTPFiles+noOfHydraSSHFiles+noOfMeterpreterFiles+noOfWebShellFiles+noOfJavaMetrFiles+noOfNormalFiles - ignored
    classes = "Classes in Dataset : "
    for i in attackType:
        classes += i+", "
    print classes[:-2]
    print "-------------------------------------------------------------"
    print "################################################################################"



sys.stdout.write("What Weight do u want to use for ngrams division? ")
n = int(raw_input())

print "TRAINING DATASET CREATION STARTED . . ."
features1 = trainDataset(n, 0)
print "TRAINING  DATASET CREATION COMPLETED\n----------------------------------------------------\nTEST  DATASET CREATION STARTED . . ."
#testDataset(n, features1, 0)
print "TEST  DATASET CREATION COMPLETED"