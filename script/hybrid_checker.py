#! /usr/bin/python3

InFileName = "../results/Spermatophyta58024_plnDB02032020_nodupl_bashcleaned.csv"
InFile = open(InFileName, 'r')

#outfile1 = open("../results/all_cultivar_NCBI.txt", "w")
#outfile1.write("ID\tTaxon\tRank\n")

#outfile2 = open("../results/all_hybrid_NCBI.txt", "w")
#outfile2.write("ID\tTaxon\tString_len\thybrid_marker_Loc\tRank\n")

outfile3 = open("../results/all_sp._NCBI.txt", "w")
outfile3.write("ID\tTaxon\tRank\tSignal\n")

LineNumber = 0

for Line in InFile:
    if LineNumber > 0:
        Line=Line.strip('\n')
        #print("Yes")
#break up csv elements
        LineList=Line.split(',')
        ID = str(LineList[0])
        Rank = str(LineList[1]) #taxonomic names
        Signal = str(LineList[2]) #taxonomic rank
        spbits = Rank.split('_') #parsing taxonomic names
        tt = len(spbits) #total number of elements in the taxonomic names after parsing
        #print(tt)

#taxon with single quote is cultivar
#        for i in spbits:
#            if i.startswith("'") and i.endswith("'"):
#                outline1 = [str(ID), str(Rank), str(Signal)]
#                outfile1.write("\t".join(outline1)+"\n")
#taxon with hybrid marker
#        if ("x" in spbits):
#                outline2 = [str(ID), str(Rank), str(tt), str(spbits.index("x")), str(Signal)]
#                outfile2.write("\t".join(outline2)+"\n")

#taxon with genus + "sp." case
        if ("sp." in spbits):
                outline3 = [str(ID), str(Rank), str(Signal)]
                outfile3.write("\t".join(outline3)+"\n")
    LineNumber = LineNumber + 1

InFile.close()
#outfile1.close()
#outfile2.close()
outfile3.close()
