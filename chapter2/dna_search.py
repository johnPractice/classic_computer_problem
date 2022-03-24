from enum import IntEnum
from typing import List, Tuple

# # define basic type


class Nucleotide(IntEnum):
    A = 1
    C = 2
    G = 3
    T = 4


# Codon contains 3 Nucleotide
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]


def custome_codon_enumerate(iterable, start=0, step=1) -> Codon:
    '''Costome Enumerate for create codon from iterable'''
    counter: int = len(iterable)

    counter = counter
    i: int = 0
    while i < counter:
        if i+2 < counter:
            extract_codon: Codon = (iterable[i], iterable[i+1], iterable[i+2])
            yield (start, extract_codon)
            start += step
            i += step
        else:
            break


def str_to_gene(gene_str: str) -> Gene:
    '''Convert input String to Gene'''
    gene: Gene = []
    for i, codon in custome_codon_enumerate(iterable=gene_str, start=0, step=3):
        gene.append(codon)
    return gene


def linear_gene_search(gene: Gene, key_codon: Codon) -> Tuple[bool, int]:
    index = 0
    for codon in gene:
        if codon == key_codon:
            return True, index
        index += 1
    return False, -1


def main():
    '''Main function for run'''

    gene_str: str = "ACGTCG"
    gene: Gene = str_to_gene(gene_str=gene_str)
    print(gene)
    check_codone, index = linear_gene_search(
        gene=gene, key_codon=(Nucleotide.A, Nucleotide.C, Nucleotide.G))
    print(check_codone)


if __name__ == '__main__':
    main()
