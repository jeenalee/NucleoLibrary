RNA_dict = {
    'A' : 'U',  'C' : 'G',
    'U' : 'A',  'G' : 'C'
    }

RNA_to_DNA_dict = {
    'A' : 'T',  'C' : 'G',
    'U' : 'A',  'G' : 'C'
    }

def complement(s):
    """Returns the complementary RNA sequence."""
    s = s.upper()
    complement = ""

    for nucleotide in s:

        if nucleotide not in RNA_dict:
            raise ValueError("At least one non-nucleotide is given. \
                              Make sure no spaces areincluded.")

        complement = RNA_dict[nucleotide] + complement

    return complement

def reverse(s):
    """Returns the reversed RNA sequence."""
    s = s.upper()
    reverse = ""

    for n in s:
        reverse = n + reverse

    return reverse

def convert_to_DNA(s):
    """Converts the RNA sequence to DNA."""
    s = s.upper()
    DNA = ""

    for nucleotide in s:

        if nucleotide not in RNA_dict:
            raise ValueError("At least one non-nucleotide is given. \
                              Make sure no spaces areincluded.")

        DNA = RNA_to_DNA_dict[nucleotide] + DNA

    return DNA

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
    """Returns Boolean whether query exists in the RNA sequence."""
    return q in s

def highlight(s, q, highlighter="-"):
    """Returns the RNA sequence with the query highlighted"""
    for nucleotide in s:

        if nucleotide not in RNA_dict:
            raise ValueError("At least one non-nucleotide is given. \
                              Make sure no spaces areincluded.")
    
    if q in s:
        q_highlight = highlighter + q + highlighter
        s_ = s.replace(q, q_highlight)

    return s_

# def find_hairpin(s):
