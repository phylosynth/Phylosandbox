#!/bin/bash

python3 ~/apps/PyPHLAWD/src/get_ncbi_tsv_miao.py -t Spermatophyta -d /data_vol/miao/plnDB20191101/plnDB20191101.db -o Spermatophyta58024_plnDB01022020.table
 
bash ../script/Spermatophyta_plnDB_cleanerV1.1.sh Spermatophyta58024_plnDB01022020.table Spermatophyta58024_plnDB01022020

python ../script/remove_duplicate.py

python Spermatophyta_sp_authority_format.py

python Spermatophyta_clean3.14snakeV2.py