#!/usr/bin/env python3

# 1. Lists, strings, and tuples

# 2. Length is 842

# 3. Done

'''
4. The number of As in the sequence is: 167
The number of Ts in the sequence is: 187
The number of Gs in the sequence is: 218
The number of Cs in the sequence is: 270
'''

'''
5.
bird = 'chicken'
bird = bird.upper()
print(bird)
'''

'''
6. The number of As is 167
The number of Ts is 187
The number of Cs is 270
The number of Gs is 218
'''

# 7. RNA = GAUGGGAUUGGGGUUUUCCCCUCCCAUGUGCUCAAGACUGGCGCUAAAAGUUUUGAGCUUCUCAAAAGUCUAGAGCCACCGUCCAGGGAGCAGGUAGCUGCUGGGCUCCGGGGACACUUUGCGUUCGGGCUGGGAGCGUGCUUUCCACGACGGUGACACGCUUCCCUGGAUUGGCAGCCAGACUGCCUUCCGGGUCACUGCCAUGGAGGAGCCGCAGUCAGAUCCUAGCGUCGAGCCCCCUCUGAGUCAGGAAACAUUUUCAGACCUAUGGAAACUACUUCCUGAAAACAACGUUCUGUCCCCCUUGCCGUCCCAAGCAAUGGAUGAUUUGAUGCUGUCCCCGGACGAUAUUGAACAAUGGUUCACUGAAGACCCAGGUCCAGAUGAAGCUCCCAGAAUUCGCCAGAGGCUGCUCCCCCCGUGGCCCCUGCACCAGCAGCUCCUACACCGGCGGCCCCUGCACCAGCCCCCUCCUGGCCCCUGUCAUCUUCUGUCCCUUCCCAGAAAACCUACCAGGGCAGCUACGGUUUCCGUCUGGGCUUCUUGCAUUCUGGGACAGCCAAGUCUGUGACUUGCACGUACUCCCCUGCCCUCAACAAGAUGUUUUGCCAACUGGCCAAGACCUGCCCUGUGCAGCUGUGGGUUGAUUCCACACCCCCGCCCGGCACCCGCGUCCGCGCCAUGGCCAUCUACAAGCAGUCACAGCACAUGACGGAGGUUGUGAGGCGCUGCCCCCACCAUGAGCGCUGCUCAGAUAGCGAUGGUCUGGCCCCUCCUCAGCAUCUUAUCCGAGUGGAAGGAAAUUUGCGUGUGGAGUAUUUGGAUGACAGAAACACUUUUCG


'''
8.

DNA = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCT'

upper_DNA = DNA.upper()
RNA = upper_DNA.replace('T', 'U')
print(RNA)

GAUGGGAUUGGGGUUUUCCCCUCCCAUGUGCUCAAGACUGGCGCUAAAAGUUUUGAGCUUCUCAAAAGUCUAGAGCCACCGUCCAGGGAGCAGGUAGCUGCUGGGCUCCGGGGACACUUUGCGUUCGGGCUGGGAGCGUGCUUUCCACGACGGUGACACGCUUCCCUGGAUUGGCAGCCAGACUGCCUUCCGGGUCACUGCCAUGGAGGAGCCGCAGUCAGAUCCUAGCGUCGAGCCCCCUCUGAGUCAGGAAACAUUUUCAGACCUAUGGAAACUACUUCCUGAAAACAACGUUCUGUCCCCCUUGCCGUCCCAAGCAAUGGAUGAUUUGAUGCUGUCCCCGGACGAUAUUGAACAAUGGUUCACUGAAGACCCAGGUCCAGAUGAAGCUCCCAGAAUUCGCCAGAGGCUGCUCCCCCCGUGGCCCCUGCACCAGCAGCUCCUACACCGGCGGCCCCUGCACCAGCCCCCUCCUGGCCCCUGUCAUCUUCUGUCCCUUCCCAGAAAACCUACCAGGGCAGCUACGGUUUCCGUCUGGGCUUCUUGCAUUCUGGGACAGCCAAGUCUGUGACUUGCACGUACUCCCCUGCCCUCAACAAGAUGUUUUGCCAACUGGCCAAGACCUGCCCUGUGCAGCUGUGGGUUGAUUCCACACCCCCGCCCGGCACCCGCGUCCGCGCCAUGGCCAUCUACAAGCAGUCACAGCACAUGACGGAGGUUGUGAGGCGCUGCCCCCACCAUGAGCGCU

'''

'''
9.

DNA = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'
DNA_length = len(DNA)
A_count = DNA.count('A')
T_count = DNA.count('T')
AT_count = A_count + T_count
AT_content = (AT_count / DNA_length)
print(AT_content)

0.42042755344418054
'''

'''
10.
DNA = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'
sliced_DNA = DNA[99:200]
print(sliced_DNA)

GCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTG
'''

'''
11. 

DNA_substring = 'GCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTG'
G_count = DNA_substring.count('G')
print(G_count)

35
'''

'''
12.

DNA = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCT'
sliced_DNA = DNA[99:200]
upper_sliced_DNA = sliced_DNA.upper()
G_count = upper_sliced_DNA.count('G')
print(G_count)

35
'''

'''
13.

DNA = 'ATGCAGGGGAAACATGATTCAGGAC'
reverse_DNA = DNA[::-1] 

reverse_DNA = reverse_DNA.replace("A", "t")
reverse_DNA = reverse_DNA.replace("T", "a")
reverse_DNA = reverse_DNA.replace("G", "c")
reverse_DNA = reverse_DNA.replace("C", "g")

reverse_complement_DNA = reverse_DNA.upper()
print(reverse_complement_DNA)

GTCCTGAATCATGTTTCCCCTGCAT
'''

'''
14.

DNA  = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'

EcoRI_index = DNA.find('GAATTC')
EcoRI_starting_nucleotide_position = EcoRI_index + 1
print(f'EcoRI starting nucleotide is {EcoRI_starting_nucleotide_position} and ends at position {(EcoRI_starting_nucleotide_position) + 5}')

EcoRI starting nucleotide is 396 and ends at position 401
'''
