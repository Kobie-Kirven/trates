################################################################################
# A class for getting the peptides needed to build the structure
#
################################################################################

from Bio import SeqIO


class Slicer:
    def __init__(self, fileName):
        self.fileName = fileName

    def slice(self, start, stop):
        if stop <= start:
            return "Error: The ending residue is the same or less than the starting residue"
        else:
            for rec in SeqIO.parse(self.fileName, "fasta"):
                return str(rec.seq)[(start - 1) : (stop)]

    def sliceNC(self, start, stop):
        for rec in SeqIO.parse(self.fileName, "fasta"):
            return (str(rec.seq)[(start - 1) : (stop)])[::-1]
