
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


	def renumberResidues(fileName, start, stop, outPath):
		pdb_io = PDB.PDBIO()
		pdb_parser = PDB.PDBParser()
		structure = pdb_parser.get_structure(" ", os.path.abspath(outPath + "/" +  fileName))
		new_resnums = [i + (start) for i in range((stop - start)+1)]

		for model in structure:
		    for chain in model:
		    	for z, residue in enumerate(chain.get_residues()):
		    		res_id = list(residue.id)
		    		res_id[1] = new_resnums[z]
		    		residue.id = tuple(res_id)

		pdb_io.set_structure(structure)
		pdb_io.save(outPath + "/" +  fileName)
