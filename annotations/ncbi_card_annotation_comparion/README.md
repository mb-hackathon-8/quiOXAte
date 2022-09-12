# Comparison of OXA annotations across NCBI and CARD

Namely taking all the OXA from each database and running AFP and RGI on these protein sequences to see how the opposite database's tool and their own tool annotate them.
This is done using the `run.sh` script and the `annotation_comparison.ipynb` notebook and generates `card_oxa_annotations.tsv` and `ncbi_oxa_annotations.tsv`

	#!/bin/bash 
	set -euo pipefail
	
	#RGI v5.2.1 with v3.2.4 database 
	rgi main -i card_oxa.faa -t protein -o rgi_afp_output/card_with_card_annotation -a BLAST --local
	rgi main -i ncbi_oxa.faa -t protein -o rgi_afp_output/ncbi_with_card_annotation -a BLAST --local
	#AMRFinderPlus v3.10.40 with 2022-08-09.1
	amrfinder -p ncbi_oxa.faa -o rgi_afp_output/ncbi_with_ncbi_annotation.txt
	amrfinder -p card_oxa.faa -o rgi_afp_output/card_with_ncbi_annotation.txt

0 CARD OXAs are incorrectly annotated by RGI
10 CARD OXAs are annotated as a different OXA by NCBI
0 CARD OXAs are missing in NCBI

1 NCBI OXAs are incorrectly annotated by NCBI
187 NCBI OXAs are annotated as a different OXA by CARD/RGI
17 NCBI OXAs are missing in CARD
