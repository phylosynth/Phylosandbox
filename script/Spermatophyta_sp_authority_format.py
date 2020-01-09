#!/bin/python

InFile = open("../results/Spermatophyta58024_plnDB01032020_nodupl.csv", 'r')
#InFile = open("test_data.csv", 'r')
outfile = open("../results/Spermatophyta58024_plnDB_pyphlawd01032020_reformated.csv", "w")
outfile2 = open("../results/Spermatophyta58024_plnDB_pyphlawd01032020_unnamed_hybrids.csv", "w")
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
        
#ranks
        if tt >= 1 and Signal in UU:
            Rank = spbits[0]
            Authority = '_'.join(spbits[1:])
            outline=[str(ID), str(Rank), str(Authority), str(Signal)]
            #print Rank+','+Authority
            outfile.write(",".join(outline)+"\n")
#species
        elif tt >= 2 and Signal in QQ:
    #species no authority case
            if tt ==2:
                Rank = '_'.join(spbits)
                outline=[str(ID), str(Rank), str(Authority), str(Signal)]
                outfile.write(",".join(outline)+"\n")
    #genus_sp. case
            elif "sp." in spbits:
                Rank = spbits[0]+'_'+spbits[1]
                outline=[str(ID), str(Rank), str(Authority), str(Signal)]
                outfile.write(",".join(outline)+"\n")
    #hybrids case
            elif "x" in spbits:
    #valid hybrid names
                if spbits[1] == "x":
                    Rank = '_'.join(spbits[:3])
                    Authority = '_'.join(spbits[3:])
                    outline=[str(ID), str(Rank), str(Authority), str(Signal)]
                    outfile.write(",".join(outline)+"\n")
                else:
                    Rank = '_'.join(spbits)
                    outline=[str(ID), str(Rank), str(Authority), str(Signal)]
                    outfile2.write(",".join(outline)+"\n")
    #subspecies level
            elif "var." in spbits or "f." in spbits or "subsp." in spbits:
                if tt == 4:
                    Rank = '_'.join(spbits)
                    #Authority = ''
                    outline=[str(ID), str(Rank), str(Authority), str(Signal)]
                    outfile.write(",".join(outline)+"\n")
                else:
                    Rank = '_'.join(spbits[0:4])
                    Authority = '_'.join(spbits[4:])
                    #print Rank+','+Authority
                    outline=[str(ID), str(Rank), str(Authority), str(Signal)]
                    outfile.write(",".join(outline)+"\n")
            else:
                Rank = spbits[0]+'_'+spbits[1]
                Authority = '_'.join(spbits[2:])
                outline=[str(ID), str(Rank), str(Authority), str(Signal)]
                outfile.write(",".join(outline)+"\n")
    LineNumber = LineNumber + 1
InFile.close()
outfile.close()
outfile2.close()

