#!/usr/bin/env python3

import re

'''
nobody_positions = []

with open ('Python_07_nobody.txt', 'r') as filo:
    for line in filo:
        for found in re.finditer(r'Nobody', line):
            nobody_positions.append(int(found.start()) + 1)
            print(nobody_positions)
            nobody_positions = []

print(nobody_positions)

'''

'''
with open ('Python_07_nobody.txt', 'r') as filo, open ('Chrischin.txt', 'w') as new_filo:
    for line in filo:
        new_line = re.sub(r'Nobody', 'Chrischin', line)
        new_filo.write(new_line)
'''

'''
fasta_header_list = []

with open ('Python_07.fasta.txt', 'r') as fasta_file:
    for line in fasta_file:
        fasta_header = re.findall(r'>.+', line)
        if fasta_header:
            fasta_header_list.append(fasta_header[0])

print(fasta_header_list)
'''

'''
# THIS WAS HECKING HARD

fasta_header_list = []
sequence_names = []
sequence_descriptions = []
sequence_fractions = []

with open ('Python_07.fasta.txt', 'r') as fasta_file:
    for line in fasta_file:
        fasta_header = re.search(r'^>', line)
        if fasta_header:

            found_name = re.search(r'\|\w+\.\w+\|', line)
            sequence_name = found_name[0]
            clean_seq_name = sequence_name.replace('|', '')
            sequence_names.append(clean_seq_name)

            found_description = re.search(r'\|[^\|]+$', line)
            description_name = found_description[0]
            clean_description_name = description_name.replace('|', '')
            sequence_descriptions.append(clean_description_name)

for i in range(0, len(sequence_names)):
    print(f'id:{sequence_names[i]} desc:{sequence_descriptions[i]}')
'''

# FASTA PARSER

fasta_dict = {}

sequence_headers = []
sequences = []

sequence_fractions = []

# THIS HECKING WORKS!!
with open('Python_07.fasta.txt', 'r') as filo:
    for line in filo:

        found_header = re.search(r'^>.+', line)
        if found_header:
            sequence_header = found_header.group()
            sequence_headers.append(sequence_header.rstrip())

        found_sequence = re.search(r'^\w+', line)
        if found_sequence:
            sequence_fraction = found_sequence.group()
            sequence_fractions.append(sequence_fraction.rstrip())

        found_blank = re.search(r'^\s', line)
        if found_blank:
            sequences.append(''.join(sequence_fractions))
            sequence_fractions = []

for i in range(0, len(sequence_headers)):
    fasta_dict[sequence_headers[i]] = sequences[i]

print(fasta_dict)






