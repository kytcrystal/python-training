def to_rna(dna_strand):
    mapping = {"A": "U", "T": "A", "C": "G", "G": "C"}
    rna_strand = ""
    for nucleotide in dna_strand:
        if nucleotide in mapping:
            rna_strand += mapping.get(nucleotide)
    return rna_strand
