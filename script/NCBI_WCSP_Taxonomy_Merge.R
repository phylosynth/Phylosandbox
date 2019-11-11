rm(list=ls())
#loading libraries
library("tidyverse")

#reading in tables

WCSP <- read_csv("results/powoNames.csv", col_names = T)
NCBI <- read_csv("results/Spermatophyta_clean11082019.csv", col_names = T)
#modify the shared species column to join the two tables
names(NCBI)[4] <- "scientificName"
NCBI$scientificName <- gsub("_", " ", NCBI$scientificName)

#join the tables
WCSP_NCBI_cmb <- left_join(WCSP, NCBI, by="scientificName")

#output
write_csv(WCSP_NCBI_cmb, "results/WCSP_NCBI_join_clean11082019.csv")
