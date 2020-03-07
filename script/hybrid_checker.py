#! /usr/bin/python3

InFileName = "../results/Spermatophyta58024_plnDB02032020_nodupl_bashcleaned.csv"
InFile = open(InFileName, 'r')

#outfile1 = open("../results/all_cultivar_NCBI.txt", "w")
#outfile1.write("ID\tTaxon\tName\n")

#outfile2 = open("../results/all_hybrid_NCBI.txt", "w")
#outfile2.write("ID\tTaxon\tString_len\thybrid_marker_Loc\tName\n")

#outfile3 = open("../results/all_sp._NCBI.txt", "w")
#outfile3.write("ID\tTaxon\tName\tSignal\n")

#define a function, report index if have duplicates
def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

#define a function, reporting how many common elements of two lists share
def common_N(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    return(len(a_set.intersection(b_set)))


UU = ["family", "order", "genus"]
QQ = ["species", "subspecies", "varietas", "forma", "no rank"]
qqbit = ["f.", "var.", "subsp."]
Authority = ""

LineNumber = 0

for Line in InFile:
    if LineNumber > 0:
        Line=Line.strip('\n')
        #print("Yes")
#break up csv elements
        LineList=Line.split(',')
        ID = str(LineList[0])
        Name = str(LineList[1]) #taxonomic names
        Signal = str(LineList[2]) #taxonomic rank
        spbits = Name.split('_') #parsing taxonomic names
        tt = len(spbits) #total number of elements in the taxonomic names after parsing
        #print(tt)
#cultivar
#taxon with single quote is cultivar
        for i in spbits:
            if i.startswith("'") and i.endswith("'"):
                outline = [str(ID), str(Name), str(Signal)]
                print("\n****************\n")
                print(",".join(outline))
                print("\n****************\n")
                #if "x" in spbits:
                    


        if Signal == "no_rank" and tt >=2 and spbits[0][0].isupper():
            #print("\n"+Line+"\n")
#Prunus_persica_x_Prunus_persica_var._nucipersica
            if "x" in spbits:
                if spbits.index("x") <= 1:
                    if common_N(qqbit, spbits) ==1:
                        if "var." in spbits or "nothovar" in spbits:
                            Signal = "varietas"
                            #ii=spbits.index("var.")
                        elif "subsp." in spbits:
                            Signal = "subspecies"
                        elif "f." in spbits:
                            Signal = "forma"                       
                        Name = '_'.join(spbits[:5])
                        Authority = '_'.join(spbits[5:])
                        outline=[str(ID), str(Name), str(Authority), str(Signal)]
                        print("\n****************\n")
                        print(",".join(outline)+"\n")
                        print("\n****************\n")
                    else:# common_N(qqbit, spbits) ==0:
                        Signal = "Species"
                        Name = '_'.join(spbits[:3])
                        Authority = '_'.join(spbits[3:])
                        outline=[str(ID), str(Name), str(Authority), str(Signal)]
                        print("\n****************\n")
                        print(",".join(outline)+"\n")
                        print("\n****************\n")
                else:
                    if "sp." in spbits:
                        print(Line+"\n")
                    print(Line+"\n")
            elif "sp." in spbits:
                print(Line+"\n")
            elif "var." in spbits or "nothovar." in spbits:
                try:
                #spbits.index("var.") #indexi of "var." in the name string
                    Name = '_'.join(spbits[:(spbits.index("var.")+2)])
                    Authority = '_'.join(spbits[(spbits.index("var.")+2):])  
                    #print(Name+"\t"+Signal)
                except:
                    #Signal = "varietas"
                    Name = '_'.join(spbits[:(spbits.index("nothovar.")+2)])
                    Authority = '_'.join(spbits[(spbits.index("nothovar.")+2):])  
                    #print(Name+"\t"+Signal)
                Signal = "varietas"
                outline=[str(ID), str(Name), str(Authority), str(Signal)]
                #outfile.write(",".join(outline)+"\n")
                print("\n****************\n")
                print(",".join(outline)+"\n")
                print("\n****************\n")
            elif "subsp." in spbits:
                Signal = "subspecies"
                Name = '_'.join(spbits[:(spbits.index("subsp.")+2)])
                Authority = '_'.join(spbits[(spbits.index("subsp.")+2):])  
                #print(Name+"\t"+Signal)
                outline=[str(ID), str(Name), str(Authority), str(Signal)]
                #outfile.write(",".join(outline)+"\n")
                print("\n****************\n")
                print(",".join(outline)+"\n")
                print("\n****************\n")
            elif "f." in spbits and spbits.index("f.")==2:
                Signal = "forma"
                Name = '_'.join(spbits[:(spbits.index("f.")+2)])
                Authority = '_'.join(spbits[(spbits.index("f.")+2):])  
                #print(Name+"\t"+Signal)
                outline=[str(ID), str(Name), str(Authority), str(Signal)]
                #outfile.write(",".join(outline)+"\n")
                print("\n****************\n")
                print(",".join(outline)+"\n")
                print("\n****************\n")
            elif spbits[1].islower() and common_N(qqbit, spbits) ==0:
                Signal = "Species"
                #print(Name+"\t"+Signal)
                Name = '_'.join(spbits[:2])
                Authority = '_'.join(spbits[2:])
                outline=[str(ID), str(Name), str(Authority), str(Signal)]
                #outfile.write(",".join(outline)+"\n")                
                print("\n****************\n")
                print(",".join(outline)+"\n")
                print("\n****************\n")




#taxon with hybrid marker
#        if ("x" in spbits) and Signal in UU:
                #outline2 = [str(ID), str(Name), str(tt), str(spbits.index("x")), str(Signal)]
#               #outfile2.write("\t".join(outline2)+"\n")
                #print(Name)
#            if spbits[0] == "x":
#                Name = '_'.join(spbits[:2])
#                Authority = '_'.join(spbits[2:])    
#                print(Name+'\t'+Authority)
#            if spbits[1] == "x":
#                Name = '_'.join(spbits[:3]) 
#                Authority = '_'.join(spbits[3:])    
#                print(Name+'\t'+Authority) 

# contains more than one "x"
#        if ("x" in spbits) and Signal in QQ:
#            if spbits[2] == "x" or len(duplicates(spbits, "x")) >=2:
#                print(Name)
                #outline2 = [str(ID), str(Name), str(tt), str(spbits.index("x")), str(Signal)]
#               #outfile2.write("\t".join(outline2)+"\n")
                #print(Name)
#            if spbits[0] == "x":
#                Name = '_'.join(spbits[:2])
#                Authority = '_'.join(spbits[2:])    
#                print(Name+'\t'+Authority)
#            if spbits[1] == "x":
#                Name = '_'.join(spbits[:3]) 
#                Authority = '_'.join(spbits[3:])    
#                print(Name+'\t'+Authority) 
#taxon with genus + "sp." case
#        if ("sp." in spbits):
#                outline3 = [str(ID), str(Name), str(Signal)]
#                outfile3.write("\t".join(outline3)+"\n")
    LineNumber = LineNumber + 1

InFile.close()
#outfile1.close()
#outfile2.close()
#outfile3.close()
