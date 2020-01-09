rm(list=ls())
#loading libraries
library("tidyverse")

#reading in tables

WCSP <- read_csv("results/powoNames.csv", col_names = T)
NCBI <- read_csv("results/Spermatophyta_clean01062020.csv", col_names = T)
#modify the shared species column to join the two tables
names(NCBI)[4] <- "scientificName"
NCBI$scientificName <- gsub("_", " ", NCBI$scientificName)

#join the tables
WCSP_NCBI_cmb <- left_join(WCSP, NCBI, by="scientificName")

# about 85.22% NCBI names are able to match with world checklist at the intial stage
# sum(NCBI$scientificName %in% WCSP$scientificName)/length(NCBI$scientificName) =0.8522467
#output

write_csv(WCSP_NCBI_cmb, "results/WCSP_NCBI_join_clean01062020.csv")

unmatched <- NCBI$NCBI_id[!(NCBI$NCBI_id %in% WCSP_NCBI_cmb$NCBI_id)]

NCBI.data <- NCBI %>% filter(NCBI_id %in% unmatched)

write_csv(NCBI.data, "results/WCSP_NCBI_unmapped01062020.csv")

#exclude entries with genus_sp.
sp_entries <- NCBI.data[grep(" sp\\.", NCBI.data$scientificName),]

write_csv(sp_entries, "results/NCBI_sequence_name_with_genus_sp.01062020.csv")

#for the rest names further check base of toxonomic names status and authority

remain.names.data <- NCBI.data[-grep(" sp\\.", NCBI.data$scientificName),]

# grep("Ephedra intermedia", WCSP$scientificName)
# WCSP[293732,3] == "Species" && WCSP[293736,10] == "Species"

library("Taxonstand")
tt <- TPL(remain.names.data$scientificName, infra=TRUE)

write.csv(tt, "./results/NCBI_sequence_name_unmatch_TPL.01062020.csv")

tt <- read_csv("./results/NCBI_sequence_name_unmatch_TPL.01062020.csv", col_names = T)

tt_NA <- tt %>% group_by(New.Taxonomic.status) %>% filter(New.Taxonomic.status=="Unresolved")

unmatch.data <- head(tt, n=100)


for(i in 1:dim(unmatch.data)[1]){
  #dealing with "genus epithet InfraspecificRank epithet" cases first
  # e.g., "Leucospermum tottum" =? "Leucospermum tottum var. tottum"
  if(!is.na(unmatch.data[i,]$Infraspecific)){
    
    if(unmatch.data[i,]$Species == unmatch.data[i,]$Infraspecific && unmatch.data[i,]$New.Taxonomic.status != "Accepted"){
      
      #reformate name
      try.name <- paste0(unmatch.data$New.Genus[i], " ", unmatch.data$New.Species[i], sep="")
      
      #index
      ncbi.id <- NCBI.data$NCBI_id[i]
      
      dd <- grep(try.name, WCSP$scientificName)
      
      if(!is.na(dd)){
        #output
        print(paste0(unmatch.data$Taxon[i], ",", ncbi.id, ",", WCSP$acceptedNameUsageID[dd[1]], sep=""))
      }
      else{
        #output
        print(paste0(unmatch.data$Taxon[i], ",", "NA", sep=""))
      }
    }
    
    else if(unmatch.data$Species[i] != unmatch.data$Infraspecific[i] && unmatch.data$New.Taxonomic.status != "Accepted"){
      
      # no Taxonomic.status records for this name in the TPL
      if(is.na(unmatch.data$New.Taxonomic.status[i])){
        #output
        print(paste0(unmatch.data$Taxon[i], ",NA", sep=""))
      }
      # Unresolved
      else if(unmatch.data$New.Taxonomic.status[i] == "Unresolved"){
        #output
        print(paste0(unmatch.data$Taxon[i], ",", "Unresolved", sep=""))
      }
    } 
    
  }
  else {
  # for resolvaed names: Accepted and Synonym
  # else if (unmatch.data$Taxonomic.status[i] == "Accepted" || unmatch.data$Taxonomic.status[i] == "Synonym" ){
    
    # names no Hybrid and no Infraspecific
    if(is.na(unmatch.data$New.Hybrid.marker[i]) && is.na(unmatch.data$New.Infraspecific.rank[i])){
      
      Acc.names <- paste0(unmatch.data$New.Genus[i], " ", unmatch.data$New.Species[i], sep="")
      
    }
    
    # names no Hybrid and only Infraspecific
    else if(is.na(unmatch.data$New.Hybrid.marker[i]) && !is.na(unmatch.data$New.Infraspecific.rank[i])){
      Acc.names <- paste0(unmatch.data$New.Genus[i], " ", unmatch.data$New.Species[i], " ", unmatch.data$New.Infraspecific.rank[i], " ", unmatch.data$New.Species[i], sep="")
      
    }
    # names only Hybrid and no Infraspecific
    else if(!is.na(unmatch.data$New.Hybrid.marker[i]) && is.na(unmatch.data$New.Infraspecific.rank[i])){
      Acc.names <- paste0(unmatch.data$New.Genus[i], " ", unmatch.data$New.Hybrid.marker[i], " ", unmatch.data$New.Species[i], sep="")
    } 
    
    # the rest cases: names Hybrid and Infraspecific
    # Rosa × odorata var. gigantea
    else{
      Acc.names <- paste0(unmatch.data$New.Genus[i], " ", unmatch.data$New.Hybrid.marker[i], " ", unmatch.data$New.Species[i], unmatch.data$New.Infraspecific.rank[i], " ", unmatch.data$New.Species[i], sep="")
    }
    
    ncbi.id <- NCBI.data$NCBI_id[i]
    
    dd <- grep(Acc.names, WCSP$scientificName)
    #output
    ifelse(is.na(dd), print(paste0(Acc.names, ",NA", sep="")), print(paste0(Acc.names, ",", ncbi.id, ",", WCSP$acceptedNameUsageID[dd[1]], sep="")))
  }
  
}


# > grep("Arquita trichocarpa", NCBI$scientificName)
# [1] 36275 36276
# > NCBI$scientificName[c(36275, 36276)]
# [1] "Arquita trichocarpa var. trichocarpa" "Arquita trichocarpa var. boliviana"  
# > grep("Arquita trichocarpa", WCSP$scientificName)
# [1] 910038 910132
# > WCSP$scientificName[c(910038, 910132)]
# [1] "Arquita trichocarpa"                "Arquita trichocarpa var. boliviana"
# > grep("Arquita trichocarpa", tt$Taxon)
# [1] 2339
# > tt[2339,]
# # A tibble: 1 x 25
# Taxon Genus Hybrid.marker Species Abbrev Infraspecific.r… Infraspecific Authority ID    Plant.Name.Index
# <chr> <chr> <chr>         <chr>   <chr>  <chr>            <chr>         <chr>     <chr> <lgl>           
#   1 Arqu… Arqu… NA            tricho… NA     var.             trichocarpa   NA        NA    FALSE           
# # … with 15 more variables: TPL.version <dbl>, Taxonomic.status <chr>, Family <chr>, New.Genus <chr>,
# #   New.Hybrid.marker <chr>, New.Species <chr>, New.Infraspecific.rank <chr>, New.Infraspecific <chr>,
# #   New.Authority <chr>, New.ID <chr>, New.Taxonomic.status <chr>, Typo <lgl>, WFormat <lgl>,
#   Higher.level <lgl>, Date <date>