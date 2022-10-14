#!/usr/bin/env python3

import re

'''
# fasta parser

fasta_dict = {}

sequence_headers = []
sequences = []

sequence_fractions = []

found_header = 0
found_sequence = 0

# works when there are no blank spaces separating (fasta headers + sequences)

with open('Python_08.fasta.txt', 'r') as filo:
    for line in filo:

        found_sequence = re.search(r'^[^\>]+', line)
        if found_sequence:
            sequence_fraction = line.strip()
            sequence_fractions.append(sequence_fraction)


        found_header = re.search(r'^>', line)
        if found_header:
            sequence = ''.join(sequence_fractions)
            sequences.append(sequence)
            sequence_fractions = []
            header = line.strip()
            sequence_headers.append(header)

sequence = ''.join(sequence_fractions)
sequences.append(sequence)
sequence_fractions = []

del sequences[0]

for i in range(0, len(sequence_headers)):
    fasta_dict[sequence_headers[i]] = sequences[i]


'''

# now onto the problems lol

# want a dictionary of dictionaries
# dictionary 1 = header_name : (dictionary = base : count))

# this works
'''
nested_dictionary = {}

for key in fasta_dict:
    nested_dictionary[key] = {'A' : fasta_dict[key].count('A'), 'T' : fasta_dict[key].count('T'), 'G' : fasta_dict[key].count('G'), 'C' : fasta_dict[key].count('C')}
'''

sequences = []
seq_names = []

sequence_codons_list = []

sequence_fractions = []

with open ('Python_08.fasta.txt', 'r') as filo:
    for line in filo:

        if re.search(r'^[^\>]+', line):
            sequence_fraction = line.strip()
            sequence_fractions.append(sequence_fraction)


        if re.search(r'^>', line):
            sequence = ''.join(sequence_fractions)
            sequences.append(sequence)
            sequence_fractions = []

            continue

sequence = ''.join(sequence_fractions)
sequences.append(sequence)
sequence_fractions = []

# populates the list of sequence names
for i in range(0, len(sequences)):
    seq_names.append(f'seq{i+1}-codons')

# introducing a space after every three nucleotides in a sequence and populating sequence_codons_list with the outputs
for seq in sequences:
    sequence_codons_list.append(' '.join([seq[i:i + 3] for i in range(0, len(seq), 3)]))

print(sequence_codons_list)





















