#!/usr/bin/env python3

DNA_sequence = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

A_count = 0
T_count = 0
C_count = 0
G_count = 0

for i in range(0, len(DNA_sequence)):
    if DNA_sequence[i] == 'A':
        A_count = A_count + 1
    if DNA_sequence[i] == 'T':
        T_count = T_count + 1
    if DNA_sequence[i] == 'C':
        C_count = C_count + 1
    if DNA_sequence[i] == 'G':
        G_count = G_count + 1
 

print(str(A_count) + ' ' + str(C_count) + ' ' + str(G_count) + ' ' + str(T_count))

