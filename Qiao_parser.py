import sys
import os.path
from libsbml import *
from bioservices import BioModels
import difflib
import simplesbml
from django.utils.encoding import smart_str, smart_unicode
import sqlite3
import json
from pprint import pprint

BM = BioModels()
reader = SBMLReader()

l= 'MODEL6185746832.xml'
#l= 'BIOMD0000000528.xml'
document = reader.readSBML(l)
m = document.getModel();
print(m)
parList = m.getListOfParameters().getListOfAllElements()


print(m.getListOfAllElements())
print(parList)

spList = m.getListOfSpecies().getListOfAllElements()
reactionsList = m.getListOfReactions()


for sp in spList:
	print(sp)
	print(sp.getInitialAmount(),sp.getInitialConcentration(),sp.getUnits(),sp.getSubstanceUnits(),sp.getAnnotationString(),sp.getNotes(),sp.getSpeciesType())
	print(sp.getSBOTerm())
	sp.setUnits('M')
for par in parList:
	print(par)
	print(par.getValue(),par.getUnits())

for reaction in reactionsList:
	print(reaction)
	print(reaction.getKineticLaw().getFormula())
	print(reaction.getListOfReactants().getListOfAllElements(),reaction.getListOfProducts().getListOfAllElements())
	print(reaction.getListOfModifiers().getListOfAllElements())
	print(reaction.getAnnotationString())

for sp in spList:
	print(sp)
	print(sp.getInitialAmount(),sp.getInitialConcentration(),sp.getUnits(),sp.getSubstanceUnits(),sp.getAnnotationString(),sp.getNotes(),sp.getSpeciesType())
	print(sp.getSBOTerm())