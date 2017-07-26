from myLib1729 import *
import os,sys
from time import sleep
import time
from multiprocessing import Pool, freeze_support

def writeFeaturesInFile(n, features):
    string3 = "featureVector"+str(n)+"-Grams.txt"       #Write Feature Vector in file
    featureFile = open(string3,"w+")
    for i in features:
        for j in i:
            featureFile.write(str(j)+" ")
        featureFile.write("\n")

def DictCalc(threadName, n, stringArray):
    print ("Thread running : "+threadName)
    FilesDict = []
    AllData = ""
    for i in stringArray:
        AllData+=i
        FilesDict.append(ngramsDictionary(i.split(),n))
    AttackDict = ngramsDictionary(AllData.split(),n)
    MAXENTRY = 25000
    Ltot = len(AttackDict)
    c=0
    sentinel = Ltot*0.3
    top30 = []
    sortedDictArray = countSort(AttackDict,MAXENTRY)#sorted(dict1.iteritems(), key=lambda (k,v): (v,k), reverse=True)      #O(nlogn)
    for key, value in sortedDictArray:      #O(n)
        c+=1
        if(sentinel > c):
            top30.append(key)
    return top30, len(stringArray), FilesDict

def DictCalc2(threadName, n, stringArray):
    print ("Thread running : "+threadName)
    FilesDict = []
    for i in stringArray:
        FilesDict.append(ngramsDictionary(i.split(),n))
    return len(stringArray), FilesDict

def createDataset(noOfFiles, threshold, finalFile, ignored, FilesDict, features):
    dataSet1=""
    for i in range(noOfFiles):       #O(k*m) k:no. of files m:no. of features
        countNonZero = 0
        tempStr = ""
        for j in range(len(features)):          #Here, 6918*1338 = 9200000
            try:
                tempStr+=str(FilesDict[i][features[j]])+", "
                countNonZero+=1
            except:
                tempStr += str(0) + ", "
        tempStr+="adduser\n"
        if(countNonZero>threshold*len(features)):
            dataSet1+=tempStr
        else:
            ignored+=1
    finalFile.write(dataSet1)
    return ignored

def fileInitialize(features, train):
    filesInDir = os.listdir("./")
    k=1
    word = ""
    if(train == True):
        word = ""
    else:
        word = "TEST_"
    string1 =word+"DATASET_"+str(k)+"_"+ str(n) +"-grams_" + "attr" + str(len(features))+".arff"
    while string1 in filesInDir:
        k+=1
        string1 = word+"DATASET_"+str(k)+"_"+ str(n) +"-grams_" + "attr" + str(len(features))+".arff"
    finalFile = open(string1,"w+")
    print ("--------------------------------------------------------\nCreating DATASET . . .")

    string2 = ""
    for l in range(1,len(features)+1):
        string2+="@attribute feature" + str(l) + " numeric\n"
    configString = "@relation KDDTrain-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.supervised.instance.Resample-B0.0-S1-Z18.0-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.supervised.instance.SMOTE-C2-K5-P1000.0-S1-weka.filters.supervised.instance.SMOTE-C2-K5-P500.0-S1-weka.filters.supervised.instance.SMOTE-C2-K5-P125.0-S1-weka.filters.supervised.instance.SMOTE-C3-K5-P500.0-S1-weka.filters.supervised.instance.SMOTE-C3-K5-P150.0-S1-weka.filters.supervised.instance.SMOTE-C4-K5-P800.0-S1-weka.filters.unsupervised.instance.Randomize-S42\n"+string2+"@attribute class {adduser,hydraftp,hydrassh,javameter,meterpreter,webshell,normal}\n\n@data\n"
    finalFile.write(configString)
    return finalFile, string1

def inputReadTrain(attackStrings, sentL, flistList, NormalString):
    print ("Concatenating Training files data together . . .\n ")
    for index in range(len(sentL)):
        sent = sentL[index]
        flist = open(flistList[index],"r")
        a = flist.read().splitlines()
        for f in a:
            if f.startswith(sent+"8")==False and f.startswith(sent + "9")==False and f.startswith(sent + "10")==False:
                fileo = open(f,"r")
                r = fileo.read()
                attackStrings[index].append(r)

    for f in os.listdir("../../Training Data/Training_Data_Master (copy)/"):
        if f.startswith("UTD"):
            fileRead = open("../../Training Data/Training_Data_Master (copy)/" + f,"r")
            inp = fileRead.read()
            NormalString.append(inp)

def inputReadTest(attackStrings, sentL, flistList, NormalString):
    print ("\n\nReading Input Files ...\n")
    for index in range(len(sentL)):
        sent = sentL[index]
        flist = open(flistList[index],"r")
        a = flist.read().splitlines()
        ####print "Concatenating " + outList[index] + " files data together . . . "
        for f in a:
            if f.startswith(sent+"8")==True or f.startswith(sent + "9")==True or f.startswith(sent + "10")==True:
                fileo = open(f,"r")
                r = fileo.read()
                attackStrings[index].append(r)

    for f in os.listdir("../../Validation Data/Validation_Data_Master (copy)/"):
        if f.startswith("UVD"):
            fileRead = open("../../Validation Data/Validation_Data_Master (copy)/" + f,"r")
            inp = fileRead.read()
            NormalString.append(inp)

def trainDataset(n, threshold):
    print ("\n\nReading Input Files ...\n")
    attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack", "Normal"]
    AddUserString = []
    HydraSSHString = []
    HydraFTPString = []
    JavaMetrString = []
    MeterpreterString = []
    WebshellString = []
    NormalString = []
    attackStrings = [AddUserString, HydraFTPString, HydraSSHString, JavaMetrString, MeterpreterString, WebshellString,NormalString]
    
    flistList = ["adduser.txt","hydrassh.txt","hydraftp.txt","javametr.txt","metr.txt","webshell.txt"]
    sentL = ["./Adduser_", "./Hydra_SSH_", "./Hydra_FTP_", "./Java_Meterpreter_", "./Meterpreter_", "./Web_Shell_"]
    
    inputReadTrain(attackStrings, sentL, flistList, NormalString)

    print ("Creating individual file records...")
     
    AddUserData = attackStrings[0]                    #Split the different files' records
    HydraSSHData = attackStrings[2]
    HydraFTPData = attackStrings[1]
    JavaMetrData = attackStrings[3]
    MeterpreterData = attackStrings[4]
    WebshellData = attackStrings[5]
    NormalData = NormalString

    freeze_support()
    with Pool() as pool:
        ans = pool.starmap( DictCalc, [("AddUser Thread", n, AddUserData), ("HydraFTP Thread", n, HydraFTPData), ("HydraSSH Thread", n, HydraSSHData), ("Java Meterpreter Thread", n, JavaMetrData), ("Meterpreter Thread", n, MeterpreterData), ("Webshell Thread", n, WebshellData), ("Normal Thread", n, NormalData)])
        top30Adduser, noOfAddUserFiles, AddUserFilesDict = ans[0]
        top30HydraFTP, noOfHydraFTPFiles, HydraFTPFilesDict = ans[1]
        top30HydraSSH, noOfHydraSSHFiles, HydraSSHFilesDict = ans[2]
        top30JavaMetr, noOfJavaMetrFiles, JavaMetrFilesDict = ans[3]
        top30Metr, noOfMeterpreterFiles, MeterpreterFilesDict = ans[4]
        top30Webshell, noOfWebShellFiles, WebshellFilesDict = ans[5]
        top30Normal, noOfNormalFiles, NormaFilesDict = ans[6]

    top30Data = [top30Adduser,top30HydraFTP,top30HydraSSH,top30JavaMetr,top30Metr,top30Webshell,top30Normal]
    featuresDict = {}
    features = []
    for i in range(len(top30Data)):                                 #Create Feature Vector
        for j in top30Data[i]:
            featuresDict[j] = 1
    features = list(featuresDict.keys())
    
    finalFile, string1 = fileInitialize(features, True)
                                      #Create the final dataaset by finding the corresponding frequency in the individual files
    ignored = 0
    ignored = createDataset(noOfAddUserFiles, threshold, finalFile, ignored, AddUserFilesDict, features)
    ignored = createDataset(noOfHydraFTPFiles, threshold, finalFile, ignored, HydraFTPFilesDict, features)
    ignored = createDataset(noOfHydraSSHFiles, threshold, finalFile, ignored, HydraSSHFilesDict, features)
    ignored = createDataset(noOfJavaMetrFiles, threshold, finalFile, ignored, JavaMetrFilesDict, features)
    ignored = createDataset(noOfMeterpreterFiles, threshold, finalFile, ignored, MeterpreterFilesDict, features)
    ignored = createDataset(noOfWebShellFiles, threshold, finalFile, ignored, WebshellFilesDict, features)
    ignored = createDataset(noOfNormalFiles, threshold, finalFile, ignored, NormaFilesDict, features)

    print ("###################################################################################")
    print ("DATASET Created in file "+ string1 +" !!!")
    print ("Dataset Specifications :\n")
    print ("------------------------------------------------------------")
    print ("Dataset Name : Attack Recognition Dataset")
    print ("No. of attributes :",len(features))
    if ignored!=0:
        print ("No. of ignored instances: ",ignored)
    print ("No. of instances :",noOfAddUserFiles+noOfHydraFTPFiles+noOfHydraSSHFiles+noOfMeterpreterFiles+noOfWebShellFiles+noOfJavaMetrFiles+noOfNormalFiles - ignored)
    classes = "Classes in Dataset : "
    for i in attackType:
        classes += i+", "
    print (classes[:-2])
    print ("-------------------------------------------------------------")
    print ("################################################################################")
    return features

def testDataset(n, features, threshold):
    
    AddUserString = []
    HydraSSHString = []
    HydraFTPString = []
    JavaMetrString = []
    MeterpreterString = []
    WebshellString = []
    NormalString = []
    attackStrings = [AddUserString, HydraFTPString, HydraSSHString, JavaMetrString, MeterpreterString, WebshellString,NormalString]
    
    attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack", "Normal"]
    flistList = ["adduser.txt","hydrassh.txt","hydraftp.txt","javametr.txt","metr.txt","webshell.txt"]
    sentL = ["./Adduser_", "./Hydra_SSH_", "./Hydra_FTP_", "./Java_Meterpreter_", "./Meterpreter_", "./Web_Shell_"]
    
    inputReadTest(attackStrings, sentL, flistList, NormalString)

    print ("Creating individual file records...")
     
    AddUserData = attackStrings[0]                  #Split the different files' records
    HydraSSHData = attackStrings[2]
    HydraFTPData = attackStrings[1]
    JavaMetrData = attackStrings[3]
    MeterpreterData = attackStrings[4]
    WebshellData = attackStrings[5]
    NormalData = NormalString

    freeze_support()
    with Pool() as pool:
        ans = pool.starmap( DictCalc2, [("AddUser Thread", n, AddUserData), ("HydraFTP Thread", n, HydraFTPData), ("HydraSSH Thread", n, HydraSSHData), ("Java Meterpreter Thread", n, JavaMetrData), ("Meterpreter Thread", n, MeterpreterData), ("Webshell Thread", n, WebshellData), ("Normal Thread", n, NormalData)])
        noOfAddUserFiles, AddUserFilesDict = ans[0]
        noOfHydraFTPFiles, HydraFTPFilesDict = ans[1]
        noOfHydraSSHFiles, HydraSSHFilesDict = ans[2]
        noOfJavaMetrFiles, JavaMetrFilesDict = ans[3]
        noOfMeterpreterFiles, MeterpreterFilesDict = ans[4]
        noOfWebShellFiles, WebshellFilesDict = ans[5]
        noOfNormalFiles, NormaFilesDict = ans[6]
    print ("\nCreating Data for Dictionaries ...\n")
     
    finalFile, string1 = fileInitialize(features, False)

    ignored = 0
    ignored = createDataset(noOfAddUserFiles, threshold, finalFile, ignored, AddUserFilesDict, features)
    ignored = createDataset(noOfHydraFTPFiles, threshold, finalFile, ignored, HydraFTPFilesDict, features)
    ignored = createDataset(noOfHydraSSHFiles, threshold, finalFile, ignored, HydraSSHFilesDict, features)
    ignored = createDataset(noOfJavaMetrFiles, threshold, finalFile, ignored, JavaMetrFilesDict, features)
    ignored = createDataset(noOfMeterpreterFiles, threshold, finalFile, ignored, MeterpreterFilesDict, features)
    ignored = createDataset(noOfWebShellFiles, threshold, finalFile, ignored, WebshellFilesDict, features)
    ignored = createDataset(noOfNormalFiles, threshold, finalFile, ignored, NormaFilesDict, features)

    print ("###################################################################################")
    print ("DATASET Created in file "+ string1 +" !!!")
    print ("Dataset Specifications :\n")
    print ("------------------------------------------------------------")
    print ("Dataset Name : Attack Recognition Dataset")
    print ("No. of attributes :",len(features))
    if ignored!=0:
        print ("No. of ignored instances: ",ignored)
    print ("No. of instances :",noOfAddUserFiles+noOfHydraFTPFiles+noOfHydraSSHFiles+noOfMeterpreterFiles+noOfWebShellFiles+noOfJavaMetrFiles+noOfNormalFiles - ignored)
    classes = "Classes in Dataset : "
    for i in attackType:
        classes += i+", "
    print (classes[:-2])
    print ("-------------------------------------------------------------")
    print ("################################################################################")


def main(n):
    sys.stdout.write("Enter one of the following:\n1. To make training dataset. . .\n2. To make both training and test dataset . . .\n3. Exit\n-----------------------------\n=>")
    choice = int(input())
    if(choice == 2):
        start_time = time.time();
        print ("TRAINING DATASET CREATION STARTED . . .")
        features1 = trainDataset(n, 0)
        print ("TRAINING  DATASET CREATION COMPLETED\n----------------------------------------------------\nTEST  DATASET CREATION STARTED . . .")
        testDataset(n, features1, 0)
        print ("TEST  DATASET CREATION COMPLETED")
        print ("TIME TAKEN : %s " % (time.time() - start_time) )
    elif(choice == 1):
        start_time = time.time();
        print ("TRAINING DATASET CREATION STARTED . . .")
        features1 = trainDataset(n, 0)
        print ("TRAINING  DATASET CREATION COMPLETED")
        print ("TIME TAKEN : %s " % (time.time() - start_time) )
    elif(choice == 3):
        print ("Closing . . .")
        sleep(1)
        sys.exit(0)
    else:
        print ("Enter correct choice !")
        main(n)


if __name__ == '__main__':
    sys.stdout.write("What Weight do u want to use for ngrams division? ")
    n = int(input())
    main(n)
    