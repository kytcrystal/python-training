amino_acid = {"AUG": "Methionine",
              "UUU": "Phenylalanine", 
              "UUC": "Phenylalanine",
              "UUA": "Leucine",
              "UUG": "Leucine",
              "UCU": "Serine",
              "UCC": "Serine", 
              "UCA": "Serine",
              "UCG": "Serine",
              "UAU": "Tyrosine",
              "UAC": "Tyrosine",
              "UGU": "Cysteine",
              "UGC": "Cysteine",
              "UGG": "Tryptophan",
              "UAA": "STOP",
              "UAG": "STOP", 
              "UGA": "STOP"}


def proteins(strand):
    protein = []
    for codon_start in range(0, len(strand), 3):
        codon = strand[codon_start:codon_start+3]
        if codon in amino_acid:
            if amino_acid[codon] == "STOP":
                break
            protein.append(amino_acid[codon])
    return protein
