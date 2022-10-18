#!/usr/bin/env python

import os, sys

from fastq_file_to_sequence_list import *


def count_kmers(sequences_file, kmer_length):

    kmer_count_dict = dict()
    master_kmer_list = []

    ##################
    ## Step 2:
    ## begin your code

    sequences_list = seq_list_from_fastq_file(sequences_file)

    for sequence in sequences_list:
        current_kmer_list = sequence_to_kmer_list(sequence, kmer_length)
        master_kmer_list += current_kmer_list

    for kmer in master_kmer_list:
        if kmer in kmer_count_dict:
            kmer_count_dict[kmer] += 1
        if kmer not in kmer_count_dict:
            kmer_count_dict[kmer] = 1



    ## end your code
    ################

    return kmer_count_dict


def main():

    progname = sys.argv[0]

    usage = "\n\n\tusage: {} filename.fastq kmer_length num_top_kmers_show\n\n\n".format(
        progname
    )

    if len(sys.argv) < 4:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    kmer_length = int(sys.argv[2])
    num_top_kmers_show = int(sys.argv[3])

    kmers_dict = count_kmers(fastq_filename, kmer_length)

    top_values = sorted(kmers_dict, key=kmers_dict.get, reverse=True)[:num_top_kmers_show]

    final_values = []
    for i in top_values:
        final_values.append(kmers_dict[i])

    final_top_kmers_dict = {}

    for i in range(0, len(final_values)):
        final_top_kmers_dict[top_values[i]] = final_values[i]

    print(final_top_kmers_dict)





    sys.exit(0)  # always good practice to indicate worked ok!


if __name__ == "__main__":
    main()
