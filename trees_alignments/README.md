## general alignment and NJ tree inference 
```bash
mafft --auto card_canonical_card_prev_and_ncbi_oxa_dedeup.faa > card_canonical_card_prev_and_ncbi_oxa_dedeup.aln
rapidnj -i fa -t p  card_canonical_card_prev_and_ncbi_oxa_dedeup.aln > card_canonical_card_prev_and_ncbi_oxa_dedeup.nj.tre
```

## quick-and-dirty to remove outliers  (not used)
```bash
iqtree2 -k 01.shortnames.nj.tre ## will generate a PDA file with seq names etc.
gotree stats edges -i 01.shortnames.nj.tre  | sort -nk 3  | tail -n 30 | cut -f 9 | sort | uniq >> 01.shortnames.nj.tre.pda
```
PDA file needs some editing. Then
```bash
gotree stats edges -i 01.shortnames.nj.tre  | sort -nk 3  | tail -n 30 | cut -f 9 | sort | uniq >> 01.shortnames.nj.tre.pda
mafft --ep 0.3 --auto 03.sans_longbranches.aln > 04.sans_realign.aln
```
## to remove outlier (that we found by eye from prev alignment):
```
goalign subset --unaligned -r -e WP_063839877 -i card_canonical_card_ncbi_oxa_dedeup.faa > dededup_minux_OXA-PR.fas 
```
and then mafft again to align
