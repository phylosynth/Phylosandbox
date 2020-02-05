#/bin/python3

file = open("test.txt","r")

#Read in each line in the text file
for line in file:
  line=line.strip('\n')
  #Let's split the line into an array called "fields" using the "\t" as a separator:
  fields = line.split('|')
  print(len(fields))
  #extract the data:
  plant_name_id = fields[0]
  genus = fields[6]
  species = fields[8]
  taxon_name = fields[21]
  accepted_plant_name_id= fields[24]
  #Print the song
  print(plant_name_id + "," + genus + " "+ species + "," + taxon_name + "," + accepted_plant_name_id)

#It is good practice to close the file at the end to free up resources   
file.close()