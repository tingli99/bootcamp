
def complement_base(base):
    """Returns the Watson-Crick complement of a base."""

    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq):
    """Compute reverse complement of a sequence."""

    # Initialize reverse complement
    rev_seq = ''

    for base in seq[::-1]:
        rev_seq += complement_base(base)
    return rev_seq
