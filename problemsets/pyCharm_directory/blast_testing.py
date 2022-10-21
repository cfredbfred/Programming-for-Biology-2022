#!/usr/bin/env python3

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

'''
sequence_data = open('cam1_protein.fasta').read()
result_handle = NCBIWWW.qblast("blastp", 'nr', sequence_data)
with open ('blast_results.xml', 'w') as new_file:
    new_file.write(result_handle.read())
'''

# below lines parse blast result into titles for each hit


with open ('blast_results.xml', 'r') as cam1_blast_results:
    blast_record = NCBIXML.read(cam1_blast_results)

E_VALUE_THRESH = 0.04

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print("****Alignment****")
            print("sequence:", alignment.title)


