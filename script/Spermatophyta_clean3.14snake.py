#! /usr/bin/python
#this script goes through each line, adding family names to each of species under such family and then will calculate:
# how many species in each genus

#Function to print genera with no species to NoSpeciesFile.
def outSpp(Order,Family,Genus,Species_Count):
	OutList=[str(Order), str(Family), str(Genus), str(Species_Count)] #output list
	if Species_Count==0:
		OutNoSpecies.write(",".join(OutList)+"\n")
	else:
		OutSpecisRich.write(",".join(OutList)+"\n")

#Open the file contains the data
InFileName = "../results/Spermatophyta58024_plnDB_pyphlawd01032020_reformated.csv"
InFile = open(InFileName, 'r')

HeaderLine = 'Order,Family,Genus,Species_Count'
HeaderLine1 = 'Order,Family,Genus,Species,NCBI_id'

SpeciesRichiFile = "../results/Spermatophyta_Richness_NCBI.csv"
NoSpeciesFile = "../results/Spermatophyta_Nospecies_NCBI.csv"
NewNameFile = "../results/Spermatophyta_clean11082019.csv"

OutSpecisRich = open(SpeciesRichiFile, 'w')
OutSpecisRich.write(HeaderLine + '\n')
OutNoSpecies = open(NoSpeciesFile, 'w')
OutNoSpecies.write(HeaderLine + '\n')
OutNewName = open(NewNameFile, 'w')
OutNewName.write(HeaderLine1 + '\n')

LineNumber = 0
Species_Count=0
Genus=""
InOrder=False
InFamily=False


# Loop through each line in the file
for Line in InFile:
	if LineNumber > 0:
		#Remove the line ending character
		Line=Line.strip('\n')
		#parsing the strings of each line
		LineList=Line.split(',')
		ID = str(LineList[0])
		Rank = str(LineList[1]) # getting the rank value
		Signal = str(LineList[2]) # getting the rank signal for downstream analyses
		#If the line is transitioning from "species", "subspecies", and "varietas" lines, stop talying species.
		UU = ["family", "order", "genus"]
		if Signal in UU:
			#If we were tallying species in a genus, print the tally.
			if InOrder and InFamily:
				outSpp(Order,Family,Genus,Species_Count)
			
			#If we have a new genus, change the name of the Genus and reset Species count.
			#We are also now in a family, so make sure InFamily is True.
			if Signal == "genus":
				Genus=Rank
				Species_Count=0
				InFamily=True

			#If we have a new family, change the name of the Family
			#We may or may not have genera in the family, so set InFamily False
			#We do have a family in the order, so make sure InOrder is True.
			elif Signal == "family":
				Family=Rank
				InOrder=True
				InFamily=False

			#If we have a new Order, chance the name of the name of the Order
			#We may or may not have Families in the order, so set InOrder False
			elif Signal == "order":
			
				Order=Rank
				InOrder=False

		#If the Signal is species, count it and write the info to the NewNameFile.
		elif Signal == "species": #counting species
			#New_Name = Family + '_' + Rank
			OutList2=[str(Order), str(Family), str(Genus), str(Rank), str(ID)]
			OutNewName.write(",".join(OutList2)+"\n")
			Species_Count+=1
		elif Signal == "subspecies":
			OutList2=[str(Order), str(Family), str(Genus), str(Rank), str(ID)]
			OutNewName.write(",".join(OutList2)+"\n")
			#Species_Count+=1 #not a species, no counting 
		elif Signal == "varietas":
			OutList2=[str(Order), str(Family), str(Genus), str(Rank), str(ID)]
			OutNewName.write(",".join(OutList2)+"\n")
			#Species_Count+=1 #not a species, no counting 
	LineNumber = LineNumber + 1

#Output last species information
outSpp(Order,Family,Genus,Species_Count)

InFile.close()
OutSpecisRich.close()
OutNoSpecies.close()
OutNewName.close()
