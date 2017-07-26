from myLib1729 import *
from time import sleep
import os,sys


print "\n\nReading Input Files ...\n"
#sleep(1)
attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack", "Normal"]

#attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack"]
flistList = ["adduser.txt","hydrassh.txt","hydraftp.txt","javametr.txt","metr.txt","webshell.txt"]
outList = ["totTrainAdduser2.txt","totTrainHydraSSH2.txt","totTrainHydraFTP2.txt","totTrainJavaMetr2.txt","totTrainMeterpreter2.txt","totTrainWebShell2.txt"]
sentL = ["./Adduser_", "./Hydra_SSH_", "./Hydra_FTP_", "./Java_Meterpreter_", "./Meterpreter_", "./Web_Shell_"]

for index in range(len(sentL)):
    sent = sentL[index]
    flist = open(flistList[index],"r")
    out = open(outList[index],"w+")
    a = flist.read().splitlines()
    print "Concatenating " + outList[index] + " files data together . . . "
    for f in a:
        if f.startswith(sent+"8")==False and f.startswith(sent + "9")==False and f.startswith(sent + "10")==False:
            fileo = open(f,"r")
            r = fileo.read()
            out.write(r)
            out.write("-1 ")
            #sys.stdout.write(attackType[index]+" ("+f+") data written to "+outList[index]+" \n")

sys.stdout.write("Concatenating all normal data files ...\n")
out = open("totTrainDataNormal3.txt","a+")
k = 1
for f in os.listdir("../../Training Data/Training_Data_Master (copy)/"):
    if f.startswith("UTD"):
        fileRead = open("../../Training Data/Training_Data_Master (copy)/" + f,"r")
        inp = fileRead.read()
        if(f.endswith(str(k) + ".txt") == False):
            print f,k
            k+=1
        out.write(inp)
        out.write("-1 ")