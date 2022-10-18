#!/usr/bin/env python

import os, sys
from Bio import SeqIO


## method: seq_list_from_fastq_file(fastq_filename)
##
##  Extracts the sequence lines from a fastq file and returns a list
##  of the sequence lines
##
##  input parameters:
##
##  fastq_filename :  name of the fastq file (type: string)
##
##  returns seq_list : list of read sequences.
##                    ie.  ["GATCGCATAG", "CGATGCAG", ...]

def seq_list_from_fastq_file(fastq_filename):
    seq_list = list()

    ## begin your code

    for record in SeqIO.parse(fastq_filename, 'fastq'):
        seq_list.append(str(record.seq))

    ## end your code

    return seq_list


# generates a kmer list of specified length from a sequence
def sequence_to_kmer_list(sequence, kmer_length):
    kmer_list = []

    for i in range(0, ((len(sequence) - kmer_length) + 1)):
        kmer_list.append(sequence[i:(i + kmer_length)])

    return kmer_list


def main():
    progname = sys.argv[0]

    usage = "\n\n\tusage: {} filename.fastq num_seqs_show\n\n\n".format(progname)

    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    num_seqs_show = int(sys.argv[2])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    print(seq_list[0:num_seqs_show])

    print(sequence_to_kmer_list(seq_list[0], 5))

    sys.exit(0)  # always good practice to indicate worked ok!


if __name__ == '__main__':
    main()
