import os,sys

out = open("totTrainDataNormal3.txt","w+")

for f in os.listdir("../../Training\ Data/Training_Data_Master\ \(copy\)/"):
    if f.startswith("UTD"):
        fileRead = open(f,"r")
        inp = fileRead.read()
        out.write(inp)
        out.write("-1 ")
        sys.stdout.write("Concatenating all normal data files ...\n")