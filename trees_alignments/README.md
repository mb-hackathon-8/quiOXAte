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
## To remove outlier (that we found by eye from prev alignment):
```bash
goalign subset --unaligned -r -e WP_063839877 -i card_canonical_card_ncbi_oxa_dedeup.faa > dededup_minux_OXA-PR.fas 
mafft --auto --ep 0.23 dededup_minux_OXA-PR.fas > dededup_minux_OXA-PR.aln
iqtree2 -s dededup_minux_OXA-PR.aln  -m LG --ninit 2 -nt 12
```
The ML tree file will be called  `dededup_minux_OXA-PR.aln.treefile` 

## Renaming alignment sequences 
```bash
grep ">" 004.card_canonical_card_ncbi_oxa_dedeup_gaps+out_removed.aln | cut -c 2- | gawk -F '|'  '{print $2"\t"$0}' > 006.newnames.tsv
goalign rename -m 006.newnames.tsv --revert  -i 004.card_canonical_card_ncbi_oxa_dedeup_gaps+out_removed.aln > 006.newnames.aln
```

## annotate internal nodes 
```bash
treetime mugration --tree 006.newnames.iq.tre --states ../annotations/ncbi_card_annotation_comparion/families.tsv --attribute "NCBI Family" --outdir 003.tt
mv 003.tt/annotated_tree.nexus 007.annotated_ncbifamily.nexus
```

