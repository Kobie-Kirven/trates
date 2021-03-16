
from .PeptideBuilder import *
from Bio import PDB, SeqIO


class Structure:

	def buildStructure(sequence, outName):
		term = make_extended_structure(sequence)
		out = PDB.PDBIO()
		out.set_structure(term)
		out.save(outName)
