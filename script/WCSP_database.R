rm(list=ls())
#loading libraries
library("tidyverse")
# library("taxonlookup")

WCSP <- read_delim("./data/powoNames/taxon.txt", delim = "\t", escape_double = FALSE, col_names =F)

#meta data "meta.xml"
# Column0=taxonID
# Column1=modified
# Column2=verbatimTaxonRank
# Column3=scientificName
# Column4=family
# Column5=genus
# Column6=specificEpithet
# Column7=infraspecificEpithet
# Column8=scientificNameAuthorship
# Column9=nomenclaturalStatus
# Column10=rightsHolder
# Column11=namePublishedInYear
# Column12=nomenclaturalCode
# Column13=taxonRemarks
# Column14=bibliographicCitation
# Column15=language
# Column16=class
# Column17=references
# Column18=license
# Column19=rights
# Column20=namePublishedIn
# Column21=taxonRank
# Column22Plantae=kingdom
# Column23=phylum
# Column24=parentNameUsageID
# Column25=acceptedNameUsageID#
# Column26=originalNameUsageID
# Column27=taxonomicStatus#
# Column28=source

#add header
names(WCSP) <- c("taxonID", "modified", "verbatimTaxonRank", "scientificName", "family", "genus", "specificEpithet", "infraspecificEpithet", "scientificNameAuthorship", "nomenclaturalStatus", "rightsHolder", "namePublishedInYear", "nomenclaturalCode", "taxonRemarks", "bibliographicCitation", "language", "class", "references", "license", "rights", "namePublishedIn", "taxonRank", "kingdom", "phylum", "parentNameUsageID", "acceptedNameUsageID", "originalNameUsageID", "taxonomicStatus", "source")

#remove prefix string
WCSP$taxonID <- gsub("urn:lsid:ipni.org:names:", "", WCSP$taxonID)
WCSP$acceptedNameUsageID <- gsub("urn:lsid:ipni.org:names:", "", WCSP$acceptedNameUsageID)

#subset focused columns
WCSP_sub <- WCSP %>% select(taxonID, verbatimTaxonRank, scientificName, genus, specificEpithet, infraspecificEpithet, scientificNameAuthorship, family, acceptedNameUsageID, taxonomicStatus)

write_csv(WCSP_sub, "results/WCSP_sub_clean11062019.csv")
  

  