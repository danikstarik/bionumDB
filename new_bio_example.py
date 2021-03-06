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

l= 'BIOMD0000000442.xml'

document = reader.readSBML(l)
m = document.getModel();
print(m)
parList = m.getListOfParameters().getListOfAllElements()
paramDict = {}
basicTerms = set(["influenza","influenza A","Flu","infection","virus","viral","immune","feedback loops","MAPK","kinase"])
for param in parList:
	paramDict[param]= {"name":"","notes":"","tags":basicTerms}
print(paramDict)
termSet = basicTerms
numPar = m.getNumParameters()
print(numPar)
print(m.getListOfAllElements())
print('Parameters \n')
pa = 0

print(parList[2].getIdAttribute())
print(m.getListOfReactions().getListOfAllElements())

print('Reactions \n')

rea = 0
numRea = m.getNumReactions()
print(numRea)
while rea< numRea:
	reaction = m.getReaction(rea)
	print(reaction)

	mods = set()
	for mod in reaction.getListOfModifiers():
		mods.add(mod.getSpecies())
	products = set()
	for prod in reaction.getListOfProducts():
		products.add(prod.getSpecies())
	reactants = set()
	for reactant in reaction.getListOfReactants():
		reactants.add(reactant.getSpecies())
	localTerms =  mods | products | reactants
	f = reaction.getKineticLaw().getFormula()
	for p in paramDict.keys():
		if p.getIdAttribute() in f:
			paramDict[p]["name"]=f
			paramDict[p]["notes"]+=f +'  ;  '
			paramDict[p]["tags"] = paramDict[p]["tags"] | localTerms
	termSet = termSet | localTerms
	rea+=1


ruleList = m.getListOfRules()
for rule in ruleList:
	var = rule.getVariable()
	f=rule.getFormula()
	for p in paramDict.keys():
		if p.getIdAttribute() in f:
			paramDict[p]["notes"]+=f+'  ;  '
			paramDict[p]["tags"].add(var)
			paramDict[p]["name"] = var

#print(termSet)
#print(paramDict)
thisModel = m.getName()
print(thisModel)
JSONstringDict = {}

i_old = 263
i = i_old
for p in paramDict.keys():
	paramDict[p]["name"]="|"+p.getIdAttribute()+"|  "+paramDict[p]["name"]
	JSONstringDict[i]={"index":i,"user":"danikstarik","name":paramDict[p]["name"],"symbol":p.getIdAttribute(),"value":p.getValue(),"units":p.getUnits(),"notes":paramDict[p]["notes"],"constant":p.getConstant()}
	JSONstringDict[i]["tags"] = list(paramDict[p]["tags"])
	tup = (str(thisModel),"https://www.ebi.ac.uk/biomodels-main/"+l[:len(l)-4])
	JSONstringDict[i]["models"] = [tup]
	i+=1
print(i)

for key in JSONstringDict.keys():
	data = JSONstringDict[key]
	file = 'ex'+str(JSONstringDict[key]["index"])+'.json'
	with open(file, 'w') as outfile:
	    json.dump(data, outfile)
print('done')
