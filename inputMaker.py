import os
import sys
from time import sleep

attackType = ["Add User Attack","Hydra SSH Attack","Hydra FTP Attack","Java Meterpreter Attack","Meterpreter Attack","Webshell Attack"]
flistList = ["adduser.txt","hydrassh.txt","hydraftp.txt","javametr.txt","metr.txt","webshell.txt"]
outList = ["totTrainAdduser.txt","totTrainHydraSSH.txt","totTrainHydraFTP.txt","totTrainJavaMetr.txt","totTrainMeterpreter.txt","totTrainWebShell.txt"]
sentL = ["./Adduser_", "./Hydra_SSH_", "./Hydra_FTP_", "./Java_Meterpreter_", "./Meterpreter_", "./Web_Shell_"]

for index in range(len(sentL)):
    sent = sentL[index]
    flist = open(flistList[index],"r")
    out = open(outList[index],"a+")
    a = flist.read().splitlines()

    for f in a:
        if f.startswith(sent+"8")==False and f.startswith(sent + "9")==False and f.startswith(sent + "10")==False:
            fileo = open(f,"r")
            r = fileo.read()
            out.write(r)
            out.write("-1 ")
            sys.stdout.write(attackType[index]+" ("+f+") data written to "+outList[index]+" \n")
