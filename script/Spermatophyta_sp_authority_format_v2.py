#!/bin/python3

InFile = open("../results/Spermatophyta58024_plnDB02032020_nodupl_bashcleaned.csv", 'r')
#InFile = open("test_data.csv", 'r')
outfile = open("../results/Spermatophyta58024_plnDB_pyphlawd02042020_reformated.csv", "w")
outfile2 = open("../results/Spermatophyta58024_plnDB_pyphlawd02042020_unnamed_hybrids.csv", "w")
#outfile = open("../results/test123.csv", "w")
#outfile2 = open("../results/test123_unnamed_hybrids.csv", "w")

LineNumber = 0
UU = ["family", "order", "genus"]
QQ = ["species", "subspecies", "varietas", "forma"]

for Line in InFile:
    if LineNumber > 0:
        Line=Line.strip('\n')
#break up csv elements
        LineList=Line.split(',')
        ID = str(LineList[0]) #ncbi id
        Name = str(LineList[1]) #taxonomic names
        Signal = str(LineList[2]) #taxonomic rank
        spbits = Name.split('_') #parsing taxonomic names
        Authority = ''
        tt = len(spbits) #total number of elements in the taxonomic names after parsing
        
#ranks
        if tt >= 1 and Signal in UU:
            if "x" in spbits:
                if spbits[0] == "x" and tt >= 2:
                    Name = spbits[0] + "_" + spbits[1]
                    Authority = '_'.join(spbits[2:])
                    
                print(Name)
            else:
                Name = spbits[0]
                Authority = '_'.join(spbits[1:])
                outline=[str(ID), str(Name), str(Authority), str(Signal)]
                #print Name+','+Authority
                outfile.write(",".join(outline)+"\n")
#species
        elif tt >= 2 and Signal in QQ:
    #species no authority case
            if tt ==2:
                Name = '_'.join(spbits)
                outline=[str(ID), str(Name), str(Authority), str(Signal)]
                outfile.write(",".join(outline)+"\n")
    #genus_sp. case
            elif "sp." in spbits:
                Name = spbits[0]+'_'+spbits[1]
                outline=[str(ID), str(Name), str(Authority), str(Signal)]
                outfile.write(",".join(outline)+"\n")
    #hybrids case
            elif "x" in spbits:
    #valid hybrid names
                if spbits[0] == "x" or spbits[1] == "x":
                    Name = '_'.join(spbits[:3])
                    Authority = '_'.join(spbits[3:])
                    outline=[str(ID), str(Name), str(Authority), str(Signal)]
                    outfile.write(",".join(outline)+"\n")
                else:
                    Name = '_'.join(spbits)
                    outline=[str(ID), str(Name), str(Authority), str(Signal)]
                    outfile2.write(",".join(outline)+"\n")
    #subspecies level
            elif "var." in spbits or "f." in spbits or "subsp." in spbits:
                if tt == 4:
                    Name = '_'.join(spbits)
                    #Authority = ''
                    outline=[str(ID), str(Name), str(Authority), str(Signal)]
                    outfile.write(",".join(outline)+"\n")
                else:
                    Name = '_'.join(spbits[0:4])
                    Authority = '_'.join(spbits[4:])
                    #print Name+','+Authority
                    outline=[str(ID), str(Name), str(Authority), str(Signal)]
                    outfile.write(",".join(outline)+"\n")
            else:
                Name = spbits[0]+'_'+spbits[1]
                Authority = '_'.join(spbits[2:])
                #print Name+'\t'+Authority
                outline=[str(ID), str(Name), str(Authority), str(Signal)]
                outfile.write(",".join(outline)+"\n")
    LineNumber = LineNumber + 1
InFile.close()
outfile.close()
outfile2.close()

