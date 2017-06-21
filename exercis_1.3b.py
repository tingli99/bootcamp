
def reverse_complement(seq):
    """Compute reverse complement of a sequence."""

    # Initialize reverse complement
    rev_seq = ''

    rev_seq = seq[::-1]
    rev_seq = rev_seq.upper()
    rev_seq = rev_seq.replace('A','t')
    rev_seq = rev_seq.replace('T','a')
    rev_seq = rev_seq.replace('G','c')
    rev_seq = rev_seq.replace('C','g')
    rev_seq = rev_seq.upper()
    return rev_seq
