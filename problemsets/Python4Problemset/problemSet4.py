#!/usr/bin/env python3

import sys
import random

'''
fav_list = ['fav1', 'fav2', 'fav3', 'fav4', 'fav5']

print(fav_list)

fav_list[2] = 'hello'

fav_list.append('new item')

fav_list.insert(0, 'first obj')

fav_list.insert(2, 'middle element')

fav_list.pop()
fav_list.pop(0)
fav_list.pop(1)

print(','.join(fav_list))

print(fav_list)
'''

'''
taxa = 'sapiens, erectus, neanderthalensis'

print(taxa)
print(taxa[1])
print(type(taxa)) 

#type is string!

species = taxa.split(', ')
print(species)
print(species[1])
print(type(species))

# type is list!

species_alphabetical = sorted(species)
print(species_alphabetical)
species_length = sorted(species, key=len)
print(species_length)
'''

'''
count = 0
while count < 100:
    count += 1
    print(count)
'''

'''
n = 100
value = 1

while n >= 1:
    value *= n
    n -= 1
    
print(value)
'''

'''
loopy = [101,2,15,22,95,33,2,27,72,15,52]
for i in loopy:
    if i % 2 == 0:
        print(i)
'''

'''
even_sum = 0
odd_sum = 0

loopy = [101,2,15,22,95,33,2,27,72,15,52]
for i in loopy:
    if i % 2 == 0:
        even_sum = even_sum + i
    if i % 2 != 0:
        odd_sum = odd_sum + i
        
print(f'Sum of even numbers: {even_sum}')
print(f'Sum of odds: {odd_sum}')
'''

'''
for i in range(0, 101):
    print(i)
'''

'''
numbers = [print(i) for i in range (0, 101)]
'''

'''
x = int(sys.argv[1])
y = int(sys.argv[2])

numbers = [print(i) for i in range (x, (y+1))]
'''

'''
DNAs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for i in DNAs:
    print(f'{len(i)}\t{i}')
'''   

'''
empty_list = []
DNAs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
    
list_of_tups = [empty_list.append((len(i), i)) for i in DNAs]
    
print(empty_list)
'''

'''
DNAs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for i in DNAs:
    print(f'{DNAs.index(i) + 1}\t{len(i)}\t{i}')
'''

'''
DNA_new = ''

DNA_seq = 'ATCGCCAATCGCCAATCGCCAATCGCCAATCGCCAATCGCCAATCGCCAATCGCCAATCGCCA'


seq_length = len(DNA_seq)


for i in range (0, seq_length):
    posA = random.randrange(0, (seq_length - 1))
    
    
    posB = random.randrange(0, (seq_length - 1))
    
    
    posA_value = DNA_seq[posA]
    
    
    posB_value = DNA_seq[posB]
    
    
    DNA_new = DNA_seq.replace(DNA_seq[posA], posB_value)
    
    DNA_new = DNA_seq.replace(DNA_seq[posB], posA_value)
    

print(DNA_seq)
print(DNA_new)
'''    
    
gi|170746|gb|M12277.1|WHTH4091      ---------AGCACCCT------CCCACCTCATCCCA-CCCTTCTGATCT
gi|603555|emb|X83548.1|             TCTAGAGATGGCGCCATTTGATTCCAGCAGCCACAAAGCACTAGAACAAT
                                             .**.**.*      **..*. *.:*..* *.**: :..:.*

gi|170746|gb|M12277.1|WHTH4091      CAATCCAACGTCGCATCTCCACCGTCTCGCGG-ATCGACCCAG-CGAAG-
gi|603555|emb|X83548.1|             CGATGCTAAGAGGTGACAGGAAAAACAGGCTGCAAAGACCCAGACAATGG
                                    *.** *:*.*: * .:*:  *...:*: ** * *:.******* *.*:* 

gi|170746|gb|M12277.1|WHTH4091      -TCCCTCCCG----CCCCCAAAGTCCCC---------CAAATCTTGCAGT
gi|603555|emb|X83548.1|             AATGCAGCGGTGGTCAGCCTAAAACACTGTAGAAGGGCAAGATGAGCTGA
                                     :  *: * *    *. **:**.:*.*          ***.:  :**:*:

gi|170746|gb|M12277.1|WHTH4091      -TCCCTCCTAAATCCTCCCCATATAAACCAAC-------------CCCCC
gi|603555|emb|X83548.1|             GTAATTTTTAACTGGGCATCATTTTTAGAAACTGGAGTTTAAGTACCCCC
                                     *.. *  ***.*   *. ***:*::* .***             *****

gi|170746|gb|M12277.1|WHTH4091      G---CCCTCAGATCCCTAATCCCATCGCAAGCATCAG--ACT--------
gi|603555|emb|X83548.1|             TTTTCCATTTTTTCCTGAAGTCGTGGGCAGGGCGCAAGGTCTGTGAATCG
                                        **.* : :***  **  * :  ***.* . **.  :**        

gi|170746|gb|M12277.1|WHTH4091      -CCCTCCAAAGCAGGCAG-------CAGCTCCTCTTCT--TCC---TAAT
gi|603555|emb|X83548.1|             GCCGACCGGATGCAGCTGGTGTGGAGAGTTCCCAATCAGGTCCGATTTAT
                                     ** :**..*  ..**:*        ** *** .:**:  ***   *:**

gi|170746|gb|M12277.1|WHTH4091      CACACTATCTCGGAGAGGAGCGG---------------------------
gi|603555|emb|X83548.1|             TACTATATAAAGTACTGCTGCGAGGCTTGCCGTGTTGCATTTTGTTTAGT
                                     **:.***.:.* * :* :***.                           

gi|170746|gb|M12277.1|WHTH4091      -----CCATGTCTGGGCGCGACAAGGGCGGCAAGGGGCTGGGCAAGGGCG
gi|603555|emb|X83548.1|             ACAAGACATGTCTGGGCGCGGCAAAGGCGGGAAGGGTCTGGGCAAAGGAG
                                         .**************.***.***** ***** ********.**.*

gi|170746|gb|M12277.1|WHTH4091      GCGCCAAGCGGCACCGGAAGGTCCTCCGCGACAACATCCAGGGCATCACC
gi|603555|emb|X83548.1|             GCGCTAAGCGCCACCGCAAAGTTCTGCGCGACAACATTCAGGGCATCACC
                                    **** ***** ***** **.** ** *********** ************

gi|170746|gb|M12277.1|WHTH4091      AAGCCGGCGATCCGGAGGCTGGCCAGGAGGGGCGGCGTGAAGCGCATCTC
gi|603555|emb|X83548.1|             AAGCCCGCCATCCGACGCCTGGCACGGCGTGGAGGCGTTAAGCGCATCTC
                                    ***** ** *****..* *****..**.* **.***** ***********

gi|170746|gb|M12277.1|WHTH4091      CGGCCTCATCTACGAGGAGACCCGCGGCGTCCTCAAGATCTTCCTCGAGA
gi|603555|emb|X83548.1|             AGGCCTTATATACGAGGAGACACGCGGAGTTCTTAAAGTGTTTTTGGAGA
                                    .***** **.***********.*****.** ** **..* **  * ****

gi|170746|gb|M12277.1|WHTH4091      ACGTCATCCGCGACGCCGTCACCTACACCGAGCACGCCCGCCGCAAAACC
gi|603555|emb|X83548.1|             ATGTAATCCGCGATGCAGTTACCTACACGGAGCACGCCAAACGCAAGACA
                                    * **.******** **.** ******** *********...*****.**.

gi|170746|gb|M12277.1|WHTH4091      GTCACCGCCATGGACGTCGTCTACGCGCTCAAGCGCCAGGGCCGCACCCT
gi|603555|emb|X83548.1|             GTCACAGCCATGGACGTGGTTTACGCGCTCAAGCGCCAGGGCCGCACCCT
                                    *****.*********** ** *****************************

gi|170746|gb|M12277.1|WHTH4091      CTACGGCTTCGGAGGCTAGATTTGTGTGGTGAAGCAACTTCCTCGTTTGC
gi|603555|emb|X83548.1|             GTATGGCTTTGGCGGCTG------AGTGTTTTACTTACTTACACGGTTCC
                                     ** ***** **.****.      :*** * :*  :****.*:** ** *

gi|170746|gb|M12277.1|WHTH4091      TCTGTG------ATCTGTGCTGTCGTAGATGAGATTTACTGATTTG---G
gi|603555|emb|X83548.1|             TCAAAGGCCCTTCTCAGGGCCACCCATGAAGTCTGTGAAAGAGCTGTAGA
                                    **:.:*      .**:* ** . * ::**:*: : * *.:**  **   .

gi|170746|gb|M12277.1|WHTH4091      CGTGCGCCGGTTGTATTCT------------GTCATGGGGTTCAGTGGGC
gi|603555|emb|X83548.1|             CTAAAGATAGTTAATTTCTTAAGAACACTTAAACGTATGGCAGTTTTGGC
                                    * :..*. .***.::****            .:*.*. ** : : * ***

gi|170746|gb|M12277.1|WHTH4091      TGTGTA---ATACCTTG--------CTCTGTACTTCTG--TTCAATG-CA
gi|603555|emb|X83548.1|             AAATTAGCGATTCCACATAAGCAGTCGCTGAAGTTTGAGGTTCGGTGCCC
                                    :.: **   **:**: .        * ***:* **  .  ***..** *.

gi|170746|gb|M12277.1|WHTH4091      ATCACTTCTATTCTGAA---------
gi|603555|emb|X83548.1|             CTTTCAGCATTACTTAGTGGTTAAAA
                                    .* :*: *::*:** *.         

