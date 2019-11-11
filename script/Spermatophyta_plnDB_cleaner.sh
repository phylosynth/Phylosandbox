#!/bin/bash

#this bash script will clean some "ugly" entries, and
#unclassified_
#_incertae_sedis
#_clade
#_superclade
#_Group
#_group
#_complex
#_(type_*)
#_lineages
#C3_
#C4_
#_sensu_lato
#_samples
#_alliance
#_division
#_hybrid_
#_cultivar
#_subgroup
#_form
#ungrouped_
#unpublished_
#no rank

#class
#forma
#section
#series
#species group
#subclass
#subfamily
#subgenus
#suborder
#subsection
#subtribe
#tribe

#reformat is as "NCBI_id,species,rank"
sed 's/,/_/g;s/__/_/g;' ../data/Spermatophyta_plnDB.table>../data/Spermatophyta_plnDB.table.tmp
sed -i '/unclassified_/d;/_incertae_sedis/d;/_clade/d;/_superclade/d;/_Group/d;/_group/d;/_complex/d;/_(type_*)/d;/_lineages/d;/C3_/d;/C4_/d;/_sensu_lato/d;/_samples/d;/_alliance/d;/_division/d;/_hybrid_/d;/_cultivar/d;/_subgroup/d;/_form/d;/ungrouped_/d;/unpublished_/d;/no rank/d' ../data/Spermatophyta_plnDB.table.tmp
sed '/	class	/d;/	forma	/d;/	section	/d;/	series	/d;/	species group	/d;/	subclass	/d;/	subfamily	/d;/	subgenus	/d;/	suborder	/d;/	subsection	/d;/	subtribe	/d;/	tribe	/d' ../data/Spermatophyta_plnDB.table.tmp|cut -f1,7,9 --output-delimiter "," >../results/Spermatophyta_plnDB_clean2.csv

