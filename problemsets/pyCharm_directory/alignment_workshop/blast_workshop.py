#!/usr/bin/env python3
import pandas as pd
import os
import re

'''
1a. query sequence is 217 AA
1b. 13144 sequences are in the PIR1 database
1c. BL50 was the scoring matrix used
1d. gap penalty is -10 when a -2 penalty when the gap is extended
1e. the evaulation of hits. E values determine homology
1f. the highest scoring sequence is P20432. percent id and similarity are different in that identity required the same residue in a location rather than similar ones. no 100% identity match because query isnt in the database
1g. 1 gap in best alignment. 16 gaps in second best alignment

2a. the highest E value shown is 5. the worst E value should be around 13144 or the size of the database.
2b. P0ACA5 has the worst statistically significant E value of 0.00029
2c. the highest scoring non-homolog is P14942 with an E value of 0.0011. it may be non-homologous because it has a truncated thioredo domain
2d. the E value for the highest non-homolog should be slightly higher than 0.001
2e. The E value for the most distant homolog is 0.00029
2f. do another alignment of the homolog in question
'''

'''
# this block gets every file in directory and writes them as new files with the lines that start with # removed
directory = 'search_results'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    with open (f, 'r') as file:

        with open(f'{filename}', 'w') as new_file:

            for line in file:
                if re.search(r'^#', line):
                    continue
                new_file.write(line)

'''

directory = 'new_search_results'
file_name_list = []
dataframes_list = []
df = pd.DataFrame()
temporary_df = pd.DataFrame()


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    file_name_list.append(f)

    with open(f, 'r') as file:
            df = pd.read_csv(file, sep='\t')
            dataframes_list.append(df)

print(dataframes_list)




























