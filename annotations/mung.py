import pandas,numpy

_csv = pandas.read_csv('oxa_annotation.csv')

with open('fasta_headers.txt', 'r') as f:
    headers = f.read().strip().split('\n')
acc_dict = {}
for h in headers:
    acc = h.split('|')[1]
    acc_dict[acc] = h.strip('>')
# print(acc_dict)
_csv['fasta_header'] = ''
_csv['acc'] = ''
for row in _csv.iterrows():

    ref_nuc = row[1]['refseq_nucleotide_accession']
    ref_prot = row[1]['refseq_protein_accession']
    gb_nuc = row[1]['genbank_nucleotide_accession']
    gb_prot = row[1]['genbank_protein_accession']
    hd = ''
    ac = ''
    
    if ref_nuc in acc_dict:
        hd = acc_dict[ref_nuc]
        ac = ref_nuc
        _csv['fasta_header'] = numpy.where(_csv['refseq_nucleotide_accession'] == ref_nuc, hd, _csv['fasta_header'])
        _csv['acc'] = numpy.where(_csv['refseq_nucleotide_accession'] == ref_nuc, ac,_csv['acc'])
        
    elif ref_prot in acc_dict:
        hd = acc_dict[ref_prot]
        ac = ref_prot
        _csv['fasta_header'] = numpy.where(_csv['refseq_protein_accession'] == ref_prot, hd, _csv['fasta_header'])
        _csv['acc'] = numpy.where(_csv['refseq_protein_accession'] == ref_prot, ac,_csv['acc'])
        
    elif gb_nuc in acc_dict:
        hd = acc_dict[gb_nuc]
        ac = gb_nuc
        _csv['fasta_header'] = numpy.where(_csv['genbank_nucleotide_accession'] == gb_nuc, hd, _csv['fasta_header'])
        _csv['acc'] = numpy.where(_csv['genbank_nucleotide_accession'] == gb_nuc, ac,_csv['acc'])
        
    elif gb_prot in acc_dict:
        hd = acc_dict[gb_prot]
        ac = gb_prot
        _csv['fasta_header'] = numpy.where(_csv['genbank_protein_accession'] == gb_prot, hd, _csv['fasta_header'])
        _csv['acc'] = numpy.where(_csv['genbank_protein_accession'] == gb_prot, ac,_csv['acc'])
        
_csv.to_csv('oxa_annotation_munged.csv', index = False)