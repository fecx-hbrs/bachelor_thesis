import argparse
import pandas as pd

parser = argparse.ArgumentParser()
result = pd.DataFrame(columns=["epoch", "rwd", "running rwd", "best cost", "optimal cost", "gap"])

#Valid - epoch:0 |rwd: 7.69 |running rwd: 7.69 |best cost: 18.297 |optimal cost: 5.717 |gap 220.026[0m
searchStr = "Valid -"

list=[]

parser.add_argument('--i', default="", type=str, help='input file path')
parser.add_argument('--o', default="", type=str, help='output file path')

args = parser.parse_args()

if args.o == "":
    args.o = args.i.split(".")[0] + ".csv"

file = open(args.i, "r")

lines = file.readlines()

for line in lines:
    line = line.replace("\x1b[0m\n","")
    if(searchStr in line):
        tmp={}
        splitted = line.split(" |")
        epoch = int(splitted[0][(splitted[0].index(":") + 1):])
        tmp["epoch"] = epoch
        for i in range(1,5):
            s_split = splitted[i].split(": ")
            tmp[s_split[0]] = s_split[1]
        tmp["gap"] = splitted[5].split(" ")[1]
        list.append(tmp)
result = pd.DataFrame(list)
result.to_csv(args.o, index = False)
        


