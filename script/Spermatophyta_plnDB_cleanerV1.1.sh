#!/bin/bash

t_file=$1
output_file=$2

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
#forma #keep
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
#cf.
#aff.
#environmental
#also remove extra "_" and replace"," as "_"
#_var._floribunda_var._floribunda_

#reformat is as "NCBI_id,species,rank"
sed 's/ /_/g;s/,/_/g;s/_\+/_/g;' $t_file >${output_file}.tmp
sed -i '/environmental_/d;/unclassified_/d;/_incertae_sedis/d;/_clade/d;/_superclade/d;/_Group/d;/_group/d;/_complex/d;/_\(type_*\)/d;/_lineages/d;/C3_/d;/C4_/d;/_sensu_lato/d;/_samples/d;/_alliance/d;/_division/d;/_hybrid_/d;/_cultivar/d;/_subgroup/d;/_form/d;/_cf._/d;/_aff._/d;/ungrouped_/d;/unpublished_/d;/no rank/d' ${output_file}.tmp

# sed -i '/no_rank/d' Spermatophyta58024_plnDB02032020_nodupl_bashcleaned.csv
sed '/	class	/d;/	section	/d;/	series	/d;/	species group	/d;/	subclass	/d;/	subfamily	/d;/	subgenus	/d;/	suborder	/d;/	subsection	/d;/	subtribe	/d;/	tribe	/d' ${output_file}.tmp|cut -f1,5,7 --output-delimiter "," >${output_file}.csv

rm ${output_file}.tmp


