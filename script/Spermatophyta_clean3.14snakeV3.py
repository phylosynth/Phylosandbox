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
InFileName = "../results/Spermatophyta58024_plnDB_pyphlawd02042020_reformated.csv"
InFile = open(InFileName, 'r')

HeaderLine = 'Order,Family,Genus,Species_Count'
HeaderLine1 = 'Order,Family,Genus_hybrid,Genus,Species_hybrid,Species,Infraspecific_rank, Infraspecies,Authority,Taxon_rank,NCBI_id'

SpeciesRichiFile = "../results/Spermatophyta_Richness_NCBI.csv"
NoSpeciesFile = "../results/Spermatophyta_Nospecies_NCBI.csv"
NewNameFile = "../results/Spermatophyta_clean01062020.csv"

OutSpecisRich = open(SpeciesRichiFile, 'w')
OutSpecisRich.write(HeaderLine + '\n')
OutNoSpecies = open(NoSpeciesFile, 'w')
OutNoSpecies.write(HeaderLine + '\n')
OutNewName = open(NewNameFile, 'w')
OutNewName.write(HeaderLine1 + '\n')

#set up a lines_seen list to store duplicate lines

LineNumber = 0
Species_Count = 0
Genus = ""
Family = ""
Order = ""
Genus_hybrid = ""
Species_hybrid = ""
Infraspecific_rank = ""
Infraspecies = ""
InOrder = False
InFamily = False
Authority = ""

# Loop through each line in the file
for Line in InFile:
	if LineNumber >= 0:
		#Remove the line ending character
		Line=Line.strip('\n')
		#parsing the strings of each line
		LineList=Line.split(',')
		ID = str(LineList[0])
		Rank = str(LineList[1]) # getting the rank value
		spbits = Rank.split('_') #parsing taxonomic names
		Authority = str(LineList[2])
		Signal = str(LineList[3]) # getting the rank signal for downstream analyses
		
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
#hybird species
			if "x" in spbits:
				if spbits[0] == "x":
					Genus_hybrid = spbits[0]
					Genus = spbits[1]
					Species = spbits[2]
					OutList2=[str(Order), str(Family), str(Genus_hybrid), str(Genus), str(Species_hybrid), str(Species), str(Infraspecific_rank), str(Infraspecies), str(Authority), str(Signal), str(ID)]
					OutNewName.write(",".join(OutList2)+"\n")
				elif spbits[1] == "x":
					Genus = spbits[0]
					Species_hybrid = spbits[1]
					Species = spbits[2]
					OutList2=[str(Order), str(Family), str(Genus_hybrid), str(Genus), str(Species_hybrid), str(Species), str(Infraspecific_rank), str(Infraspecies), str(Authority), str(Signal), str(ID)]
					OutNewName.write(",".join(OutList2)+"\n")
			else:
				Genus = spbits[0] #need to make sure Genus = spbits[0]
				Species = spbits[1]
				OutList2=[str(Order), str(Family), str(Genus_hybrid), str(Genus), str(Species_hybrid), str(Species), str(Infraspecific_rank), str(Infraspecies), str(Authority), str(Signal), str(ID)]
				OutNewName.write(",".join(OutList2)+"\n")
			Species_Count+=1
		elif Signal == "subspecies":
			if "subsp." in spbits and "x" not in spbits:
				Genus = spbits[0] #need to make sure Genus = spbits[0]
				Species = spbits[1]
				Infraspecific_rank = spbits[2]
				Infraspecies = spbits[3]
				OutList2=[str(Order), str(Family), str(Genus_hybrid), str(Genus), str(Species_hybrid), str(Species), str(Infraspecific_rank), str(Infraspecies), str(Authority), str(Signal), str(ID)]
				OutNewName.write(",".join(OutList2)+"\n")
###################
			elif "var." in 
			elif "x" in spbits and "subsp." in Authority.split('_'):
				Genus = spbits[0]
				Species_hybrid = spbits[1]
				Species = spbits[2]
				Infraspecific_rank = Authority.split('_')[0]
				Infraspecies = Authority.split('_')[1]
				Authority = Authority.split('_')[2:]
			elif "x" in spbits and "subsp." not in Authority.split('_'):
			
			else:
				Genus = spbits[0] #need to make sure Genus = spbits[0]
				Species = spbits[1]
				Infraspecific_rank = spbits[2]
				Infraspecies = spbits[3]
				OutList2=[str(Order), str(Family), str(Genus_hybrid), str(Genus), str(Species_hybrid), str(Species), str(Infraspecific_rank), str(Infraspecies), str(Authority), str(Signal), str(ID)]
				OutNewName.write(",".join(OutList2)+"\n")
			#Species_Count+=1 #not a species, no counting 
		elif Signal == "varietas":
			OutList2=[str(Order), str(Family), str(Genus), str(Rank), str(Authority), str(ID)]
			OutNewName.write(",".join(OutList2)+"\n")
			#Species_Count+=1 #not a species, no counting
		elif Signal == "forma":
			OutList2=[str(Order), str(Family), str(Genus), str(Rank), str(Authority), str(ID)]
			OutNewName.write(",".join(OutList2)+"\n")
	LineNumber = LineNumber + 1

#Output last species information
outSpp(Order,Family,Genus,Species_Count)

InFile.close()
OutSpecisRich.close()
OutNoSpecies.close()
OutNewName.close()
