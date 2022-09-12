#!/bin/bash 
set -euo pipefail

#RGI v5.2.1 with v3.2.4 database 
rgi main -i card_oxa.faa -t protein -o rgi_afp_output/card_with_card_annotation -a BLAST --local
rgi main -i ncbi_oxa.faa -t protein -o rgi_afp_output/ncbi_with_card_annotation -a BLAST --local
#AMRFinderPlus v3.10.40 with 2022-08-09.1
amrfinder -p ncbi_oxa.faa -o rgi_afp_output/ncbi_with_ncbi_annotation.txt
amrfinder -p card_oxa.faa -o rgi_afp_output/card_with_ncbi_annotation.txt
