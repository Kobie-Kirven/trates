import os
from Bio.PDB import *

class TerminiStructure:

    def __init__(self, pdb):
        self.pdb = pdb

    def getStructure(self):
        '''Get the Bio.PDB structure'''
        return PDBParser().get_structure(self.pdb.strip(".pdb"), self.pdb)

    def getAllAtoms(self):
        '''Get all of the atoms in a structure
            
            input - pdb ifle
            output - a list with [chain[residue[atom]]]
        '''
        structure = TerminiStructure.getStructure(self)
        allAtoms = []
        for model in structure:
            for chain in model:
                chainAtoms = []
                for residue in chain:
                    res = []
                    for atom in residue:
                        res.append(atom)
                    chainAtoms.append(res)
                allAtoms.append(chainAtoms)
        return allAtoms



class NativeContacts(TerminiStructure):

    '''A class for finding native contacts'''

    def getIntermolecularContacts(self, distance):
        '''Calculate the native contacts between 2 termini
            
            input - cutoff distance in angstroms
            output - a count of native contacts
        '''
        allAtoms = TerminiStructure.getAllAtoms(self)
        contacts = 0
        for z in range(len(allAtoms[0])):
            for t in range(len(allAtoms[1])):
                for a in allAtoms[0][z]:
                    for b in allAtoms[1][t]:
                        if (a - b) < distance:
                            contacts += 1
        return contacts

    def getIntramolecularContacts(self, distance, residueCutoff,chain):
        '''Calculate the native contacts within each chain
            
            input - cutoff distance in angstroms, 
                    Residue distance cutoff, 
                    chain number of structure

            output - count of native contacts
        '''
        allAtoms = TerminiStructure.getAllAtoms(self)
        specChain = allAtoms[chain]
        count = 0

        for i in range(len(specChain)):
            for z in range(i + 1, len(specChain)):
                if i != z and (z < (i + residueCutoff) or z > (i - residueCutoff)):
                    for atomi in specChain[i]:
                        for atomz in specChain[z]:
                            if atomi - atomz <= residueCutoff:
                                count += 1
        return count

    def getAllContacts(self, distance, residueCutoff):
    	""" Calculate all of the native contacts

    	input - cutoff distance in angstroms,
    		  - Residue distance cutoff

    	output - count of native contacts
    	"""
    	total = NativeContacts.getIntermolecularContacts(distance)
    	for i in range(3):
    		total += NativeContacts.getIntramolecularContacts(distance, residueCutoff, i)
    	return total







