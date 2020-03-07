#!/bin/python3

InFile = open("../results/Spermatophyta58024_plnDB02032020_nodupl_bashcleaned.csv", 'r')

outfile = open("../results/new_result/Spermatophyta58024_plnDB_pyphlawd02072020_reformated.csv", "w")
outfile.write("ID,Taxon,Authority,Rank\n")

outfile2 = open("../results/new_result/Spermatophyta58024_plnDB_pyphlawd02072020_cultivar.csv", "w")
outfile2.write("ID,Taxon,Rank\n")

outfile3 = open("../results/new_result/Spermatophyta58024_plnDB_pyphlawd02072020_ill.hybrids.csv", "w")
outfile3.write("ID,Taxon,Rank\n")

outfile4 = open("../results/new_result/Spermatophyta58024_plnDB_pyphlawd02072020_sp.csv", "w")
outfile4.write("ID,Taxon,Rank\n")


#define a function, report index if have duplicates
def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

#define a function, reporting how many common elements of two lists share
def common_N(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    return(len(a_set.intersection(b_set)))

UU = ["family", "order", "genus"]
QQ = ["species", "subspecies", "varietas", "forma"]
qqbit = ["f.", "var.", "nothovar.", "subsp."]
Authority = ""

LineNumber = 0

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
        
#cultivar
#taxon with single quote is cultivar
        try:
            for i in spbits:
                if i.startswith("'") and i.endswith("'"):
                    #outline = [str(ID), str(Name), str(Signal)]
                    outfile2.write(Line+"\n")
                    if "x" in spbits:
                        outfile3.write(Line+"\n")
                    elif "sp." in spbits:
                        outfile4.write(Line+"\n")
        except:
            continue
#rescue "no rank"
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
                            outfile.write(",".join(outline)+"\n")
                        else:# common_N(qqbit, spbits) ==0:
                            Signal = "species"
                            Name = '_'.join(spbits[:3])
                            Authority = '_'.join(spbits[3:])
                            outline=[str(ID), str(Name), str(Authority), str(Signal)]
                            outfile.write(",".join(outline)+"\n")
                    else:
                        if "sp." in spbits:
                            outfile4.write(Line+"\n")
                        outfile3.write(Line+"\n")
                elif "sp." in spbits:
                    outfile4.write(Line+"\n")
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
                    outfile.write(",".join(outline)+"\n")
                elif "subsp." in spbits:
                    Signal = "subspecies"
                    Name = '_'.join(spbits[:(spbits.index("subsp.")+2)])
                    Authority = '_'.join(spbits[(spbits.index("subsp.")+2):])  
                    #print(Name+"\t"+Signal)
                    outline=[str(ID), str(Name), str(Authority), str(Signal)]
                    outfile.write(",".join(outline)+"\n") 
                elif "f." in spbits and spbits.index("f.")==2:
                    Signal = "forma"
                    Name = '_'.join(spbits[:(spbits.index("f.")+2)])
                    Authority = '_'.join(spbits[(spbits.index("f.")+2):])  
                    #print(Name+"\t"+Signal)
                    outline=[str(ID), str(Name), str(Authority), str(Signal)]
                    outfile.write(",".join(outline)+"\n") 
                elif spbits[1].islower() and common_N(qqbit, spbits) ==0:
                    Signal = "species"
                    #print(Name+"\t"+Signal)
                    Name = '_'.join(spbits[:2])
                    Authority = '_'.join(spbits[2:])
                    outline=[str(ID), str(Name), str(Authority), str(Signal)]
                    outfile.write(",".join(outline)+"\n")
#Higher ranks
        if Signal in UU:
                if "x" in spbits:
                    #outfile3.write(Line+"\n") #this will output all the taxonomic names with "x" tag
# example: x_Tritordeum Asch._&_Graeb.
                    if spbits[0] == "x":
                        Name = '_'.join(spbits[:2])
                        Authority = '_'.join(spbits[2:])    
                        #print(Name+'\t'+Authority)
                        outline=[str(ID), str(Name), str(Authority), str(Signal)]
                        outfile.write(",".join(outline)+"\n")
# example: Bambusa_x_Dendrocalamus
                    elif spbits[1] == "x":
                        Name = '_'.join(spbits[:3]) 
                        Authority = '_'.join(spbits[3:])    
                        #print(Name+'\t'+Authority)
                        outline=[str(ID), str(Name), str(Authority), str(Signal)]
                        outfile.write(",".join(outline)+"\n")                
#example: Elymordeum LePage
                else:
                    Name = spbits[0]
                    Authority = '_'.join(spbits[1:])
                    outline=[str(ID), str(Name), str(Authority), str(Signal)]
                    #print Name+','+Authority
                    outfile.write(",".join(outline)+"\n")

#species and under speies level
        if tt >= 2 and Signal in QQ:
#hybrid
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
                            outfile.write(",".join(outline)+"\n")
                        else:# common_N(qqbit, spbits) ==0:
                            Signal = "species"
                            Name = '_'.join(spbits[:3])
                            Authority = '_'.join(spbits[3:])
                            outline=[str(ID), str(Name), str(Authority), str(Signal)]
                            outfile.write(",".join(outline)+"\n")
                    else:
                        if "sp." in spbits:
                            outfile4.write(Line+"\n")
                        outfile3.write(Line+"\n")
# sp.
                elif "sp." in spbits:
                    outfile4.write(Line+"\n")
# varietas
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
                    outfile.write(",".join(outline)+"\n")
# subspecies
                elif "subsp." in spbits:
                    Signal = "subspecies"
                    Name = '_'.join(spbits[:(spbits.index("subsp.")+2)])
                    Authority = '_'.join(spbits[(spbits.index("subsp.")+2):])
                    #print(Name+"\t"+Signal)
                    outline=[str(ID), str(Name), str(Authority), str(Signal)]
                    outfile.write(",".join(outline)+"\n")
# forma
                elif "f." in spbits and spbits.index("f.")==2:
                    Signal = "forma"
                    Name = '_'.join(spbits[:(spbits.index("f.")+2)])
                    Authority = '_'.join(spbits[(spbits.index("f.")+2):])
                    #print(Name+"\t"+Signal)
                    outline=[str(ID), str(Name), str(Authority), str(Signal)]
                    outfile.write(",".join(outline)+"\n")
# species
                elif spbits[1].islower() and common_N(qqbit, spbits) ==0:
                    Signal = "species"
                    if tt ==2 and spbits[1].islower():
                        Name = '_'.join(spbits)
                        outline=[str(ID), str(Name), str(Authority), str(Signal)]
                        outfile.write(",".join(outline)+"\n")
                    else:
                        Name = '_'.join(spbits[:2])
                        Authority = '_'.join(spbits[2:])
                        outline=[str(ID), str(Name), str(Authority), str(Signal)]
                        outfile.write(",".join(outline)+"\n")
    LineNumber = LineNumber + 1
InFile.close()
outfile2.close()
outfile3.close()
outfile4.close()
outfile.close()
