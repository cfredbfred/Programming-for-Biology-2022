#!/usr/bin/env python3
import re

fasta_file = input('Input fasta file path: ')

fasta_dict = {}

sequence_headers = []
sequences = []

sequence_fractions = []

# THIS HECKING WORKS!!
with open(fasta_file, 'r') as filo:
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