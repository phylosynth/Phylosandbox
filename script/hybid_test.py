#!/bin/python

InFile = open("../results/Spermatophyta58024_plnDB_pyphlawd11142019_nodupl.csv", 'r')
LineNumber = 0
UU = ["family", "order", "genus"]
QQ = ["species", "subspecies", "varietas", "forma"]

for Line in InFile:
    if LineNumber > 0:
        Line=Line.strip('\n')
#break up csv elements
        LineList=Line.split(',')
        ID = str(LineList[0]) #nibi id
        Rank = str(LineList[1]) #taxonomic names
        Signal = str(LineList[2]) #taxonomic rank
        spbits = Rank.split('_') #parsing taxonomic names
        Authority = ''
        tt = len(spbits) #total number of elements in the taxonomic names after parsing
#species
        if tt >= 2 and Signal in QQ:
   #hybrids case
            if "x" in spbits:
                if spbits[1] == "x":
                    Rank = '_'.join(spbits[:3])
                    Authority = '_'.join(spbits[3:])
                    outline=[str(ID), str(Rank), str(Authority), str(Signal)]
                    print("\t".join(outline)+"\n")
                else:
                    Rank = '_'.join(spbits)
                    outline=[str(ID), str(Rank), str(Authority), str(Signal)]
                    print(",".join(outline)+"\n")
    LineNumber = LineNumber + 1
InFile.close()

