#!/bin/bash

while read -r line; do 
	name=$(echo $line|sed 's/no rank/varietas/g'); 
	sed -i "s/$line/$name/g" ../results/Spermatophyta58024_plnDB02032020_nodupl.csv; 
done <wrongly_assig_var.txt

#corrwct two "no rank" records
#while read -r line ; do 
#	name=$(echo $line|sed 's/no_rank/species/g'); 
#	sed -i "s/$line/$name/g" Spermatophyta58024_plnDB02032020_nodupl_bashcleaned.csv
#done <wrongly_assig_no_rank.txt 


while read -r line; do 
	if grep -q "var\." <<< "$line" ; then
		name=$(echo $line|sed 's/forma/varietas/g');
	elif grep -q "subsp\." <<< "$line"; then
		name=$(echo $line|sed 's/forma/subspecies/g');
	else
		name=$(echo $line|sed 's/forma/species/g');
	fi
	#echo $name;
	sed -i "s/$line/$name/g" ../results/Spermatophyta58024_plnDB02032020_nodupl.csv; 
done <wrongly_assig_forma.txt

