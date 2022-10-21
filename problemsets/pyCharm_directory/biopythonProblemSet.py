#!/usr/bin/env python3
from typing import List, Any

import Bio
from Bio import SeqIO
import re


sequence_count = 0
'''
nucleotide_count = 0
shortest_length = float('inf')
longest_length = 0
GC_content_list = []
G_count = 0
C_count = 0
'''

id_list = []
description_list = []
sequences_list = []

for seq_record in SeqIO.parse('uniprot_sprot.fasta', 'fasta'):

    # counts number of sequences in fasta file
    if seq_record.seq:
        sequence_count += 1

    id_list.append(seq_record.id)
    description_list.append(seq_record.description)
    sequences_list.append(seq_record.seq)


'''
    # counts the total number of nucleotides
    nucleotide_count += len(seq_record.seq)

    # keeps track of the length of the shortest sequence
    if len(seq_record.seq) < shortest_length:
        shortest_length = len(seq_record.seq)

    # keeps track of the length of the longest sequence
    if len(seq_record.seq) > longest_length:
        longest_length = len(seq_record.seq)
'''
'''
    # occupies GC content list
    G_count = seq_record.seq.count('G')
    C_count = seq_record.seq.count('C')
    GC_content = 100 * ((G_count + C_count) / len(seq_record.seq))
    GC_content_list.append(GC_content)
    GC_content = 0
'''





'''
average_length = nucleotide_count / sequence_count
average_GC_content = sum(GC_content_list) / len(GC_content_list)
max_GC_content = max(GC_content_list)
min_GC_content = min(GC_content_list)
'''

'''
print(sequence_count)
print(nucleotide_count)
print(average_length)
print(shortest_length)
print(longest_length)
print(average_GC_content)
print(max_GC_content)
print(min_GC_content)
'''

# extracts genus and species as a string from record seq descriptions and occupies the genus_species_list with the results
genus_species_list = []

for i in description_list:

    found = re.search(r'OS=\w+ \w+', i)
    if found:
        genus_species_list.append((found.group())[3:])


genus_species_count = 0
for i in genus_species_list:
    if 'Salmonella paratyphi' in i:
        genus_species_count += 1


sub_description_list = []
sub_sequence_list = []

for i in range(0, len(description_list)):
    if 'Salmonella paratyphi' in description_list[i]:
        sub_description_list.append(description_list[i])
        sub_sequence_list.append(str(sequences_list[i]))


with open ('smaller_db', 'w') as new_file:
    for i in range(0, len(sub_description_list)):
        new_file.write('>' + sub_description_list[i] + '\n')
        new_file.write(sub_sequence_list[i] + '\n')




