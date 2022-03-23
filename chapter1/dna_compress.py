from sys import getsizeof


class Compressedgenee:
    def __init__(self, gene: str) -> None:
        self.__gene_bit_string: int = 1  # start with sentinel
        self._compress(gene=gene)
        self.__check_size(gene=gene)

    def __check_size(self, gene: str) -> None:
        print(f' the gene size is {getsizeof(gene)} byts')
        print(
            f'after using compress class {getsizeof(self.__gene_bit_string)} byts')

    def _compress(self, gene: str) -> None:
        for nucleotide in gene.upper():
            self.__gene_bit_string <<= 2  # shift left two bits
            if nucleotide == "A":  # change last two bits to 00
                self.__gene_bit_string |= 0b00
            elif nucleotide == "C":  # change last two bits to 01
                self.__gene_bit_string |= 0b01
            elif nucleotide == "G":  # change last two bits to 10
                self.__gene_bit_string |= 0b10
            elif nucleotide == "T":  # change last two bits to 11
                self.__gene_bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.__gene_bit_string.bit_length() - 1, 2):  # - 1 to exclude sentinel
            # return check two bits [i][i+1]
            bits: int = self.__gene_bit_string >> i & 0b11
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # C
                gene += "C"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]  # [::-1] reverses string by slicing backward

    def get_gene___gene_bit_string(self) -> int:
        return self.__gene_bit_string

    def __repr__(self) -> str:
        return f'gene it {bin(self.__gene_bit_string)}'


gene = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGC\
CATGGATCGATTATA" * 100
test = Compressedgenee(gene=gene)
# print(test)
# print(test.decompress())
