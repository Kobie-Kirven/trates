
from .PeptideBuilder import *
from Bio import PDB, SeqIO
import os

class Structure:

	def buildStructure(sequence, outName, outPath):
		term = make_extended_structure(sequence)
		out = PDB.PDBIO()
		out.set_structure(term)
		out.save(outName)
		os.system("mv " + outName + " " + outPath)
