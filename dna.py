DNA_dict = {
    'A' : 'T',  'C' : 'G',
    'T' : 'A',  'G' : 'C'
    }


DNA_to_RNA_dict = {
    'A' : 'U',  'C' : 'G',
    'T' : 'A',  'G' : 'C'
    }

def complement(s):
    """Returns the complementary DNA sequence."""
    s = s.upper()
    complement = ""

    for nucleotide in s:

        if nucleotide not in DNA_dict:
            raise ValueError("At least one non-nucleotide is given. \
                              Make sure no spaces areincluded.")

        complement = DNA_dict[nucleotide] + complement

    return complement


def reverse(s):
    """Returns the reversed DNA sequence."""
    s = s.upper()
    reverse = ""

    for n in s:
        reverse = n + reverse

    return reverse


def convert_to_RNA(s):
    """Converts the DNA sequence to RNA."""
    s = s.upper()
    RNA = ""

    for nucleotide in s:

        if nucleotide not in DNA_dict:
            raise ValueError("At least one non-nucleotide is given. \
                              Make sure no spaces areincluded.")

        RNA = DNA_to_RNA_dict[nucleotide] + RNA

    return RNA


def GCfraction(s):
    """Returns the fraction of GC of the DNA sequence."""
    length = float(len(s))
    s = s.upper()
    GC = float(0)
    
    for nucleotide in s:
        if nucleotide == 'G' or nucleotide == 'C':
            GC += 1

    GCfraction = round(GC/length, 2)

    return GCfraction
  

def is_present(s, q):
    """Returns Boolean whether query exists in the DNA sequence."""
    return q in s


def highlight(s, q, highlighter="-"):
    """Returns the DNA sequence with the query highlighted"""
    for nucleotide in s:

        if nucleotide not in DNA_dict:
            raise ValueError("At least one non-nucleotide is given. \
                              Make sure no spaces areincluded.")
    
    if q in s:
        q_highlight = highlighter + q + highlighter
        s_ = s.replace(q, q_highlight)

    return s_
