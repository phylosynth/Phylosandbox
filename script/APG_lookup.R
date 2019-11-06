rm(list=ls())
#loading libraries
library("tidyverse")
library("taxonlookup")

#read WCSP species list

WCSP <- read_csv("../data/WCSP_DI_taxon.txt", col_names = F)

names(WCSP) <- c("WC_ID", "species")

#head(WCSP)
WCSP$species <- gsub("_", " ", WCSP$species)
WCSP1 <- WCSP %>% select(species, WC_ID)

Tmp_table <- lookup_table(unique(WCSP$species), by_species=TRUE)
APG_table <- Tmp_table %>% mutate(species=row.names(Tmp_table)) %>% select(species, genus, family, order, group)
write_csv(APG_table, "../results/WCSP_APG_lookup.csv")

#checking the taxonomy scope

#> APG_table %>% group_by(group) %>% summarise(group_n = n())
## A tibble: 4 x 2
#  group         group_n
#  <chr>           <int>
#1 Angiosperms    376423
#2 Bryophytes          2
#3 Gymnosperms      1566
#4 Pteridophytes   13814

#unique(APG_table$group)
#Angiosperms
#Bryophytes
#Gymnosperms
#Pteridophytes
#Well since we only work on Spermatophytes, "Bryophytes" and "Pteridophytes" will be excluded then


#add in WCSP unique id
table_big <- left_join(APG_table, WCSP1)
write_csv(table_big, "../results/WCSP_APG_lookup_ID.csv")

Spermatophytes <- table_big %>% filter(group == "Angiosperms" | group == "Gymnosperms")
#> dim(Spermatophytes)
#[1] 378026      6
#> unique(Spermatophytes$group)
#[1] "Angiosperms" "Gymnosperms"
#> dim(table_big)
#[1] 391842      6
write_csv(Spermatophytes, "../results/Spermatophytes_APG_wcspID.csv")
