import subprocess, sqlite3

subprocess.call(["wget", "https://storage.googleapis.com/powop-content/backbone/powoNames.zip"])

subprocess.call(["mkdir", "powoNames"])

subprocess.call(["unzip", "powoNames.zip", "-d", "powoNames"])

# connect to database - this will create a new database if none exists
DB = "powoNames.db"
conn = sqlite3.connect(DB)
c = conn.cursor()

# Define columns to include
idx = [0] + list(range(2,10)) + [25, 27]

# Define column names
fieldNames = ["taxonID", "verbatimTaxonRank", "scientificName", "family", "genus", "specificEpithet", "infraspecificEpithet", "scientificNameAuthorship", "nomenclaturalStatus", "acceptedNameUsageID", "taxonomicStatus"]

# generate the SQL query for creating table
sqlcmd = "CREATE TABLE IF NOT EXISTS 'powoNames' ('idx' INTEGER PRIMARY KEY AUTOINCREMENT, "
for n in fieldNames:
	sqlcmd += "'" + n + "' TEXT, "
sqlcmd = sqlcmd[0:-2]
#sqlcmd += ")"
sqlcmd += ");" #should add a comma?
#CREATE TABLE 'powoNames' ('idx' INTEGER PRIMARY KEY AUTOINCREMENT, 'taxonID' TEXT, 'verbatimTaxonRank' TEXT, 'scientificName' TEXT, 'family' TEXT, 'genus' TEXT, 'specificEpithet' TEXT, 'infraspecificEpithet' TEXT, 'scientificNameAuthorship' TEXT, 'nomenclaturalStatus' TEXT, 'acceptedNameUsageID' TEXT, 'taxonomicStatus' TEXT)
	
# creating table 
c.execute(sqlcmd)

# extract data from powoNames
with open("powoNames/taxon.txt") as taxon: 
	i = 0
	for line in taxon:
		line = line.replace("'","''")
		line = line.split("\t")
		line[0] = line[0].replace("urn:lsid:ipni.org:names:","")
		line[25] = line[25].replace("urn:lsid:ipni.org:names:","")
		#print([line[j] for j in idx])
		sqlcmd = "INSERT INTO 'powoNames' ("
		for n in fieldNames:
			sqlcmd += "'" + n + "', "
		sqlcmd = sqlcmd[0:-2]
		sqlcmd += ") VALUES ("
		for id in idx:
			sqlcmd += "'" + line[id] + "', "
		sqlcmd = sqlcmd[0:-2]
		sqlcmd += ");"
		i += 1
		print(i)
		#print(sqlcmd)
		c.execute(sqlcmd)
#write csv sqlcmd
c.execute(""".headers on""")
c.execute(""".mode csv""")
c.execute(""".output powoNames.csv""")
c.execute("""SELECT * FROM powoNames""")
c.execute(""".output stdout""")

conn.commit()
conn.close()
