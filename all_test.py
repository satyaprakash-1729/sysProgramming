from myLib1729 import *
from time import sleep
print "\n\nReading Input File ...\n"

fAddUser = open("totTestAddUser.txt","r")
fHydraFTP = open("totTestHydraFTP.txt","r")
fHydraSSH = open("totTestHydraSSH.txt","r")
fJavaMetr = open("totTestJavaMetr.txt","r")
fMetr = open("totTestMetr.txt","r")
fWebShell = open("totTestWebShell.txt","r")

print "What Weight do u want to use for ngrams division?\n"
n = int(raw_input())

print "\n\nCreating ngrams dictionaries for all files. Please Wait ...\n"
addUserDict = ngramsDictionary(fAddUser.read().split(),n)
print "Add User Dictionary Created!\n"
sleep(1)
HydraFTPDict = ngramsDictionary(fHydraFTP.read().split(),n)
print "Hydra FTP Dictionary Created!\n"
sleep(1)
HydraSSHDict = ngramsDictionary(fHydraSSH.read().split(),n)
print "Hydra SSH Dictionary Created!\n"
sleep(1)
JavaMetrDict = ngramsDictionary(fJavaMetr.read().split(),n)
print "Java Meterpreter Dictionary Created!\n"
sleep(1)
MetrDict = ngramsDictionary(fMetr.read().split(),n)
print "Meterpreter Dictionary Created!\n"
sleep(1)
WebShellDict = ngramsDictionary(fWebShell.read().split(),n)
print "Webshell Dictionary Created!\n"
sleep(1)

print "\nCreating Text Files for Dictionary Output ...\n"

dictNames = ["addUserDictTest","HydraFTPDictTest","HydraSSHDictTest","JavaMetrDictTest","MetrDictTest","WebShellDictTest"]
allDicts = [addUserDict,HydraFTPDict,HydraSSHDict,JavaMetrDict,MetrDict,WebShellDict]
top30Adduser = []
top30HydraFTP = []
top30HydraSSH = []
top30JavaMetr = []
top30Metr = []
top30Webshell = []
top30Data = [top30Adduser,top30HydraFTP,top30HydraSSH,top30JavaMetr,top30Metr,top30Webshell]
for i in range(len(allDicts)):
    out = open(dictNames[i]+".txt", "a+")
    dict = allDicts[i]
    Ltot = len(dict)
    c=0
    #sentinel = Ltot*0.3
    sentinel = 150
    top30 = top30Data[i]
    print "\nCreating top 30\%\ arrays of tuples for "+dictNames[i]+" . . .\n"
    sleep(1)
    for key, value in sorted(dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        c+=1
        out.write("%s: %s\n" % (key, value))
        if(sentinel >= c):
            top30.append(key)

finalFile = open("Test_1.arff","a+")
configString = "@relation KDDTest-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.supervised.instance.Resample-B0.0-S1-Z18.0-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.supervised.instance.SMOTE-C2-K5-P1000.0-S1-weka.filters.supervised.instance.SMOTE-C2-K5-P500.0-S1-weka.filters.supervised.instance.SMOTE-C2-K5-P125.0-S1-weka.filters.supervised.instance.SMOTE-C3-K5-P500.0-S1-weka.filters.supervised.instance.SMOTE-C3-K5-P150.0-S1-weka.filters.supervised.instance.SMOTE-C4-K5-P800.0-S1-weka.filters.unsupervised.instance.Randomize-S42\n@attribute duration numeric\n@attribute src_bytes numeric\n@attribute dst_bytes numeric\n@attribute wrong_fragment numeric\n@attribute urgent numeric\n@attribute hot numeric\n@attribute num_failed_logins numeric\n@attribute num_compromised numeric\n@attribute root_shell numeric\n@attribute su_attempted numeric\n@attribute num_root numeric\n@attribute num_file_creations numeric\n@attribute num_shells numeric\n@attribute num_access_files numeric\n@attribute num_outbound_cmds numeric\n@attribute count numeric\n@attribute srv_count numeric\n@attribute serror_rate numeric\n@attribute class {adduser,hydraftp,hydrassh,javameter,meterpreter,webshell}\n\n@data\n"
finalFile.write(configString)
print "--------------------------------------------------------\nCreating DATASHEET . . ."
sleep(3)
print "###################################################################################"
for i in range(0,150,3):
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
    dataSet1 = ""
    dataSet2 = ""
    dataSet3 = ""
    dataSet4 = ""
    dataSet5 = ""
    dataSet6 = ""
    for j in range(18):
        try:
            dataSet1+=str(addUserDict[features[j]])+", "
        except:
            dataSet1 += str(0) + ", "
    dataSet1+="?\n"
    for j in range(18):
        try:
            dataSet2+=str(HydraFTPDict[features[j]])+", "
        except:
            dataSet2 += str(0) + ", "
    dataSet2+="?\n"
    for j in range(18):
        try:
            dataSet3+=str(HydraSSHDict[features[j]])+", "
        except:
            dataSet3 += str(0) + ", "
    dataSet3+="?\n"
    for j in range(18):
        try:
            dataSet4+=str(JavaMetrDict[features[j]])+", "
        except:
            dataSet4 += str(0) + ", "
    dataSet4+="?\n"
    for j in range(18):
        try:
            dataSet5+=str(MetrDict[features[j]])+", "
        except:
            dataSet5 += str(0) + ", "
    dataSet5+="?\n"
    for j in range(18):
        try:
            dataSet6+=str(WebShellDict[features[j]])+", "
        except:
            dataSet6 += str(0) + ", "
    dataSet6+="?\n"
    finalFile.write(dataSet1+dataSet2+dataSet3+dataSet4+dataSet5+dataSet6)
print "Test Model Created !!!"
print "################################################################################"