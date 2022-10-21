#!/usr/bin/env python3


class DNA_sequnce(object):

    # class attributes
    def __init__(self, sequence, sequence_name, organism):
        self.sequence = sequence
        self.sequence_name = sequence_name
        self.organism = organism

    def sequence_length(self):
        length = len(self.sequence)
        return length

    def nucleotide_comp(self):

        A_count = 0
        T_count = 0
        G_count = 0
        C_count = 0

        comp_dict = {}

        for i in self.sequence:
            i = i.upper()
            if i == 'A':
                A_count += 1
            if i == 'T':
                T_count += 1
            if i == 'G':
                G_count += 1
            if i == 'C':
                C_count += 1

        comp_dict['A'] = A_count
        comp_dict['T'] = T_count
        comp_dict['G'] = G_count
        comp_dict['C'] = C_count

        return comp_dict

    def GC_content(self):

        sequence = self.sequence

        G_count = 0
        C_count = 0

        for i in sequence:
            i = i.upper()
            if i == 'G':
                G_count += 1
            if i == 'C':
                C_count += 1

        GC_content = 100 * ((G_count + C_count) / len(sequence))
        return GC_content

    def fasta_formatter(self):

        header_string = f'>{self.sequence_name} {self.organism}'
        sequence_string = self.sequence

        fasta_string = f'{header_string}\n{sequence_string}'
        return fasta_string



DNA_seq1 = DNA_sequnce('ATAGGGCAATTCTGACTTTACGG', 'BRCA1', 'Homo sapiens')

print(DNA_seq1.sequence_length())
print(DNA_seq1.nucleotide_comp())
print(DNA_seq1.GC_content())
print(DNA_seq1.fasta_formatter())