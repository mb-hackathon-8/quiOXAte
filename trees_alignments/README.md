## general alignment and NJ tree inference 
```bash
mafft --auto card_canonical_card_prev_and_ncbi_oxa_dedeup.faa > card_canonical_card_prev_and_ncbi_oxa_dedeup.aln
rapidnj -i fa -t d  card_canonical_card_prev_and_ncbi_oxa_dedeup.aln > card_canonical_card_prev_and_ncbi_oxa_dedeup.nj.tre
```

## quick-and-dirty to remove outliers 
```bash
iqtree2 -k 01.shortnames.nj.tre ## will generate a PDA file with seq names etc.
gotree stats edges -i 01.shortnames.nj.tre  | sort -nk 3  | tail -n 30 | cut -f 9 | sort | uniq >> 01.shortnames.nj.tre.pda
```
PDA file needs some editing.
